from redis import Redis
from os import getenv

class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__redis_conn = None

    def connect(self) -> Redis:
        redis_conn = Redis(
            host= getenv("DATABASE_HOST"), 
            port= getenv("DATABASE_PORT"), 
            db=0, 
            password= getenv("DATABASE_PASSWORD"), 
            username= getenv("DATABASE_USERNAME")
        )
        self.__redis_conn = redis_conn
        return self.__redis_conn

    def get_connection(self) -> Redis:
        if self.__redis_conn is None:
            raise ValueError("Redis connection not established. Call connect() first.")
        return self.__redis_conn
    
redis_connection_handle = RedisConnectionHandler()