import redis 

r = redis.Redis()

r.set('name', 'hmz', ex=7)
result = r.get('name')
# or any other command (set, list, hash, sorted-set or ..)

print(result)