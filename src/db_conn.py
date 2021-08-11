#!/usr/bin/env python
# coding:utf-8
"""
Author : Vitaliy Zubriichuk
Contact : v@zubr.kiev.ua
Time    : 12.03.2020 20:26
"""
import pyodbc
from pyodbc import Error as SQLError
from log_error import writelog


class Error(Exception):
    """ Exception raised if error has detected.
    Attributes:
        expression - input expression in which the error occurred;
    """

    def __init__(self, expression):
        self.expression = expression
        super().__init__(self.expression)


class DBConnect:
    def __init__(self, server, db):
        self._server = server
        self._db = db

    def __enter__(self):
        # Connection properties
        conn_str = (
            'Driver={{SQL Server}};'
            'Server={0};'
            'Database={1};'
            'Trusted_Connection=yes;'.format(self._server, self._db)
        )
        self.__db = pyodbc.connect(conn_str)
        self.__db.autocommit = True
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, type, value, traceback):
        self.__db.close()

    def get_users(self):
        query = '''
		select [cub.People.peopleLogin], [cub.People.peopleFullName]
        from [DBMS_S31].[MasterData].[dbo].[dim_Staff] s
        where 1=1
        and [cub.Staff.isWork] = 1
        and [cub.Businesses.topLevelBusinessId] in ( 76,80,88,102,105,113,114,353,421  )
        and [cub.People.peopleLogin] is not NULL
        '''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_user_info(self, UserName):
        query = '''
        exec payment.admin_get_user_info @UserName = ?
        '''
        self.__cursor.execute(query, UserName)
        return self.__cursor.fetchone()

    def get_active_user_info(self, UserID):
        query = '''
        exec payment.admin_get__active_user_info @UserID = ?
        '''
        self.__cursor.execute(query, UserID)
        return self.__cursor.fetchone()

    def get_active_users(self):
        query = '''
        select UserID, UserName
        from payment.People
        '''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_regions(self):
        query = '''
           select distinct Region_LocalID, RegionName 
           from LogisticFinance.BTool.aid_CostObject_Detail
             '''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_offices(self):
        query = '''
        select ROW_NUMBER () over (order by ServiceName ) as ID , ServiceName 
        from ( select distinct ServiceName from payment.ListObjects ) l
             '''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def get_people_group_id(self):
        query = '''
        select ROW_NUMBER () over (order by GroupID ) as ID , GroupID 
        from ( select distinct GroupID from payment.People ) p
        '''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def add_user(self, UserLogin, UserName, ShortUserName, AccessRights,
                 CopyUserRights, ServiceName, Region, GroupID):
        query = '''
        exec payment.add_user @UserLogin = ?,
                              @UserName = ?,
                              @ShortUserName = ?,
                              @AccessRights = ?,
                              @CopyUserRights = ?, 
                              @ServiceName = ?,
                              @Region = ?,
                              @GroupID = ?
        '''
        self.__cursor.execute(query, UserLogin, UserName, ShortUserName,
                              AccessRights, CopyUserRights, ServiceName,
                              Region, GroupID)
        try:
            return self.__cursor.fetchone()
        except:
            self.__db.commit()

    def admin_change_active_user_info(self, UserID, AccessType, isSuperUser,
                                      userCreateRequestLimit_Update,
                                      resetCreateRequestLimit,
                                      userApproveNeededLimit_Update, GroupID,
                                      PayConditionsID):
        query = '''
        exec payment.admin_change_active_user_info 
                              @UserID = ?,
                              @AccessType = ?,
                              @isSuperUser = ?,
                              @userCreateRequestLimit_Update = ?,
                              @resetCreateRequestLimit = ?,
                              @userApproveNeededLimit_Update = ?, 
                              @GroupID = ?,
                              @PayConditionsID = ?
        '''
        self.__cursor.execute(query, UserID, AccessType, isSuperUser,
                              userCreateRequestLimit_Update,
                              resetCreateRequestLimit,
                              userApproveNeededLimit_Update, GroupID,
                              PayConditionsID)
        self.__db.commit()

    def admin_get_user_objects(self, UserID):
        query = '''
        exec payment.admin_get_user_objects @UserID = ?
        '''
        self.__cursor.execute(query, UserID)
        return self.__cursor.fetchall()

    def add_mvz_to_user(self, UserID, ObjectID):
        query = '''
        exec payment.add_mvz_to_user @UserID = ?, @ObjectID = ?
        '''
        try:
            self.__cursor.execute(query, UserID, ObjectID)
        except SQLError as error:
            writelog(error)
        self.__db.commit()

    def remove_mvz_from_user(self, UserID, ObjectID):
        query = '''
        exec payment.remove_mvz_from_user @UserID = ?, @ObjectID = ?
        '''
        self.__cursor.execute(query, UserID, ObjectID)
        self.__db.commit()