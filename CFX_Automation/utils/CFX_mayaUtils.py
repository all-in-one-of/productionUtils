import maya.cmds as cmds
import os, glob, json

#split WEFX_ASSETNAEM_CTRLSETNAME into list, ignore namespace
def returnWEFXTag(inputName):
    nspace = cmds.ls(inputName, l=True, sns=True)[1]
    baseName = inputName.split('|')[-1]
    if not nspace == ':':
        baseName = baseName.split(':')[-1]
    baseName = baseName.split('_')
    return baseName

#swap refernce by matching first part of filename to rigConfig file
def swapReference(rigConfig):
    sceneName = cmds.file(q=True, sceneName=True)
    refs = cmds.file(q=True, r=True)

    if refs:
        for ref in refs:
            rfn = cmds.referenceQuery(ref, rfn=True)
            fpath = cmds.referenceQuery(rfn, filename=True, wcn=True)
            if cmds.referenceQuery(rfn, il=True):
                #corresponded ref is loaded, no need to swap
                return True
            else:
                baseRig = os.path.basename(fpath)
                rigName = baseRig.split('_')[0]#get first part of filename

                if rigName in rigConfig.keys():
                    targetRig = os.path.join(rigConfig[rigName]['animRigPath'], baseRig)
                    if os.path.isfile(targetRig):
                        #load reference if file exist.
                        cmds.file(targetRig, lr=rfn)
                    return True
                else:
                    print 'CFX AUTOMATION _ swapReference _ : rigConfig key: %s not existed.'%rigName
                    return False 
    else:
        print 'CFX AUTOMATION _ swapReference _ : there is no reference existed in file %s'%sceneName
        return False

#Naming need to change if rig file naming change
#Selection set naming convention WEFX_ASSETNAME_SETNAME
def exportAnimationNode(outPath, rigConfig, anmNodeFile, jsonNodeFile, tarSet):    
    ctlNs = cmds.ls("*:WEFX_*_*", type='objectSet')
    ctl = cmds.ls("WEFX_*_*", type='objectSet')#if no namespace
    target = ctlNs + ctl
    
    #get All avaialbe set member in a dict, different set store in different sub-dic
    #{"0":{"tag":"ASSETNAME", "member":[list of member]},"1":{"tag".......}}
    availableSet = getSelectionSetMember(rigConfig, 'ctrlSet')
    
    if not availableSet:
        sceneName = cmds.file(q=True, sceneName=True)
        print 'CFX AUTOMATION _ exportAnimationNode _ : no aviableSet in the file %s'%sceneName
        return False

    count = 0
    animData={}
    allNode = []
    for k in availableSet:
        tag = availableSet[k]['tag']
        sel = availableSet[k]['member']
        allNode += sel
        animationNodeType =availableSet[k]['anmNodeType']        

        animData[count] = {}
        nspace = cmds.ls(k,l=True,sns=True)[1]
        if nspace==':':
            nspace = ''
        animData[count]['namespace'] = nspace

        animData[count]['targetAsset'] = tag
        filePattern = '%s_*.%s'%(rigConfig[tag]['animRigName'], rigConfig[tag]['animRigType'])#need to fix if naming change
        targetPath = os.path.join(rigConfig[tag]['animRigPath'],filePattern)
        fileList = glob.glob(targetPath)
        animData[count]['targetRigFile'] = sorted(fileList)[-1]

        '''
        #use different version for animation
        version = cmds.getAttr('%s.WEFX_version'%k) 

        if not version == 0:
            diffVersionFile =  rigConfig[tag[1]]['animRigName']+'.v%s.'%version.zfill(2)+ rigConfig[tag[1]]['animRigType']#need to fix if naming change
            if os.path.isfile(diffVersionFile):
                animData[count]['targetRigFile'] = diffVersionFile
        '''

        animData[count]['animCtl'] = {}
        animData[count]['nonKeyCtl'] = {}
        animNodes = []

        for node in sel:
            availableAttrs = cmds.listAttr(node, v=True, k=True, u=True)

            if availableAttrs:
                for a in availableAttrs:
                    aNode = cmds.listConnections('%s.%s'%(node, a), s=True, d=False, scn=True)                    
                    if aNode:
                        for n in aNode:
                            #if there is connection to attr, and source is animation                                                
                            if cmds.objectType(n) in animationNodeType:   
                                if not node in animData[count]['animCtl'].keys():
                                    animData[count]['animCtl'][node] = {}      
                                animData[count]['animCtl'][node][a] = n
                                animNodes.append(n)
                    else:
                        #no animation, and no connection
                        currentVal = cmds.getAttr('%s.%s'%(node, a))
                        if not node in animData[count]['nonKeyCtl'].keys():
                            animData[count]['nonKeyCtl'][node] = {}
                        animData[count]['nonKeyCtl'][node][a] = currentVal

    #allNode contains all animationCurve Node that needs to be exported.
    cmds.select(allNode, r=True)
    sceneName = cmds.file(q=True, sceneName=True)
    extFile = os.path.join(outPath, anmNodeFile )
    extJson = os.path.join(outPath,jsonNodeFile)
    outFile = cmds.file(extFile, force=True, type='mayaAscii',eas=True)
    animData[count]['animFile'] = outFile
    count += 1

    #write json file of animation data
    with open( extJson, 'w') as f:
        json.dump(animData,f)
    return extJson
    cmds.select(cl=True)
    print 'CFX AUTOMATION _ exportAnimationNode _ : finish exporting animation data.'


