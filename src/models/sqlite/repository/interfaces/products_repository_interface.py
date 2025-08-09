from abc import ABC, abstractmethod

class ProductsRepositoryInterface(ABC):
    @abstractmethod
    def find_product_by_name(self, name: str) -> tuple:
        pass

    @abstractmethod
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        pass