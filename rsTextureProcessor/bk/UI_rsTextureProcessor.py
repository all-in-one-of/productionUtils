# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\Han\scriptBk\rsTextureProcessor\UI_rsTextureProcessor.ui'
#
# Created: Thu Mar 02 15:47:24 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 501)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 281, 461))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pB_doMakeTx = QtGui.QPushButton(self.frame)
        self.pB_doMakeTx.setGeometry(QtCore.QRect(10, 360, 261, 61))
        self.pB_doMakeTx.setAcceptDrops(True)
        self.pB_doMakeTx.setFlat(False)
        self.pB_doMakeTx.setObjectName("pB_doMakeTx")
        self.lE_log = QtGui.QLineEdit(self.frame)
        self.lE_log.setEnabled(True)
        self.lE_log.setGeometry(QtCore.QRect(10, 430, 261, 21))
        self.lE_log.setAcceptDrops(False)
        self.lE_log.setAutoFillBackground(False)
        self.lE_log.setFrame(False)
        self.lE_log.setReadOnly(True)
        self.lE_log.setObjectName("lE_log")
        self.gB_overwrite = QtGui.QGroupBox(self.frame)
        self.gB_overwrite.setGeometry(QtCore.QRect(10, 150, 261, 51))
        self.gB_overwrite.setCheckable(True)
        self.gB_overwrite.setChecked(False)
        self.gB_overwrite.setObjectName("gB_overwrite")
        self.cB_overwrite = QtGui.QCheckBox(self.gB_overwrite)
        self.cB_overwrite.setGeometry(QtCore.QRect(11, 19, 61, 20))
        self.cB_overwrite.setObjectName("cB_overwrite")
        self.radioButton = QtGui.QRadioButton(self.gB_overwrite)
        self.radioButton.setGeometry(QtCore.QRect(90, 20, 51, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtGui.QRadioButton(self.gB_overwrite)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 20, 51, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtGui.QRadioButton(self.gB_overwrite)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 20, 51, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.tabWid = QtGui.QTabWidget(self.frame)
        self.tabWid.setEnabled(True)
        self.tabWid.setGeometry(QtCore.QRect(10, 10, 261, 131))
        self.tabWid.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWid.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWid.setElideMode(QtCore.Qt.ElideNone)
        self.tabWid.setDocumentMode(True)
        self.tabWid.setObjectName("tabWid")
        self.tabWid_folder = QtGui.QWidget()
        self.tabWid_folder.setObjectName("tabWid_folder")
        self.gB_srouceFolder = QtGui.QGroupBox(self.tabWid_folder)
        self.gB_srouceFolder.setGeometry(QtCore.QRect(0, 10, 261, 101))
        self.gB_srouceFolder.setObjectName("gB_srouceFolder")
        self.cmB_sourceDirPath = QtGui.QComboBox(self.gB_srouceFolder)
        self.cmB_sourceDirPath.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.cmB_sourceDirPath.setAcceptDrops(True)
        self.cmB_sourceDirPath.setEditable(False)
        self.cmB_sourceDirPath.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.cmB_sourceDirPath.setDuplicatesEnabled(False)
        self.cmB_sourceDirPath.setObjectName("cmB_sourceDirPath")
        self.tB_sourceDirBrowse = QtGui.QToolButton(self.gB_srouceFolder)
        self.tB_sourceDirBrowse.setGeometry(QtCore.QRect(220, 20, 27, 21))
        self.tB_sourceDirBrowse.setObjectName("tB_sourceDirBrowse")
        self.cB_convertAll = QtGui.QRadioButton(self.gB_srouceFolder)
        self.cB_convertAll.setGeometry(QtCore.QRect(10, 80, 198, 17))
        self.cB_convertAll.setChecked(False)
        self.cB_convertAll.setObjectName("cB_convertAll")
        self.cB_subFolder = QtGui.QRadioButton(self.gB_srouceFolder)
        self.cB_subFolder.setGeometry(QtCore.QRect(10, 50, 121, 20))
        self.cB_subFolder.setChecked(True)
        self.cB_subFolder.setObjectName("cB_subFolder")
        self.sB_subLevel = QtGui.QSpinBox(self.gB_srouceFolder)
        self.sB_subLevel.setGeometry(QtCore.QRect(140, 50, 53, 22))
        self.sB_subLevel.setMinimum(0)
        self.sB_subLevel.setMaximum(1000)
        self.sB_subLevel.setProperty("value", 0)
        self.sB_subLevel.setObjectName("sB_subLevel")
        self.tabWid.addTab(self.tabWid_folder, "")
        self.tabWid_files = QtGui.QWidget()
        self.tabWid_files.setObjectName("tabWid_files")
        self.gB_sourceFiles = QtGui.QGroupBox(self.tabWid_files)
        self.gB_sourceFiles.setGeometry(QtCore.QRect(0, 10, 261, 101))
        self.gB_sourceFiles.setObjectName("gB_sourceFiles")
        self.tB_sourceFileBrowse = QtGui.QToolButton(self.gB_sourceFiles)
        self.tB_sourceFileBrowse.setGeometry(QtCore.QRect(220, 70, 27, 21))
        self.tB_sourceFileBrowse.setObjectName("tB_sourceFileBrowse")
        self.tB_clearList = QtGui.QToolButton(self.gB_sourceFiles)
        self.tB_clearList.setGeometry(QtCore.QRect(220, 20, 27, 21))
        self.tB_clearList.setObjectName("tB_clearList")
        self.tB_removeSel = QtGui.QToolButton(self.gB_sourceFiles)
        self.tB_removeSel.setGeometry(QtCore.QRect(220, 40, 27, 21))
        self.tB_removeSel.setObjectName("tB_removeSel")
        self.lW_sourceFiles = QtGui.QListWidget(self.gB_sourceFiles)
        self.lW_sourceFiles.setGeometry(QtCore.QRect(10, 20, 201, 71))
        self.lW_sourceFiles.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lW_sourceFiles.setObjectName("lW_sourceFiles")
        self.tabWid.addTab(self.tabWid_files, "")
        self.tabWid_maya = QtGui.QWidget()
        self.tabWid_maya.setEnabled(True)
        self.tabWid_maya.setObjectName("tabWid_maya")
        self.gB_sourceShd = QtGui.QGroupBox(self.tabWid_maya)
        self.gB_sourceShd.setGeometry(QtCore.QRect(0, 10, 261, 51))
        self.gB_sourceShd.setMinimumSize(QtCore.QSize(0, 0))
        self.gB_sourceShd.setFlat(False)
        self.gB_sourceShd.setObjectName("gB_sourceShd")
        self.rB_allShd = QtGui.QRadioButton(self.gB_sourceShd)
        self.rB_allShd.setGeometry(QtCore.QRect(11, 20, 46, 20))
        self.rB_allShd.setChecked(True)
        self.rB_allShd.setObjectName("rB_allShd")
        self.rB_selectedShd = QtGui.QRadioButton(self.gB_sourceShd)
        self.rB_selectedShd.setGeometry(QtCore.QRect(70, 20, 98, 20))
        self.rB_selectedShd.setObjectName("rB_selectedShd")
        self.tabWid.addTab(self.tabWid_maya, "")
        self.tabWid_options = QtGui.QTabWidget(self.frame)
        self.tabWid_options.setEnabled(True)
        self.tabWid_options.setGeometry(QtCore.QRect(10, 210, 261, 141))
        self.tabWid_options.setTabPosition(QtGui.QTabWidget.North)
        self.tabWid_options.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWid_options.setElideMode(QtCore.Qt.ElideNone)
        self.tabWid_options.setDocumentMode(True)
        self.tabWid_options.setObjectName("tabWid_options")
        self.tabWid_makeTx = QtGui.QWidget()
        self.tabWid_makeTx.setObjectName("tabWid_makeTx")
        self.gB_makeTxBinary = QtGui.QGroupBox(self.tabWid_makeTx)
        self.gB_makeTxBinary.setGeometry(QtCore.QRect(0, 10, 261, 51))
        self.gB_makeTxBinary.setObjectName("gB_makeTxBinary")
        self.tB_sourceCmbBrowse = QtGui.QToolButton(self.gB_makeTxBinary)
        self.tB_sourceCmbBrowse.setGeometry(QtCore.QRect(220, 20, 27, 21))
        self.tB_sourceCmbBrowse.setObjectName("tB_sourceCmbBrowse")
        self.lE_cmdPath = QtGui.QLineEdit(self.gB_makeTxBinary)
        self.lE_cmdPath.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.lE_cmdPath.setReadOnly(True)
        self.lE_cmdPath.setObjectName("lE_cmdPath")
        self.gB_commandFlags = QtGui.QGroupBox(self.tabWid_makeTx)
        self.gB_commandFlags.setGeometry(QtCore.QRect(0, 70, 261, 51))
        self.gB_commandFlags.setCheckable(True)
        self.gB_commandFlags.setChecked(False)
        self.gB_commandFlags.setObjectName("gB_commandFlags")
        self.lE_cmdFlag = QtGui.QLineEdit(self.gB_commandFlags)
        self.lE_cmdFlag.setGeometry(QtCore.QRect(10, 20, 241, 21))
        self.lE_cmdFlag.setObjectName("lE_cmdFlag")
        self.tabWid_options.addTab(self.tabWid_makeTx, "")
        self.tabWid_option = QtGui.QWidget()
        self.tabWid_option.setObjectName("tabWid_option")
        self.gB_saveTo = QtGui.QGroupBox(self.tabWid_option)
        self.gB_saveTo.setGeometry(QtCore.QRect(0, 10, 261, 51))
        self.gB_saveTo.setFlat(False)
        self.gB_saveTo.setCheckable(True)
        self.gB_saveTo.setChecked(False)
        self.gB_saveTo.setObjectName("gB_saveTo")
        self.cmB_tarDirPath = QtGui.QComboBox(self.gB_saveTo)
        self.cmB_tarDirPath.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.cmB_tarDirPath.setAcceptDrops(True)
        self.cmB_tarDirPath.setEditable(True)
        self.cmB_tarDirPath.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.cmB_tarDirPath.setDuplicatesEnabled(False)
        self.cmB_tarDirPath.setObjectName("cmB_tarDirPath")
        self.tB_tarDirBrowse = QtGui.QToolButton(self.gB_saveTo)
        self.tB_tarDirBrowse.setGeometry(QtCore.QRect(220, 20, 27, 21))
        self.tB_tarDirBrowse.setObjectName("tB_tarDirBrowse")
        self.gB_imageFilter = QtGui.QGroupBox(self.tabWid_option)
        self.gB_imageFilter.setEnabled(True)
        self.gB_imageFilter.setGeometry(QtCore.QRect(0, 70, 261, 51))
        self.gB_imageFilter.setCheckable(True)
        self.gB_imageFilter.setChecked(False)
        self.gB_imageFilter.setObjectName("gB_imageFilter")
        self.lE_imageFilter = QtGui.QLineEdit(self.gB_imageFilter)
        self.lE_imageFilter.setGeometry(QtCore.QRect(10, 20, 231, 21))
        self.lE_imageFilter.setObjectName("lE_imageFilter")
        self.tabWid_options.addTab(self.tabWid_option, "")
        self.tabWid_filter = QtGui.QWidget()
        self.tabWid_filter.setObjectName("tabWid_filter")
        #self.gB_extra = QtGui.QGroupBox(self.tabWid_filter)
        #self.gB_extra.setEnabled(True)
        #self.gB_extra.setGeometry(QtCore.QRect(0, 10, 261, 111))
        #self.gB_extra.setCheckable(True)
        #self.gB_extra.setChecked(False)
        #self.gB_extra.setObjectName("gB_extra")
        #self.pB_goOiio = QtGui.QPushButton(self.gB_extra)
        #self.pB_goOiio.setGeometry(QtCore.QRect(170, 20, 79, 41))
        #self.pB_goOiio.setObjectName("pB_goOiio")
        #self.lE_oiioFlag = QtGui.QLineEdit(self.gB_extra)
        #self.lE_oiioFlag.setGeometry(QtCore.QRect(20, 70, 231, 21))
        #self.lE_oiioFlag.setText("")
        #self.lE_oiioFlag.setObjectName("lE_oiioFlag")
        #self.lE_suffix = QtGui.QLineEdit(self.gB_extra)
        #self.lE_suffix.setGeometry(QtCore.QRect(60, 20, 101, 21))
        #self.lE_suffix.setText("")
        #self.lE_suffix.setObjectName("lE_suffix")
        #self.label_suffix = QtGui.QLabel(self.gB_extra)
        #self.label_suffix.setGeometry(QtCore.QRect(20, 20, 51, 16))
        #self.label_suffix.setObjectName("label_suffix")
        #self.label_oiioFlag = QtGui.QLabel(self.gB_extra)
        #self.label_oiioFlag.setGeometry(QtCore.QRect(20, 50, 121, 16))
        #self.label_oiioFlag.setObjectName("label_oiioFlag")
        #self.tabWid_options.addTab(self.tabWid_filter, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 17))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuCmd = QtGui.QMenu(self.menubar)
        self.menuCmd.setObjectName("menuCmd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ac_confirm = QtGui.QAction(MainWindow)
        self.ac_confirm.setCheckable(True)
        self.ac_confirm.setChecked(True)
        self.ac_confirm.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.ac_confirm.setObjectName("ac_confirm")
        self.ac_currentList = QtGui.QAction(MainWindow)
        self.ac_currentList.setEnabled(False)
        self.ac_currentList.setObjectName("ac_currentList")
        self.ac_quit = QtGui.QAction(MainWindow)
        self.ac_quit.setObjectName("ac_quit")
        self.ac_createBatchFile = QtGui.QAction(MainWindow)
        self.ac_createBatchFile.setCheckable(False)
        self.ac_createBatchFile.setObjectName("ac_createBatchFile")
        self.ac_aboutTextureProcessor = QtGui.QAction(MainWindow)
        self.ac_aboutTextureProcessor.setObjectName("ac_aboutTextureProcessor")
        self.ac_aboutMe = QtGui.QAction(MainWindow)
        self.ac_aboutMe.setEnabled(True)
        self.ac_aboutMe.setObjectName("ac_aboutMe")
        self.ac_aboutOIIO = QtGui.QAction(MainWindow)
        self.ac_aboutOIIO.setObjectName("ac_aboutOIIO")
        self.menuMenu.addAction(self.ac_confirm)
        self.menuMenu.addAction(self.ac_currentList)
        self.menuMenu.addAction(self.ac_createBatchFile)
        self.menuMenu.addAction(self.ac_quit)
        self.menuCmd.addAction(self.ac_aboutTextureProcessor)
        self.menuCmd.addSeparator()
        self.menuCmd.addAction(self.ac_aboutMe)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuCmd.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWid.setCurrentIndex(2)
        self.tabWid_options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Redshift Convert Texture", None, QtGui.QApplication.UnicodeUTF8))
        self.pB_doMakeTx.setText(QtGui.QApplication.translate("MainWindow", "Run Texture Processor", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_overwrite.setTitle(QtGui.QApplication.translate("MainWindow", "Flag", None, QtGui.QApplication.UnicodeUTF8))
        self.cB_overwrite.setText(QtGui.QApplication.translate("MainWindow", "noskip", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "auto", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "sRGB", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "linear", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_srouceFolder.setTitle(QtGui.QApplication.translate("MainWindow", "source folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_sourceDirBrowse.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cB_convertAll.setText(QtGui.QApplication.translate("MainWindow", "Including All Sub Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.cB_subFolder.setText(QtGui.QApplication.translate("MainWindow", "Sub-Folder Level", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tabWid_folder), QtGui.QApplication.translate("MainWindow", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_sourceFiles.setTitle(QtGui.QApplication.translate("MainWindow", "source files", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_sourceFileBrowse.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_clearList.setText(QtGui.QApplication.translate("MainWindow", "c", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_removeSel.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tabWid_files), QtGui.QApplication.translate("MainWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_sourceShd.setTitle(QtGui.QApplication.translate("MainWindow", "source shader/texture", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_allShd.setText(QtGui.QApplication.translate("MainWindow", "ALL", None, QtGui.QApplication.UnicodeUTF8))
        self.rB_selectedShd.setText(QtGui.QApplication.translate("MainWindow", "Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tabWid_maya), QtGui.QApplication.translate("MainWindow", "Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_makeTxBinary.setTitle(QtGui.QApplication.translate("MainWindow", "texture processor binary", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_sourceCmbBrowse.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_commandFlags.setTitle(QtGui.QApplication.translate("MainWindow", "Custom Command Flags", None, QtGui.QApplication.UnicodeUTF8))
        self.lE_cmdFlag.setText(QtGui.QApplication.translate("MainWindow", "-u -oiio", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWid_options.setTabText(self.tabWid_options.indexOf(self.tabWid_makeTx), QtGui.QApplication.translate("MainWindow", "Texture Processor", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_saveTo.setTitle(QtGui.QApplication.translate("MainWindow", "Different tx Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.tB_tarDirBrowse.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.gB_imageFilter.setTitle(QtGui.QApplication.translate("MainWindow", "Custom Filter for Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.lE_imageFilter.setText(QtGui.QApplication.translate("MainWindow", "jpg png bmp tif tga exr", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWid_options.setTabText(self.tabWid_options.indexOf(self.tabWid_option), QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        #self.gB_extra.setTitle(QtGui.QApplication.translate("MainWindow", "oiiotools", None, QtGui.QApplication.UnicodeUTF8))
        #self.pB_goOiio.setText(QtGui.QApplication.translate("MainWindow", "go oiio", None, QtGui.QApplication.UnicodeUTF8))
        #self.label_suffix.setText(QtGui.QApplication.translate("MainWindow", "suffix", None, QtGui.QApplication.UnicodeUTF8))
        #self.label_oiioFlag.setText(QtGui.QApplication.translate("MainWindow", "oiio command flags", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWid_options.setTabText(self.tabWid_options.indexOf(self.tabWid_filter), QtGui.QApplication.translate("MainWindow", "Extra", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCmd.setTitle(QtGui.QApplication.translate("MainWindow", "help", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_confirm.setText(QtGui.QApplication.translate("MainWindow", " Confirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_currentList.setText(QtGui.QApplication.translate("MainWindow", "Display List", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_createBatchFile.setText(QtGui.QApplication.translate("MainWindow", "Create Batch", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_aboutTextureProcessor.setText(QtGui.QApplication.translate("MainWindow", "About TextureProcessor", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_aboutMe.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.ac_aboutOIIO.setText(QtGui.QApplication.translate("MainWindow", "About OIIO", None, QtGui.QApplication.UnicodeUTF8))

