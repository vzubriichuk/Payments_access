#!/usr/bin/env python
# coding:utf-8
"""
Author : Vitaliy Zubriichuk
Contact : v@zubr.kiev.ua
Time    : 12.03.2020 20:01
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from db_conn import DBConnect
from gui.mainWindow import Ui_MainWindow
from pyodbc import Error as SQLError
from log_error import writelog
from singleinstance import Singleinstance
import sys
import os


server = 's-kv-center-s59'
db = 'LogisticFinance'


class Error(Exception):
    """ Exception raised if error has detected.
    Attributes:
        expression - input expression in which the error occurred;
    """

    def __init__(self, expression):
        self.expression = expression
        super().__init__(self.expression)


def _get_users():
    with DBConnect(server, db) as sql:
        return sql.get_users()


def _get_active_users():
    with DBConnect(server, db) as sql:
        return sql.get_active_users()


def _get_active_users_all():
    with DBConnect(server, db) as sql:
        return sql.get_active_users_all()


def _get_regions():
    with DBConnect(server, db) as sql:
        return sql.get_regions()


def _get_offices():
    with DBConnect(server, db) as sql:
        return sql.get_offices()


def _get_people_group_id():
    with DBConnect(server, db) as sql:
        return sql.get_people_group_id()


class PopupInfoWindows(QWidget):
    def __init__(self):
        super().__init__()

    def popup_add_user_succesfull(self):
        QMessageBox.information(self, 'Добавление пользователя',
                                'Пользователь успешно добавлен',
                                QMessageBox.Ok, QMessageBox.Ok)

    def popup_add_user_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Пользователь с таким @UserLogin уже существует',
                             QMessageBox.Ok, QMessageBox.Ok)


    def popup_change_user_info_succesfull(self):
        QMessageBox.information(self, 'Изменение данных пользователя',
                                'Изменения пользователю успешно применены.',
                                QMessageBox.Ok, QMessageBox.Ok)

    def popup_add_mvz_succesfull(self):
        QMessageBox.information(self, 'Добавление МВЗ',
                                'Выбранные МВЗ были успешно добавлены.',
                                QMessageBox.Ok, QMessageBox.Ok)

    def popup_add_mvz_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Не было выбрано ни одного нового '
                             'МВЗ для добавления.',
                             QMessageBox.Ok, QMessageBox.Ok)

    def popup_remove_mvz_from_user(self):
        QMessageBox.information(self, 'Удаление МВЗ',
                                'Выбранные МВЗ были успешно удалены.',
                                QMessageBox.Ok, QMessageBox.Ok)

    def popup_remove_mvz_from_user_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Не было выбрано ни одного нового '
                             'МВЗ для удаления.',
                             QMessageBox.Ok, QMessageBox.Ok)

LastStateRole = QtCore.Qt.UserRole

class PaymentAdminApp(QtWidgets.QMainWindow, Ui_MainWindow, PopupInfoWindows):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('resources/admin.png'))
        # Global list of users
        users = dict(_get_users())

        #############################
        # global values
        #############################

        active_users = dict(_get_active_users())
        regions = dict(_get_regions())
        offices = dict(_get_offices())
        group_id = dict(_get_people_group_id())
        self.page1_list_regions = []
        self.page1_list_offices = []
        self.AccessRights = "Создание"
        self.ActiveUserID = 0

        # Add autocomplete for total list users
        completer = QCompleter(users.values())
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)
        self.lineEdit.textChanged.connect(self.on_text_changed)

        # ----------------------------
        # toolBox page_0 forms
        # ----------------------------

        # Add autocomplete for active list users
        completer = QCompleter(active_users.values())
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit_8.setCompleter(completer)
        self.lineEdit_8.textChanged.connect(self.on_text_changed_p1)

        # Buttons disabled while lineEdit is empty
        self.button_get_user_info.setEnabled(False)
        self.button_get_user_info.clicked.connect(self._get_user_info)
        self.button_get_copy_active_user_info.setEnabled(False)
        self.button_get_copy_active_user_info.clicked.connect(
            self._get_copy_active_user_info)

        # Add regions to combobox with checkable items
        self.comboBox_regions.setPlaceholderText("Выбрать")
        self.model_regions = self.comboBox_regions.model()
        self.regions_count = 0
        for key, values in regions.items():
            self.comboBox_regions.addItem(values)
            self.model_regions.item(self.regions_count).setCheckable(True)
            self.regions_count += 1

        # Add offices to combobox with checkable items
        self.comboBox_offices.setPlaceholderText("Выбрать")
        self.model_offices = self.comboBox_offices.model()
        self.offices_count = 0
        for key, values in offices.items():
            self.comboBox_offices.addItem(values)
            self.model_offices.item(self.offices_count).setCheckable(True)
            self.offices_count += 1

        for key, values in group_id.items():
            self.comboBox_user_group.addItem(str(values))

        self.button_get_user_info_clear_2.clicked.connect(self.input_enable)

        # main run button
        self.button_run_task.clicked.connect(self._run_buttons_task)

    # ----------------------------
    # toolBox page_0 actions
    # ----------------------------

    # get all info from forms
    def get_output_info(self):
        self.page1_list_regions = []
        for i in range(self.regions_count):
            selected_item = self.model_regions.item(i).checkState()
            if selected_item == 2:
                self.page1_list_regions.append(
                    self.comboBox_regions.itemText(i))
        self.page1_list_offices = []
        for i in range(self.offices_count):
            selected_item = self.model_offices.item(i).checkState()
            if selected_item == 2:
                self.page1_list_offices.append(
                    self.comboBox_offices.itemText(i))
        if self.radioButton_access.isChecked():
            self.AccessRights = "Создание"
        elif self.radioButton_access_2.isChecked():
            self.AccessRights = "Утверждение"

    # disable elements for header form
    def on_text_changed(self):
        self.button_get_user_info.setEnabled(bool(self.lineEdit.text()))

    # disable elements for page 1
    def on_text_changed_p1(self):
        self.button_get_copy_active_user_info.setEnabled(
            bool(self.lineEdit_8.text()))
        self.comboBox_regions.setEnabled(False)
        self.comboBox_offices.setEnabled(False)

    def input_enable(self):
        self.comboBox_regions.setEnabled(True)
        self.comboBox_offices.setEnabled(True)

    # def get_output_info_print(self):
    #     print(self.AccessRights)
    #     print(self.page1_list_regions)
    #     print(self.page1_list_offices)
    #     print(self.comboBox_user_group.currentText())


    def _get_user_info(self):
        UserFullName = self.lineEdit.text()
        with DBConnect(server, db) as sql:
            UserInfo = sql.get_user_info(UserFullName)
            self.lineEdit_2_UserLogin.setText(UserInfo[0])
            self.lineEdit_3_ShortUserName.setText(UserInfo[1])
            self.lineEdit_4_UserFulName.setText(UserInfo[2])
            self.lineEdit_5_Department.setText(UserInfo[3])
            self.lineEdit_6_Position.setText(UserInfo[4])
            self.lineEdit_7_BusinessName.setText(UserInfo[5])
            self.lineEdit_8_isActiveUser.setText(UserInfo[7])
            if UserInfo[7] == 'Да':
                self.ActiveUserID = UserInfo[6]
                self.change_active_user_info()  # get info for change page
                self._admin_get_user_objects()  # get info for user roles
                self._admin_get_user_objects_del()  # get info for user roles


    def _get_copy_active_user_info(self):
        UserFullName = self.lineEdit_8.text()
        with DBConnect(server, db) as sql:
            try:
                UserInfo2 = sql.get_user_info(UserFullName)
                self.lineEdit_9.setText(str(UserInfo2[6]))
            except Exception as error:
                writelog(error)

    # final execute query
    def _add_user(self):
        UserLogin = self.lineEdit_2_UserLogin.text()
        UserName = self.lineEdit_4_UserFulName.text()
        ShortUserName = self.lineEdit_3_ShortUserName.text()
        AccessRights = self.AccessRights
        CopyUserRights = self.lineEdit_9.text() or None
        ServiceName = ', '.join(self.page1_list_offices)
        Region = ', '.join(self.page1_list_regions)
        group_id = None
        if self.comboBox_user_group.currentText() == 'None':
            group_id == None
        else:
            self.comboBox_user_group.currentText()
        GroupID = group_id

        elements = (UserLogin, UserName, ShortUserName, AccessRights,
                    CopyUserRights, ServiceName, Region, GroupID)
        try:
            # print(elements)
            with DBConnect(server, db) as sql:
                sql.add_user(UserLogin, UserName, ShortUserName, AccessRights,
                             CopyUserRights, ServiceName, Region, GroupID)
            self.popup_add_user_succesfull()
        except SQLError as error:
            writelog(error)
            for i in error.args[1].split():
                if i == '(221902)':
                    self.popup_add_user_error()

    # ----------------------------
    # toolBox page_1 actions
    # ----------------------------
    def change_active_user_info(self):
        with DBConnect(server, db) as sql:
            UserCurrentInfo = sql.get_active_user_info(self.ActiveUserID)
            # print(UserCurrentInfo)
            if UserCurrentInfo[0] == 0:
                self.lineEdit_AccessType.setText('Нет доступа')
            elif UserCurrentInfo[0] == 1:
                self.lineEdit_AccessType.setText('Создание')
            elif UserCurrentInfo[0] == 2:
                self.lineEdit_AccessType.setText('Утверждение')
            else:
                self.lineEdit_AccessType.setText('Архивный статус')

            if UserCurrentInfo[1] == 0:
                self.lineEdit_isSuperUser.setText('Нет')
            else:
                self.lineEdit_isSuperUser.setText('Да')
            self.lineEdit_userCreateRequestLimit.setText(
                str(UserCurrentInfo[2]))
            self.lineEdit_userCreateRequestLimit_Update.setText(
                str(UserCurrentInfo[2]))

            if UserCurrentInfo[3] == 0:
                self.lineEdit_resetCreateRequestLimit.setText('Нет')
            else:
                self.lineEdit_resetCreateRequestLimit.setText('Да')
            self.lineEdit_userApproveNeededLimit.setText(
                str(UserCurrentInfo[4]))
            self.lineEdit_userApproveNeededLimit_Update.setText(
                str(UserCurrentInfo[4]))
            self.lineEdit_GroupID.setText(str(UserCurrentInfo[5]))
            self.lineEdit_PayConditions.setText(str(UserCurrentInfo[6]))

        # add elements in change active user's form
        group_id = dict(_get_people_group_id())
        self.comboBox_AccessType.addItem('Выбрать')
        self.comboBox_AccessType.addItem('Создание')
        self.comboBox_AccessType.addItem('Утверждение')
        self.comboBox_isSuperUser.addItem('Выбрать')
        self.comboBox_isSuperUser.addItem('Нет')
        self.comboBox_isSuperUser.addItem('Да')
        self.comboBox_resetCreateRequestLimit.addItem('Выбрать')
        self.comboBox_resetCreateRequestLimit.addItem('Нет')
        self.comboBox_resetCreateRequestLimit.addItem('Да')
        for key, values in group_id.items():
            self.comboBox_GroupID.addItem(str(values))
        self.comboBox_PayConditions.addItem('Выбрать')


    def change_active_user(self):
        UserID = self.ActiveUserID

        if self.comboBox_AccessType.currentText() == 'Создание':
            AccessType = 1
        elif self.comboBox_AccessType.currentText() == 'Утверждение':
            AccessType = 2
        else:
            AccessType = None
        if self.comboBox_isSuperUser.currentText() == 'Нет':
            isSuperUser = 0
        elif self.comboBox_isSuperUser.currentText() == 'Да':
            isSuperUser = 1
        else:
            isSuperUser = None
        userCreateRequestLimit_Update = self.lineEdit_userCreateRequestLimit_Update.text()
        if self.comboBox_resetCreateRequestLimit.currentText() == 'Нет':
            resetCreateRequestLimit = 0
        elif self.comboBox_resetCreateRequestLimit.currentText() == 'Да':
            resetCreateRequestLimit = 1
        else:
            resetCreateRequestLimit = None
        userApproveNeededLimit_Update = self.lineEdit_userApproveNeededLimit_Update.text()
        if self.comboBox_GroupID.currentText() == 'None':
            GroupID = None
        else:
            GroupID = self.comboBox_GroupID.currentText()
        PayConditionsID = None  # временно self.comboBox_PayConditions
        with DBConnect(server, db) as sql:
            sql.admin_change_active_user_info(UserID, AccessType,
                                              isSuperUser,
                                              userCreateRequestLimit_Update,
                                              resetCreateRequestLimit,
                                              userApproveNeededLimit_Update,
                                              GroupID, PayConditionsID)

    # ----------------------------
    # toolBox page_2 actions (add MVZ to user)
    # ----------------------------
    def _admin_get_user_objects(self):
        self.tableWidget.removeRow(0)
        # get all values of user roles
        with DBConnect(server, db) as sql:
            allRows = sql.admin_get_user_objects(self.ActiveUserID)
        self.countRows = len(allRows)

        # create basic table
        self.tableWidget.setRowCount(self.countRows)
        for row in range(self.countRows):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)
            item.setData(LastStateRole, item.checkState())
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 40)
            self.tableWidget.setColumnWidth(3, 260)

            self.tableWidget.setItem(row, 0, item)

            # insert values into table
            # print(allRows)
            rows = 0
            for tup in allRows:
                col = 1
                for i in tup:
                    cell = QTableWidgetItem(str(i))
                    self.tableWidget.setItem(rows, col, cell)
                    self.tableWidget.setRowHeight(rows, 10)
                    cell_align = self.tableWidget.item(rows, 1)
                    cell_align.setTextAlignment(QtCore.Qt.AlignCenter)
                    col += 1
                rows += 1

            # check or uncheck for every row of user roles
            for i in range(self.countRows):
                if self.tableWidget.item(i,1).text() != self.tableWidget.item(i,4).text():
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(i, 0, chkBoxItem)
                else:
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    self.tableWidget.setItem(i, 0, chkBoxItem)

    # check every checkboxes for change of user roles
    def check_rows_checkboxes(self):
        ObjectID = []
        for i in range(self.countRows):
            checkboxItem = self.tableWidget.item(i, 0)
            currentState = checkboxItem.checkState()
            if currentState == QtCore.Qt.Checked:
                # add mvz in list only if user not have it
                if self.tableWidget.item(i, 1).text() != self.tableWidget.item(i, 4).text():
                    ObjectID.append(self.tableWidget.item(i, 1).text())
        ListObjectID = ', '.join(ObjectID)
        print(ObjectID)
        try:
            with DBConnect(server, db) as sql:
                sql.add_mvz_to_user(self.ActiveUserID, ListObjectID)
            self.popup_add_mvz_succesfull()
        except SQLError as error:
            writelog(error)
            for i in error.args[0].split():
                if i == 'HY000':
                    self.popup_add_mvz_error()

    # ----------------------------
    # toolBox page_3 actions (remove MVZ from user)
    # ----------------------------
    def _admin_get_user_objects_del(self):
        self.tableWidget2.removeRow(0)
        # get all values of user roles
        with DBConnect(server, db) as sql:
            allRows = sql.admin_get_user_objects(self.ActiveUserID)
        self.countRows = len(allRows)

        # create basic table
        self.tableWidget2.setRowCount(self.countRows)
        for row in range(self.countRows):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)
            item.setData(LastStateRole, item.checkState())
            self.tableWidget2.setColumnWidth(0, 50)
            self.tableWidget2.setColumnWidth(1, 40)
            self.tableWidget2.setColumnWidth(3, 260)

            self.tableWidget2.setItem(row, 0, item)

            # insert values into table from allRows
            rows = 0
            for tup in allRows:
                col = 1
                for i in tup:
                    cell = QTableWidgetItem(str(i))
                    self.tableWidget2.setItem(rows, col, cell)
                    self.tableWidget2.setRowHeight(rows, 10)
                    cell_align = self.tableWidget2.item(rows, 1)
                    cell_align.setTextAlignment(QtCore.Qt.AlignCenter)
                    col += 1
                rows += 1

            # check or uncheck for every row of user roles
            for i in range(self.countRows):
                if self.tableWidget2.item(i, 1).text() != self.tableWidget2.item(
                        i, 4).text():
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget2.setItem(i, 0, chkBoxItem)
                else:
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    self.tableWidget2.setItem(i, 0, chkBoxItem)

    # check every checkboxes for change of user roles
    def check_rows_checkboxes_del(self):
        ObjectID = []
        for i in range(self.countRows):
            checkboxItem = self.tableWidget2.item(i, 0)
            currentState = checkboxItem.checkState()
            if currentState == QtCore.Qt.Unchecked:
                # add mvz in list only if user not have it
                if self.tableWidget2.item(i, 1).text() == self.tableWidget2.item(
                        i, 4).text():
                    ObjectID.append(self.tableWidget2.item(i, 1).text())
        ListObjectID = ', '.join(ObjectID)
        print(str(ListObjectID))
        try:
            with DBConnect(server, db) as sql:
                sql.remove_mvz_from_user(self.ActiveUserID, ListObjectID)
            self.popup_remove_mvz_from_user()
        except SQLError as error:
            writelog(error)
            for i in error.args[0].split():
                if i == '42000':
                    self.popup_remove_mvz_from_user_error()

    # runs buttons for every task
    def _run_buttons_task(self):
        if self.toolBox.currentIndex() == 0:
            self.get_output_info()
            self._add_user()
        elif self.toolBox.currentIndex() == 1:
            self.change_active_user()
            self.popup_change_user_info_succesfull()
        elif self.toolBox.currentIndex() == 2:
            self.check_rows_checkboxes()
        elif self.toolBox.currentIndex() == 3:
            self.check_rows_checkboxes_del()
        else:
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = PaymentAdminApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    try:
        fname = os.path.basename(__file__)
        myapp = Singleinstance(fname)
        if myapp.alreadyrunning():
            sys.exit()
        main()
    except Exception as e:
        writelog(e)
    finally:
        sys.exit()
