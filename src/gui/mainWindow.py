# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 583)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(627, 583))
        MainWindow.setMaximumSize(QtCore.QSize(627, 583))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_1_tab = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1_tab.setGeometry(QtCore.QRect(10, 20, 611, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_1_tab.setFont(font)
        self.groupBox_1_tab.setFlat(False)
        self.groupBox_1_tab.setCheckable(False)
        self.groupBox_1_tab.setObjectName("groupBox_1_tab")
        self.label = QtWidgets.QLabel(self.groupBox_1_tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.label.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_1_tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 251, 29))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"font-weight:normal;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.button_get_user_info = QtWidgets.QPushButton(self.groupBox_1_tab)
        self.button_get_user_info.setGeometry(QtCore.QRect(280, 40, 111, 29))
        self.button_get_user_info.setStyleSheet("background-color:#525252;\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.button_get_user_info.setObjectName("button_get_user_info")
        self.button_get_user_info_clear = QtWidgets.QPushButton(self.groupBox_1_tab)
        self.button_get_user_info_clear.setGeometry(QtCore.QRect(400, 40, 101, 30))
        self.button_get_user_info_clear.setObjectName("button_get_user_info_clear")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 611, 311))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.toolBox = QtWidgets.QToolBox(self.groupBox)
        self.toolBox.setGeometry(QtCore.QRect(10, 20, 591, 281))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolBox.setFont(font)
        self.toolBox.setMouseTracking(False)
        self.toolBox.setAcceptDrops(False)
        self.toolBox.setAutoFillBackground(True)
        self.toolBox.setStyleSheet("")
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox.setLineWidth(0)
        self.toolBox.setMidLineWidth(5)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 591, 173))
        self.page.setObjectName("page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 60, 591, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_get_copy_active_user_info = QtWidgets.QPushButton(self.groupBox_2)
        self.button_get_copy_active_user_info.setGeometry(QtCore.QRect(10, 70, 91, 24))
        self.button_get_copy_active_user_info.setStyleSheet("background-color:#525252;\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.button_get_copy_active_user_info.setObjectName("button_get_copy_active_user_info")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 40, 191, 24))
        self.lineEdit_8.setAutoFillBackground(False)
        self.lineEdit_8.setStyleSheet("padding-left:5px;\n"
"font-size:11px;")
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_8.setReadOnly(False)
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 261, 16))
        self.label_8.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.comboBox_regions = CheckComboBox(self.groupBox_2)
        self.comboBox_regions.setGeometry(QtCore.QRect(400, 40, 111, 24))
        self.comboBox_regions.setCurrentText("")
        self.comboBox_regions.setObjectName("comboBox_regions")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(400, 20, 81, 16))
        self.label_9.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(280, 20, 71, 16))
        self.label_10.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.comboBox_offices = CheckComboBox(self.groupBox_2)
        self.comboBox_offices.setGeometry(QtCore.QRect(280, 40, 111, 24))
        self.comboBox_offices.setObjectName("comboBox_offices")
        self.comboBox_user_group = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_user_group.setGeometry(QtCore.QRect(520, 40, 61, 24))
        self.comboBox_user_group.setObjectName("comboBox_user_group")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(520, 20, 141, 16))
        self.label_11.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 40, 61, 24))
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"\n"
"")
        self.lineEdit_9.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(210, 20, 41, 16))
        self.label_13.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_13.setObjectName("label_13")
        self.button_get_user_info_clear_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_get_user_info_clear_2.setGeometry(QtCore.QRect(110, 70, 91, 24))
        self.button_get_user_info_clear_2.setObjectName("button_get_user_info_clear_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 221, 51))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("font-weight:bold;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_access = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_access.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_access.setChecked(True)
        self.radioButton_access.setObjectName("radioButton_access")
        self.radioButton_access_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_access_2.setGeometry(QtCore.QRect(100, 20, 111, 17))
        self.radioButton_access_2.setObjectName("radioButton_access_2")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 591, 173))
        self.page_2.setObjectName("page_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 591, 71))
        self.groupBox_6.setStyleSheet("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_15.setStyleSheet("font-size:11px;\n"
"font-weight:bold;")
        self.label_15.setObjectName("label_15")
        self.lineEdit_AccessType = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_AccessType.setGeometry(QtCore.QRect(10, 40, 81, 24))
        self.lineEdit_AccessType.setAutoFillBackground(False)
        self.lineEdit_AccessType.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_AccessType.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_AccessType.setReadOnly(True)
        self.lineEdit_AccessType.setPlaceholderText("")
        self.lineEdit_AccessType.setClearButtonEnabled(False)
        self.lineEdit_AccessType.setObjectName("lineEdit_AccessType")
        self.lineEdit_isSuperUser = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_isSuperUser.setGeometry(QtCore.QRect(100, 40, 71, 24))
        self.lineEdit_isSuperUser.setAutoFillBackground(False)
        self.lineEdit_isSuperUser.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_isSuperUser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_isSuperUser.setReadOnly(True)
        self.lineEdit_isSuperUser.setPlaceholderText("")
        self.lineEdit_isSuperUser.setClearButtonEnabled(False)
        self.lineEdit_isSuperUser.setObjectName("lineEdit_isSuperUser")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(100, 20, 71, 16))
        self.label_16.setStyleSheet("font-size:11px;\n"
"font-weight:bold;")
        self.label_16.setObjectName("label_16")
        self.lineEdit_userCreateRequestLimit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_userCreateRequestLimit.setGeometry(QtCore.QRect(180, 40, 71, 24))
        self.lineEdit_userCreateRequestLimit.setAutoFillBackground(False)
        self.lineEdit_userCreateRequestLimit.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_userCreateRequestLimit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_userCreateRequestLimit.setReadOnly(True)
        self.lineEdit_userCreateRequestLimit.setPlaceholderText("")
        self.lineEdit_userCreateRequestLimit.setClearButtonEnabled(False)
        self.lineEdit_userCreateRequestLimit.setObjectName("lineEdit_userCreateRequestLimit")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(180, 20, 71, 16))
        self.label_17.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_17.setObjectName("label_17")
        self.lineEdit_resetCreateRequestLimit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_resetCreateRequestLimit.setGeometry(QtCore.QRect(260, 40, 81, 24))
        self.lineEdit_resetCreateRequestLimit.setAutoFillBackground(False)
        self.lineEdit_resetCreateRequestLimit.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_resetCreateRequestLimit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_resetCreateRequestLimit.setReadOnly(True)
        self.lineEdit_resetCreateRequestLimit.setPlaceholderText("")
        self.lineEdit_resetCreateRequestLimit.setClearButtonEnabled(False)
        self.lineEdit_resetCreateRequestLimit.setObjectName("lineEdit_resetCreateRequestLimit")
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(260, 20, 81, 16))
        self.label_18.setStyleSheet("font-weight:bold;\n"
"font-size:11px;\n"
"")
        self.label_18.setObjectName("label_18")
        self.lineEdit_userApproveNeededLimit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_userApproveNeededLimit.setGeometry(QtCore.QRect(350, 40, 71, 24))
        self.lineEdit_userApproveNeededLimit.setAutoFillBackground(False)
        self.lineEdit_userApproveNeededLimit.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_userApproveNeededLimit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_userApproveNeededLimit.setReadOnly(True)
        self.lineEdit_userApproveNeededLimit.setPlaceholderText("")
        self.lineEdit_userApproveNeededLimit.setClearButtonEnabled(False)
        self.lineEdit_userApproveNeededLimit.setObjectName("lineEdit_userApproveNeededLimit")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(350, 20, 61, 16))
        self.label_19.setStyleSheet("font-size:11px;\n"
"font-weight:bold;")
        self.label_19.setObjectName("label_19")
        self.lineEdit_GroupID = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_GroupID.setGeometry(QtCore.QRect(430, 40, 51, 24))
        self.lineEdit_GroupID.setAutoFillBackground(False)
        self.lineEdit_GroupID.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_GroupID.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_GroupID.setReadOnly(True)
        self.lineEdit_GroupID.setPlaceholderText("")
        self.lineEdit_GroupID.setClearButtonEnabled(False)
        self.lineEdit_GroupID.setObjectName("lineEdit_GroupID")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(430, 20, 51, 16))
        self.label_20.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(490, 20, 101, 16))
        self.label_21.setStyleSheet("font-size:11px;\n"
"font-weight:bold;")
        self.label_21.setObjectName("label_21")
        self.lineEdit_PayConditions = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_PayConditions.setGeometry(QtCore.QRect(490, 40, 91, 24))
        self.lineEdit_PayConditions.setAutoFillBackground(False)
        self.lineEdit_PayConditions.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_PayConditions.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_PayConditions.setReadOnly(True)
        self.lineEdit_PayConditions.setPlaceholderText("")
        self.lineEdit_PayConditions.setClearButtonEnabled(False)
        self.lineEdit_PayConditions.setObjectName("lineEdit_PayConditions")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 80, 591, 71))
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_29.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_7)
        self.label_30.setGeometry(QtCore.QRect(100, 20, 71, 16))
        self.label_30.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_30.setObjectName("label_30")
        self.lineEdit_userCreateRequestLimit_Update = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_userCreateRequestLimit_Update.setGeometry(QtCore.QRect(180, 40, 71, 24))
        self.lineEdit_userCreateRequestLimit_Update.setAutoFillBackground(False)
        self.lineEdit_userCreateRequestLimit_Update.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#FFF;\n"
