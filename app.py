from flask import Flask
import redis

application = Flask(__name__)
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

NUMBERS_PER_REQUEST = 100000
POWER_FACTOR = 200

@application.route("/")
def load_server():

    for i in range(NUMBERS_PER_REQUEST):
        num = i ** POWER_FACTOR
        redis.lpush("list1", str(num))

    return str(redis.llen("list1"))

if __name__ == "__main__":
    application.run()
