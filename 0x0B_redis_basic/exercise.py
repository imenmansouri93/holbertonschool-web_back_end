#!/usr/bin/env python3
import redis 
import uuid

class Cache:
    def __init__(self):
        """Create a Redis client instance and store it as a private variable"""
        self._redis = redis.Redis()
        """ Flush the Redis database to start with an empty cache"""
        self._redis.flushdb()


    def store (self, data):
        """Generate a random key using UUID"""
        Random_key = str(uuid.uuid4())
        """Store the input data in Redis using the random key"""
        self._redis.set(Random_key, data)
        """return random key"""
        return Random_key


    def get(self, key):
        return self._redis.get(key)
