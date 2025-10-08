import redis 

redis_client = redis.Redis()

with redis_client.pipeline(transaction=True) as pipe:
    try:
        pipe.watch('name')

        pipe.multi()
        pipe.set('name', 'ali ali ali')
        pipe.set('last', 'mmd mmd mmd')
        
        result = pipe.execute()
        print(f'success {result}')

    except redis.WatchError:
        print('transaction error: the key was changed during operation')
    except redis.ResponseError:
        print('redis responses error')
    except Exception:
        print('somthing went wrong')
        