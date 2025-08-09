from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = products_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params['product_name']
        product = None
        product = self.__find_in_redis(product_name)

        if not product:
            product = self.__find_in_sqlite(product_name)
            self.__insert_in_cache(product)

        formated_response = self.__format_response(product)
        return formated_response


    def __find_in_redis(self, product_name: str) -> tuple:
        product = self.__redis_repo.get_key(product_name)
        if product:
            # redis retorna  "chave": price, quantity
            # e o sqlite retorna (id, "chave", price, quantity), sendo assim, precisamos padronizar
            product_list = product.split(',') # price, quantity -> [price, quantity]
            return (0, product_name, product_list[0], product_list[1])
        return None
    
    def __find_in_sqlite(self, product_name: str) -> tuple:
        product = self.__sqlite_repo.find_product_by_name(product_name)
        if not product:
            raise Exception('Product not found')
        return product
    
    def __insert_in_cache(self, product:tuple) -> None:
        product_name = product[1]
        value = f"{product[2]},{product[3]}"
        self.__redis_repo.insert_with_ttl(product_name, value, ttl=60)

    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "Product",
                "count": 1,
                "attributes": {
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3]
                }
            },
            status_code = 200
        )