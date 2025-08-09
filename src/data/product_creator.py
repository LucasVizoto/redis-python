from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductCreator:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = products_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        name = body.get('name')
        price = body.get('price')
        quantity = body.get('quantity')

        self.__insert_produtct_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        formated_response = self.__format_response()
        return formated_response
    

    def __insert_produtct_in_sql(self,name: str, price:float, quantity: int) -> None:
        self.__sqlite_repo.insert_product(name, price, quantity)

    def __insert_in_cache(self,name: str, price:float, quantity: int) -> None:
        product_key = name
        value = f'{price},{quantity}'
        self.__redis_repo.insert_with_ttl(product_key, value, ttl=60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            data = {
                "type": "Product",
                "count": 1,
                "message": "Produto cadastrado com sucesso"
            },
            status_code = 201
        )