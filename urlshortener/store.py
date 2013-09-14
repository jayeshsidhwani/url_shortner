import redis
from config import REDIS_HOST, REDIS_PORT

class Urls():

    def __init__(self):
        self.connection = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def fetch(self, code):
        return self.connection.get(code)

    def create(self, code, url):
        return self.connection.set(code, url)
