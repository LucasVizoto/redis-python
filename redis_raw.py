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
forma_certa = redis_conn.get("minha_chave").decode("utf-8")

#para deleções, basta usar o método delete

redis_conn.delete("minha_chave")
print(redis_conn.get("minha_chave"))


#-------------------------------------------
#           COMANDOS PARA HASH
#-------------------------------------------

meu_hash = { # chave de exemplo
    "nome": "valor", #fields e values
    "idade": "30",
    "cidade": "São Paulo"
}

redis_conn.hset("meu_hash","nome", "valor")
redis_conn.hset("meu_hash", mapping=meu_hash)
# o mapping é para inserir vários valores de uma vez

valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")
print(valor_1)
# o hget é para buscar valores de um hash

redis_conn.hdel("meu_hash", "cidade")
# o hdel é para deletar valores de um hash

#-------------------------------------------
#           BUSCAS POR EXISTÊNCIA
#-------------------------------------------

# Verifico se meu elemento existe de fato
existe = redis_conn.exists("minha_chave") # verificando se existe a chave
print(existe)  # Retorna 1 se existir, 0 se não existir

# Verifico se meu elemento existe dentro do meu hash

existe_hash = redis_conn.hexists("meu_hash", "nome")  # verificando se existe o campo "nome" no hash
print(existe_hash)  # Retorna 1 se existir, 0 se não existir


'''
#-------------------------------------------
#           BUSCAS POR KEYS
#-------------------------------------------

dados -> TTL (Time To Live) é o tempo de vida de uma chave no Redis.
O TTL é o tempo que a chave ficará disponível antes de ser removida automaticamente.
tempo de exisÊncia em segundos, o próprio banco deleta o dado após esse tempo sem qeu façamos o delete

ou seja, o próprio banco pode gerenciar sua própria memória fazendo com que seja possível apagar os dados
já que o Redis armazena da  RAM

TTL com valor negativo significa que a chave não expira, ou seja, não tem tempo de vida definido.
'''

redis_conn.set("chave_del", "esse valor será deletado em 10 segundos", 10)
redis_conn.expire("meu_hash", 12)  # Define o tempo de expiração da chave em 12 segundos para um elemento já existente