"border:1px solid #DDD;")
        self.lineEdit_userCreateRequestLimit_Update.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_userCreateRequestLimit_Update.setReadOnly(False)
        self.lineEdit_userCreateRequestLimit_Update.setPlaceholderText("")
        self.lineEdit_userCreateRequestLimit_Update.setClearButtonEnabled(False)
        self.lineEdit_userCreateRequestLimit_Update.setObjectName("lineEdit_userCreateRequestLimit_Update")
        self.label_31 = QtWidgets.QLabel(self.groupBox_7)
        self.label_31.setGeometry(QtCore.QRect(180, 20, 71, 16))
        self.label_31.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_7)
        self.label_32.setGeometry(QtCore.QRect(260, 20, 81, 16))
        self.label_32.setStyleSheet("font-weight:bold;\n"
"font-size:11px;\n"
"")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_7)
        self.label_33.setGeometry(QtCore.QRect(350, 20, 61, 16))
        self.label_33.setStyleSheet("font-size:11px;\n"
"font-weight:bold;")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_7)
        self.label_34.setGeometry(QtCore.QRect(430, 20, 51, 16))
        self.label_34.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_7)
        self.label_35.setGeometry(QtCore.QRect(490, 20, 101, 16))
        self.label_35.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.label_35.setObjectName("label_35")
        self.comboBox_AccessType = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_AccessType.setGeometry(QtCore.QRect(10, 40, 81, 24))
        self.comboBox_AccessType.setCurrentText("")
        self.comboBox_AccessType.setObjectName("comboBox_AccessType")
        self.comboBox_GroupID = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_GroupID.setGeometry(QtCore.QRect(430, 40, 51, 24))
        self.comboBox_GroupID.setObjectName("comboBox_GroupID")
        self.comboBox_isSuperUser = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_isSuperUser.setGeometry(QtCore.QRect(100, 40, 71, 24))
        self.comboBox_isSuperUser.setCurrentText("")
        self.comboBox_isSuperUser.setObjectName("comboBox_isSuperUser")
        self.comboBox_resetCreateRequestLimit = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_resetCreateRequestLimit.setGeometry(QtCore.QRect(260, 40, 81, 24))
        self.comboBox_resetCreateRequestLimit.setCurrentText("")
        self.comboBox_resetCreateRequestLimit.setObjectName("comboBox_resetCreateRequestLimit")
        self.lineEdit_userApproveNeededLimit_Update = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_userApproveNeededLimit_Update.setGeometry(QtCore.QRect(350, 40, 71, 24))
        self.lineEdit_userApproveNeededLimit_Update.setAutoFillBackground(False)
        self.lineEdit_userApproveNeededLimit_Update.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#FFF;\n"
