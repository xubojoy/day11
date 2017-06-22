#Author:xubojoy
import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))