#recreate a clean animation file, this is our init file
def generateCleanAnimation(config):
    print 'CFX AUTOMATION _ generateCleanAnimation _ : generate clean animation file stage'
    for g in config:
        if not g == 'outFile':
            #print config[g]['targetRigFile']
            if os.path.isfile(config[g]['targetRigFile']):
                ref =cmds.file(config[g]['targetRigFile'],r=True,ignoreVersion=True,mergeNamespacesOnClash=False,ns=config[g]['namespace'],options="v=0;")

            if 'animFile' in config[g].keys():
                cmds.file(config[g]['animFile'], i=True, namespace=":", options="mo=0")
                for i in config[g]['animCtl'].keys():
                    for attr in config[g]['animCtl'][i].keys():
                        cmds.connectAttr('%s.output'%config[g]['animCtl'][i][attr], '%s.%s'%(i,attr), f=True)

            for i in config[g]['nonKeyCtl'].keys():
                for attr in config[g]['nonKeyCtl'][i].keys():
                    cmds.setAttr('%s.%s'%(i,attr), config[g]['nonKeyCtl'][i][attr])


#do preroll and postroll
def extendAnimPrePostRoll(selection, config, sf, ef, preRollNum, preRollHold, cfxPreRollNum, postRollNum, defaultNum):
    for sel in selection:
        # find available attrs
        if not cmds.objExists(sel):
            print 'CFX AUTOMATION _ extendAnimPrePostRoll _ : %s not exist'%sel


        attrs = cmds.listAttr(sel, v=True, k=True, u=True)
        if attrs:
            for attr in attrs:
                attrValidate = False
                if not cmds.getAttr('%s.%s'%(sel,attr), type=True) == 'bool':
                    if not config == None:
                        tarData = removeNameSapce(sel)
                        if 'ctrl' in config.keys()   :          
                            if tarData in config['ctrl'].keys():
                                if attr in config['ctrl'][tarData].keys():
                                    defaultVal = config['ctrl'][tarData][attr]
                                    attrValidate = True
                    else:
                        connection = cmds.listConnections('%s.%s'%(sel, attr), s=True, d=True)
                        if connection:
                            if cmds.objectType(connection[0]) in ["animCurveTA", "animCurveTL","animCurveTT","animCurveTU"]:
                                defaultVal = cmds.attributeQuery(attr, node=sel, ld=True)[0]
                                attrValidate = True
                        else:
                            defaultVal = cmds.attributeQuery(attr, node=sel, ld=True)[0]
                            attrValidate = True

                if attrValidate:
                    keys = cmds.keyframe(sel, at=attr, q=True)

                    if keys:
                        vals = cmds.keyframe(sel, at=attr,t=(keys[0], keys[-1]), q=True, vc=True)
                        keyRange = range(int(sf), int(ef)+1)
                        matchRange = sorted(list(set(keyRange) & set(keys)))
                        if matchRange:
                            if not matchRange[0] == sf:
                                cmds.setKeyframe(sel, at=attr, insert=True, t=(sf,sf))
                            if not matchRange[-1] == ef:
                                cmds.setKeyframe(sel, at=attr, insert=True, t=(ef,ef))
                            
                        else:
                            if keys[-1] < sf:
                                if not cmds.setInfinity(sel, at=attr, q=True, poi=True)[0] == 'constant':
                                    cmds.bakeResults(sel, at=attr, t=(sf, ef), sb=1)
                                else:
                                    cmds.setKeyframe(sel, at=attr, insert=True, t=(sf,sf))
                                    
                            if keys[0] > ef:       
                                if not cmds.setInfinity(sel, at=attr, q=True, pri=True)[0] == 'constant':
                                    cmds.bakeResults(sel, at=attr, t=(sf, ef), sb=1)
                                else:
                                    cmds.setKeyframe(sel, at=attr, insert=True, t=(ef,ef)) 
                        #remove frame outside sf to ef
                        if keys[0] < sf:
                            cmds.cutKey(sel, at=attr, t=(keys[0],sf-1), clear=True)
                        if keys[-1] > ef:
                            cmds.cutKey(sel, at=attr, t=(ef+1,keys[-1]), clear=True)
                        
                        setPrePostRoll(preRollNum, postRollNum, sel, attr)
                        setPreRollFrameHold(preRollHold,sel,attr)
                        setCFXPreRoll(cfxPreRollNum, sel, attr)
                        preRollToDefault(defaultNum, defaultVal, sel, attr)
                    else:
                        sfVal = cmds.getAttr('%s.%s'%(sel,attr))
                        if not sfVal == defaultVal:                    
                            cmds.setKeyframe(sel, at=attr, t=(sf,sf), v=sfVal)
                            setPrePostRoll(preRollNum,0,sel,attr)
                            setPreRollFrameHold(preRollHold, sel,attr)
                            setCFXPreRoll(cfxPreRollNum, sel, attr)
                            preRollToDefault(defaultNum, defaultVal, sel, attr)
                        else:
                            pass
    
    print 'CFX AUTOMATION _ extendAnimPrePostRoll _ : finish extended'

