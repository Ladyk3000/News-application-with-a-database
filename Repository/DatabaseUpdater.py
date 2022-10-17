import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import datetime
from Repository.Configuration import Configuration
from settings import database_ini, database_section
from PySide6 import QtCore

class DataBaseUpdater(QtCore.QThread):
    signal_db_updater = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        configuration = Configuration()
        configuration.get_config(database_ini, database_section)
        self.params = configuration.params

    def init_table(self, table_name):
        connection = None
        try:
            connection = psycopg2.connect(**self.params)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS %s (STRESS INT NOT NULL,PATIENCE INT NOT NULL,DATE DATE NOT NULL);"%(table_name))
            #print("table created successfully")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                #print("Соединение с PostgreSQL закрыто")
    
    def update_data(self, stress_value: int, patience_value: int) -> None:
        self.signal_db_updater.emit(1)
        #print(stress_value, patience_value)
        connection = None
        try:
            connection = psycopg2.connect(**self.params)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO TELEMETRY (stress, patience, date) VALUES (%s, %s, %s)", (stress_value, patience_value, datetime.date.today()))
            print("data updated successfully")
            self.signal_db_updater.emit(0)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                #("Соединение с PostgreSQL закрыто")

    def connect_execute(self, request: str):
        connection = None
        try:
            connection = psycopg2.connect(**self.params)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute(request)
            cursor.close()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                # ("Соединение с PostgreSQL закрыто")