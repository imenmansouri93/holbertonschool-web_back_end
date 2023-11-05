#!/usr/bin/env python3
import redis 
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
    def __init__(self):
        """Create a Redis client instance and store it as a private variable"""
        self._redis = redis.Redis()
        """ Flush the Redis database to start with an empty cache"""
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key using UUID"""
        Random_key = str(uuid.uuid4())
        """Store the input data in Redis using the random key"""
        self._redis.set(Random_key, data)
        """return random key"""
        return Random_key


    def get(self, key, fn=None):
        """Retrieve the data from the cach"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        else:
            return data
    
    def get_str(self, key):
        return self.get(key, fn=lambda data: data.decode())

    def get_int(self, key):
        return self.get(key, fn=lambda data: int(data.decode()))

def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrrapped function"""
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    
    return wrapper

@count_calls
def store(self, data: Union[str, bytes, int, float]) -> str:
    random_key = str(uuid.uuid4())
    self._redis.set(random_key, data)
    return random_key