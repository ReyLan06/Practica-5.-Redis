import redis
import time

redis_host = 'redis-16873.c232.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 16873  
redis_password = 'LBR12PVpAMsKNh5mH9VBUpW3anK8XIaO'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