"border:1px solid #DDD;")
        self.lineEdit_userApproveNeededLimit_Update.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_userApproveNeededLimit_Update.setReadOnly(False)
        self.lineEdit_userApproveNeededLimit_Update.setPlaceholderText("")
        self.lineEdit_userApproveNeededLimit_Update.setClearButtonEnabled(False)
        self.lineEdit_userApproveNeededLimit_Update.setObjectName("lineEdit_userApproveNeededLimit_Update")
        self.comboBox_PayConditions = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_PayConditions.setGeometry(QtCore.QRect(490, 40, 91, 24))
        self.comboBox_PayConditions.setObjectName("comboBox_PayConditions")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 591, 173))
        self.page_3.setObjectName("page_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 591, 161))
        self.tableWidget.setMinimumSize(QtCore.QSize(571, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("font-size:11px;\n"
"\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 591, 173))
        self.page_4.setObjectName("page_4")
        self.tableWidget2 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget2.setGeometry(QtCore.QRect(0, 0, 591, 161))
        self.tableWidget2.setMinimumSize(QtCore.QSize(571, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tableWidget2.setFont(font)
        self.tableWidget2.setStyleSheet("font-size:11px;\n"
"\n"
"")
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(5)
        self.tableWidget2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(4, item)
        self.toolBox.addItem(self.page_4, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 16))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 150, 81, 16))
        self.label_5.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3_ShortUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3_ShortUserName.setGeometry(QtCore.QRect(20, 170, 161, 24))
        self.lineEdit_3_ShortUserName.setAutoFillBackground(False)
        self.lineEdit_3_ShortUserName.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"")
        self.lineEdit_3_ShortUserName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_3_ShortUserName.setReadOnly(True)
        self.lineEdit_3_ShortUserName.setPlaceholderText("")
        self.lineEdit_3_ShortUserName.setClearButtonEnabled(False)
        self.lineEdit_3_ShortUserName.setObjectName("lineEdit_3_ShortUserName")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 171, 16))
        self.label_4.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 171, 16))
        self.label_3.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5_Department = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5_Department.setGeometry(QtCore.QRect(300, 170, 171, 24))
        self.lineEdit_5_Department.setAutoFillBackground(False)
        self.lineEdit_5_Department.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"")
        self.lineEdit_5_Department.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_5_Department.setReadOnly(True)
        self.lineEdit_5_Department.setPlaceholderText("")
        self.lineEdit_5_Department.setClearButtonEnabled(False)
        self.lineEdit_5_Department.setObjectName("lineEdit_5_Department")
        self.lineEdit_2_UserLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_UserLogin.setGeometry(QtCore.QRect(20, 120, 161, 24))
        self.lineEdit_2_UserLogin.setAutoFillBackground(False)
        self.lineEdit_2_UserLogin.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"")
        self.lineEdit_2_UserLogin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2_UserLogin.setReadOnly(True)
        self.lineEdit_2_UserLogin.setPlaceholderText("")
        self.lineEdit_2_UserLogin.setClearButtonEnabled(False)
        self.lineEdit_2_UserLogin.setObjectName("lineEdit_2_UserLogin")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 150, 71, 16))
        self.label_7.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7_BusinessName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7_BusinessName.setGeometry(QtCore.QRect(190, 170, 101, 24))
        self.lineEdit_7_BusinessName.setAutoFillBackground(False)
        self.lineEdit_7_BusinessName.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;")
        self.lineEdit_7_BusinessName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_7_BusinessName.setReadOnly(True)
        self.lineEdit_7_BusinessName.setPlaceholderText("")
        self.lineEdit_7_BusinessName.setClearButtonEnabled(False)
        self.lineEdit_7_BusinessName.setObjectName("lineEdit_7_BusinessName")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 100, 171, 16))
        self.label_6.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6_Position = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6_Position.setGeometry(QtCore.QRect(390, 120, 220, 24))
        self.lineEdit_6_Position.setAutoFillBackground(False)
        self.lineEdit_6_Position.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"")
        self.lineEdit_6_Position.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6_Position.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6_Position.setReadOnly(True)
        self.lineEdit_6_Position.setPlaceholderText("")
        self.lineEdit_6_Position.setClearButtonEnabled(False)
        self.lineEdit_6_Position.setObjectName("lineEdit_6_Position")
        self.lineEdit_4_UserFulName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4_UserFulName.setGeometry(QtCore.QRect(190, 120, 191, 24))
        self.lineEdit_4_UserFulName.setAutoFillBackground(False)
        self.lineEdit_4_UserFulName.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"")
        self.lineEdit_4_UserFulName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4_UserFulName.setReadOnly(True)
        self.lineEdit_4_UserFulName.setPlaceholderText("")
        self.lineEdit_4_UserFulName.setClearButtonEnabled(False)
        self.lineEdit_4_UserFulName.setObjectName("lineEdit_4_UserFulName")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 150, 121, 16))
        self.label_12.setStyleSheet("font-weight: bold;\n"
"font-size:11px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.lineEdit_8_isActiveUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8_isActiveUser.setGeometry(QtCore.QRect(480, 170, 131, 24))
        self.lineEdit_8_isActiveUser.setAutoFillBackground(False)
        self.lineEdit_8_isActiveUser.setStyleSheet("padding-left:5px;\n"
"font-size:11px;\n"
"background-color:#DDDDDD;\n"
"border:none;\n"
"color:red;\n"
"")
        self.lineEdit_8_isActiveUser.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_8_isActiveUser.setReadOnly(True)
        self.lineEdit_8_isActiveUser.setPlaceholderText("")
        self.lineEdit_8_isActiveUser.setClearButtonEnabled(False)
        self.lineEdit_8_isActiveUser.setObjectName("lineEdit_8_isActiveUser")
        self.button_run_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_run_task.setGeometry(QtCore.QRect(510, 520, 111, 31))
        self.button_run_task.setStyleSheet("background-color:rgb(85, 170, 0);\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.button_run_task.setObjectName("button_run_task")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 530, 201, 16))
        self.label_14.setObjectName("label_14")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, -4, 631, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background:#f1f1f1;")
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_4_UserFulName.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_6_Position.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_2_UserLogin.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_3_ShortUserName.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_7_BusinessName.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_5_Department.clear)
        self.button_get_user_info_clear.clicked.connect(self.lineEdit_8_isActiveUser.clear)
        self.button_get_user_info_clear_2.clicked.connect(self.lineEdit_8.clear)
        self.button_get_user_info_clear_2.clicked.connect(self.lineEdit_9.clear)
        self.button_get_user_info.clicked.connect(self.comboBox_isSuperUser.clear)
        self.button_get_user_info.clicked.connect(self.comboBox_GroupID.clear)
        self.button_get_user_info.clicked.connect(self.comboBox_resetCreateRequestLimit.clear)
        self.button_get_user_info.clicked.connect(self.lineEdit_userApproveNeededLimit_Update.clear)
        self.button_get_user_info.clicked.connect(self.comboBox_PayConditions.clear)
        self.button_get_user_info.clicked.connect(self.lineEdit_userCreateRequestLimit_Update.clear)
        self.button_get_user_info.clicked.connect(self.comboBox_AccessType.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Payments Control Administrator "))
        self.groupBox_1_tab.setTitle(_translate("MainWindow", "Выбор пользователя"))
        self.label.setText(_translate("MainWindow", "Поиск"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Начните вводить фамилию"))
        self.button_get_user_info.setText(_translate("MainWindow", "Выбрать"))
        self.button_get_user_info_clear.setText(_translate("MainWindow", "Очистить"))
        self.groupBox.setTitle(_translate("MainWindow", "Выбор операции"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Опциональные параметры"))
        self.button_get_copy_active_user_info.setText(_translate("MainWindow", "Выбрать"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Начните вводить фамилию"))
        self.label_8.setText(_translate("MainWindow", "Права чьи скопировать"))
        self.label_9.setText(_translate("MainWindow", "Регионы"))
        self.label_10.setText(_translate("MainWindow", "Офисы"))
        self.label_11.setText(_translate("MainWindow", "Группа"))
        self.label_13.setText(_translate("MainWindow", "ID"))
        self.button_get_user_info_clear_2.setText(_translate("MainWindow", "Отменить"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Тип доступа"))
        self.radioButton_access.setText(_translate("MainWindow", "Создание"))
        self.radioButton_access_2.setText(_translate("MainWindow", "Утверждение"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Добавить пользователя"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Текущие значения"))
        self.label_15.setText(_translate("MainWindow", "Тип доступа"))
        self.label_16.setText(_translate("MainWindow", "Суперюзер"))
        self.label_17.setText(_translate("MainWindow", "Лимит, грн"))
        self.label_18.setText(_translate("MainWindow", "Сброс лимита"))
        self.label_19.setText(_translate("MainWindow", "Мин.сумма"))
        self.label_20.setText(_translate("MainWindow", "Группа"))
        self.label_21.setText(_translate("MainWindow", "Условия оплаты"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Изменяемые значения"))
        self.label_29.setText(_translate("MainWindow", "Тип доступа"))
        self.label_30.setText(_translate("MainWindow", "Суперюзер"))
        self.label_31.setText(_translate("MainWindow", "Лимит, грн"))
        self.label_32.setText(_translate("MainWindow", "Сброс лимита"))
        self.label_33.setText(_translate("MainWindow", "Мин.сумма"))
        self.label_34.setText(_translate("MainWindow", "Группа"))
        self.label_35.setText(_translate("MainWindow", "Условия оплаты"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Изменение данных пользователя"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Права"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Офис"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Название МВЗ"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UserObjectID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Добавление прав на МВЗ"))
        self.tableWidget2.setSortingEnabled(True)
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Права"))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Офис"))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Название МВЗ"))
        item = self.tableWidget2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UserObjectID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Удаление прав на МВЗ"))
        self.label_2.setText(_translate("MainWindow", "Логин"))
        self.label_5.setText(_translate("MainWindow", "Отдел"))
        self.label_4.setText(_translate("MainWindow", "Полное имя"))
        self.label_3.setText(_translate("MainWindow", "Краткое имя"))
        self.label_7.setText(_translate("MainWindow", "Бизнес"))
        self.label_6.setText(_translate("MainWindow", "Должность"))
        self.label_12.setText(_translate("MainWindow", "Наличие доступа"))
        self.button_run_task.setText(_translate("MainWindow", "Выполнить"))
        self.label_14.setText(_translate("MainWindow", "Версия 0.7"))
        self.menu.setTitle(_translate("MainWindow", "Инструкция"))
        self.action.setText(_translate("MainWindow", "Открыть файл"))
from check_combobox import CheckComboBox
