import sys

import sqlite3
from sqlite3 import Error


class SerialHandler:
    '''this class is responsible for 
    getting the data from serial
    formatting for database
    inserting into database
    '''
    def __init__(self) -> None:
        pass

    def connect_to_db(name: str = "Testing") -> bool:
        return False
    
   