import redis


class Urls():

    def __init__(self):
        self.connection = redis.StrictRedis(host='localhost', port=6379, db=0)

    def fetch(self, code):
        return self.connection.get(code)

    def create(self, code, url):
        return self.connection.set(code, url)
