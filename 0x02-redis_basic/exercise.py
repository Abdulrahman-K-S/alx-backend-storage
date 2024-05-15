#!/usr/bin/env python3
"""
Creating the redis exercise file to address various tasks.
"""

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count_calls

    This method counts the number of key every time it's called by
    the method and returns it's orignal value.

    Arguments:
        method (Callable): The function to call.

    Return:
        (Callable): The wrapped function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds) -> Callable:
        """wrapper

        Arguments:
            *args (tuple): Variable length argument list.
            **kwds (dictionary): Arbitrary keyword arguments.

        Return:
            (Callable): The result of invoking the original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history

    Everytime the original function will be called, we will add its
    input parameters to one list in redis, and store its output into another list.

    Arguments:
        method (Callable): The function to call.

    Return:
        (Callable): The wrapped function.
    """
    qualified_name = method.__qualname__
    input_key = qualified_name + ":inputs"
    output_key = qualified_name + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper

        Arguments:
            *args (tuple): Variable length argument list.
            **kwds (dictionary): Arbitrary keyword arguments.
    
        Return:
            (Callable): The result of invoking the original method.
        """
        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """replay

    This function displays the history of calls of a particular function.

    Arguments:
        method (Callable): The function to call.
    """
    redis = method.__self__._redis
    qualified_name = method.__qualname__
    num_of_calls = redis.get(qualified_name).decode("utf-8")
    print("{} was called {} times:".format(qualified_name, num_of_calls))
    input_key = qualified_name + ":inputs"
    output_key = qualified_name + ":outputs"
    input_list = redis.lrange(input_key, 0, -1)
    output_list = redis.lrange(output_key, 0, -1)
    r_zipped = list(zip(input_list, output_list))
    for key, value in r_zipped:
        key = key.decode("utf-8")
        value = value.decode("utf-8")
        print("{}(*{}) -> {}".format(qualified_name, key, value))




class Cache:
    """Cache

    Attributes:
        _redis: The redis connection and the important part of the Cache class. 
    """

    def __init__(self):
        """__init__

        The initalization of the Cache class stores an instance of redis
        in the private variable _redis and flushes the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

