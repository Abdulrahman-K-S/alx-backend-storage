#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis

Create a cache class and create it's constructor and store method.
"""

import redis
from uuid import uuid4
from typing import Union, Callable


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
            data (str/bytes/int/float): The data that will be stored inside redis.

        Return:
            (str): The random key generated.
        """
        redisKey = str(uuid4())
        self._redis.set(redisKey, data)
        return redisKey

    def get(self, key: str, fn: Callable = None):
        """get

        This method takes in a key str and an optional callable and returns
        the data with the correct conversion function.

        Arguments:
            key (str): The key which we'll get its data
            fn (Callable): The function we'll invoke. Default=None

        Return:
            (str/int): Depending on what the fn will be.
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """get_str

        The str conversion function

        Arguments:
            key (str): The key which we'll get its data

        Return:
            (str): The data as an str variable
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """get_int

        The int conversion function

        Arguments:
            key (str): The key which we'll get its data

        Return:
            (int): The data as an int variable
        """
        try:
            data = int((self._redis.get(key)).decode("utf-8"))
        except Exception:
            data = 0
        return data

