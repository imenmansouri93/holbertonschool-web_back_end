#!/usr/bin/env python3
import redis 
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrrapped function"""
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    
    return wrapper

class Cache:
    def __init__(self):
        """Create a Redis client instance and store it as a private variable"""
        self._redis = redis.Redis()
        """ Flush the Redis database to start with an empty cache"""
        self._redis.flushdb()


    
    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return ke


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



@count_calls
def store(self, data: Union[str, bytes, int, float]) -> str:
    random_key = str(uuid.uuid4())
    self._redis.set(random_key, data)
    return random_key