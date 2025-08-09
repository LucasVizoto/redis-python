from sqlite3 import Connection, connect

class SQLiteConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None
    
    def connect(self) -> Connection:
        conn = connect(
            self.__connection_string,
            check_same_thread = False
            )
        self.__conn = conn
        return conn
    
    def get_connection(self) -> Connection:
        return self.__conn
    
sqlite_connection_handler = SQLiteConnectionHandler()