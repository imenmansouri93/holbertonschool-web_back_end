#!/usr/bin/env python3
import redis 
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper
    
def call_history(method: Callable) -> Callable:
    """Decorator call history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrrapped function"""
        history_key = method.__qualname__ + ":_history"
        """ Store the input arguments in the history"""
        self._redis.rpush(history_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(history_key, str(result))
        return result
    
    return wrapper

class Cache:
    def __init__(self):
        """Create a Redis client instance and store it as a private variable"""
        self._redis = redis.Redis()
        """ Flush the Redis database to start with an empty cache"""
        self._redis.flushdb()


    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


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

