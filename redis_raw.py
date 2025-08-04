from redis import Redis
from dotenv import load_dotenv
from os import getenv

load_dotenv()

redis_conn = Redis(
    host= getenv("DATABASE_HOST"), 
    port= getenv("DATABASE_PORT"), 
    db=0, 
    password= getenv("DATABASE_PASSWORD"), 
    username= getenv("DATABASE_USERNAME")
)

redis_conn.set("minha_chave", "valor")
redis_conn.set("minha_chave", "dando um update no meu valor")

# O set é para inserções e edição dos dados no banco

valor = redis_conn.get("minha_chave")
print(valor)
# a partir de uma chave eu consigo buscar um valor, porém ele vem
# em bytes, então é necessário decodificar
print(valor.decode("utf-8"))
# decodificando o valor, ele fica legível
# no caso de uma exibição normalemtne é feito da seguinte forma
forma_certa =redis_conn.get("minha_chave").decode("utf-8")
  


#para deleções, basta usar o método delete

redis_conn.delete("minha_chave")
print(redis_conn.get("minha_chave"))