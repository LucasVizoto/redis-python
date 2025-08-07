from sqlite3 import Connection

class ProductsRepository:
    def __init__(self, conn: Connection):
        self.__conn = conn

    def find_product_by_name(self, name: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (name,)
        )
        product = cursor.fetchone()
        return product
    
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO products (name, price, quantity) 
            VALUES (?, ?, ?)
            ''',
            (name, price, quantity,)
        )
        self.__conn.commit()
        
