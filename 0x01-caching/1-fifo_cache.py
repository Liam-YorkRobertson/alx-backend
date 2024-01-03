#!/usr/bin/env python3
"""
a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class that creates a caching system that uses fifo
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        adds item to cache using fifo
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        pulls item from cache
        """
        if key is not None:
            return self.cache_data.get(key)