def setPreRollFrameHold(preRollHold, obj, attr):
    if not preRollHold == 0:
        if not cmds.setInfinity(obj, at=attr, q=True, pri=True)[0] == 'constant':
            cmds.setInfinity(obj, at=attr, pri='constant')
        keys = cmds.keyframe(obj, at=attr, q=True)
        preRollHoldFrame = keys[0] - preRollHold
        cmds.bakeResults(obj, at=attr, t=(preRollHoldFrame, keys[0]),simulation=False,sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=False,removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False)

def setCFXPreRoll(CFXPreRollNum, obj, attr):
    if not CFXPreRollNum == 0:
        setPrePostRoll(1, 0, obj, attr)
        keys = cmds.keyframe(obj, at=attr, q=True)
        offset = (CFXPreRollNum-1)*-1
        cmds.keyframe(obj, at=attr, e=True, iub=True, r=True, o="over", tc= offset, t=(keys[0],keys[0]))
        cmds.bakeResults(obj, at=attr, t=(keys[0]-offset, keys[0]),simulation=False,sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=False,removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False)
        #pass

def setPrePostRoll(preRollNum, postRollNum, obj, attr):    
    keys = cmds.keyframe(obj, at=attr, q=True)
    if not preRollNum == 0:
        if cmds.setInfinity(obj, at=attr, q=True, pri=True)[0] == 'constant':
            cmds.setInfinity(obj, at=attr, pri='linear')
        preRollFrame = keys[0] - preRollNum
        cmds.bakeResults(obj, at=attr, t=(preRollFrame, keys[0]),simulation=False,sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=False,removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False)
        #cmds.setKeyframe(obj, at=attr, insert=True, t=(preRollFrame,preRollFrame))        

    if not postRollNum == 0:
        if cmds.setInfinity(obj, at=attr, q=True, poi=True)[0] == 'constant':
            cmds.setInfinity(obj, at=attr, poi='linear')
        postRollFrame = keys[-1] + postRollNum        
        cmds.bakeResults(obj, at=attr, t=(keys[-1], postRollFrame),simulation=False,sampleBy=1,disableImplicitControl=True,preserveOutsideKeys=True,sparseAnimCurveBake=False,removeBakedAttributeFromLayer=False,removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False)
        #cmds.setKeyframe(obj, at=attr, insert=True, t=(postRollFrame,postRollFrame))

