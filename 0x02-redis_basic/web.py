#!/usr/bin/env python3
"""
Task 5. Implementing an expiring web cache and tracker

Implement an expiring web cache and tracker
"""

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """count_requests

    Decorator for counting how many times a request
    has been made

    Arguments:
        method (Callable): The function to call.

    Return:
        (Callable): The wrapped function.
    """

    @wraps(method)
    def wrapper(url):
        """wrapper

        Arguments:
            url (str): The url passed to get_page.
        """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper

@count_requests
def get_page(url: str) -> str:
    """get_page
    
    Arguments:
        url (str): The url to check & track.

    Return:
        (str): The chached result.
    """
    req = requests.get(url)
    return req.text