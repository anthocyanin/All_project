from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379)
redis.set('name', 'Bob')
print(redis.get('name'))
print(redis.exists('name'))
print(redis.type('name'))
print(redis.rename('name', 'nickname'))


