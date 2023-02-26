import sqlite3
from sqlite3 import Error

import os

class Database_Wrapper():

    def __init__(self) -> None:
        self.conn = None

    def __create_table(self, conn, create_table_sql):
            """ create a table from the create_table_sql statement
            :param conn: Connection object
            :param create_table_sql: a CREATE TABLE statement
            :return:
            """
            try:
                c = conn.cursor()
                c.execute(create_table_sql)
            except Error as e:
                print(e)

    def __create_connection(self, db_file):
            """ create a database connection to the SQLite database
                specified by db_file
            :param db_file: database file
            :return: Connection object or None
            """
            conn = None
            try:
                conn = sqlite3.connect(db_file)
                return conn
            except Error as e:
                print(e)

            return conn

    def create_table_if_not_exists(self, table_name: str = "test") -> bool:

        working_directory_path = os.path.abspath(os.getcwd())

        db_path = working_directory_path + f"\source\pyqt\db\{table_name}.db"
        print(db_path)

        sql_create_data_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            timestamp text NOT NULL,
                                            front_left_compression INTEGER,
                                            front_right_compression INTEGER,
                                            back_left_compression INTEGER,
                                            back_right_compression INTEGER,
                                            steering_angle INTEGER,
                                            front_left_rpm REAL,
                                            front_right_rpm REAL,
                                            rear_rpm REAL,
                                            gps_latitude INTEGER,
                                            gps_longtitude INTEGER,
                                            gps_lat_sigfigs INTEGER,
                                            gps_long_sigfigs INTEGER
                                        ); """


        
        # create a database connection
        conn = self.__create_connection(db_path)

        
        # create tables
        if conn is not None:
            # create projects table
            self.__create_table(conn, sql_create_data_table)

        else:
            print("Error! cannot create the database connection.")
        
        
            
        
