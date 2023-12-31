#!/usr/bin/env python3
"""
    String Redis
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator count calls """
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
        """ Store the input arguments in the history"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        result = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", result)
        return result

    return wrapper


def replay(cache, method):
    """replay method"""
    history_key = method.__qualname__ + ":inputs"
    call_history = cache._redis.lrange(history_key, 0, -1)
    if len(call_history) % 2 == 0:
        for inputs, output in zip(call_history[::2], call_history[1::2]):
            print("Inputs: ", inputs.decode())
            print("outputs", output.decode())
    else:
        print("Call history is incomplete or has an odd number of elements.")


class Cache:
    """Cache"""
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
        """get-str function"""
        return self.get(key, fn=lambda data: data.decode())

    def get_int(self, key):
        """get-int function"""
        return self.get(key, fn=lambda data: int(data.decode()))
