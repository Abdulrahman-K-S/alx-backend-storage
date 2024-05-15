#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis

Create a cache class and create it's constructor and store method.
"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache
    """
    def __init__(self):
        """__init__

        The initalization of the Cache class stores an instance of redis
        in the private variable _redis and flushes the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store

        This method generates a random key, stores the input data in Redis using
        the random key and returns the key.

        Arguments
            data ():

        Return:
            (str): The random key generated.
        """
        redisKey = str(uuid4())
        self._redis.set(redisKey, data)
        return redisKey
