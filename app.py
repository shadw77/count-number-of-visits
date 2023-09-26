from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
       redis.incr('visits')
       visits = redis.get('visits').decode('utf-8')
       return f'Number of visits: {visits}'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