def preRollToDefault(defaultNum, defaultVal, obj, attr):
    if not defaultNum == 0:
        keys = cmds.keyframe(obj, at=attr, q=True)
        rollToDefaultFrame = keys[0]-defaultNum
        cmds.setKeyframe(obj, at=attr, itt='flat', ott='flat', t=(rollToDefaultFrame,rollToDefaultFrame), v=defaultVal)
        #cmds.setInfinity(obj, at=attr, pri='constant')

#return all available selection set member
def getSelectionSetMember(rigConfig, targetSet):        
    ctlNs = cmds.ls("*:WEFX_*_*", type='objectSet')
    ctl = cmds.ls("WEFX_*_*", type='objectSet')#if no namespace
    target = ctlNs + ctl

    availableSet = {}

    if target:
        for k in target:
            tag = returnWEFXTag(k)             
            selShape = cmds.listRelatives(k, f=True, ni=True)
            sel = []
            availableSet = {}
            if tag[0] == 'WEFX':
                if tag[1] in rigConfig.keys():                    
                    if '_'.join(tag) == rigConfig[tag[1]][targetSet]:
                        
                        availableSet[k] = {}
                        selShape = cmds.listRelatives(k, f=True, ni=True)
                        sel = []

                        for i in selShape:
                            node = cmds.listRelatives(i, p=True, type='transform', f=True)[0]     
                            if not node in sel:
                                sel.append(node) 
                        availableSet[k]['member'] = sel
                        availableSet[k]['tag'] = tag[1]
                        availableSet[k]['anmNodeType'] =  rigConfig[tag[1]]['anmNodeType']
    
    if availableSet:
        return availableSet
    else:
        return False


def getAvailableAttrs(sel, excludeNode=None):
    attrs = cmds.listAttr(sel, v=True, k=True)
    outAttrs=[]
    for k in attrs:
        connection = cmds.listConnections('%s.%s'%(i,k), s=True, d=False)
        if connection:
            if excludeNode:
                if cmds.objectType(connection[0]) in excludeNode:
                    outAttrs.append(k)
        else:
            outAttrs.append(k)

def getDefaultVal(sel, attr):
    return cmds.attributeQuery(sel, node=sel, ld=True) 

def removeNameSapce(inputData):
    tarData = inputData.split('|') 
    for idx in range(len(tarData)):
        tarData[idx] = tarData[idx].split(':')[-1]
    tarData = '|'.join(tarData)
    return tarData

def swapNameSapce(inputData, namespace):
    tarData = inputData.split('|') 
    for idx in range(len(tarData)):
        tarData[idx] = tarData[idx].split(':')[-1]
        tarData[idx] = namespace + ':' + tarData[idx] 
    tarData = '|'.join(tarData)
    return tarData
