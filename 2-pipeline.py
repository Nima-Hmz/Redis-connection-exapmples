import redis

redis_client = redis.Redis()

# pipe lines to reduce the RTT(round-trim-time) or making atomic transactions without watch
pipeline = redis_client.pipeline(transaction=True)

pipeline.set('name', 'nima2')
pipeline.set('last2', 'nnn')

pipeline.execute()