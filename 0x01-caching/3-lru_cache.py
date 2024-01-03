#!/usr/bin/env python3
"""
a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    a class that creates a caching system that uses lru
    """

    def __init__(self):
        """
        initializes
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        adds item to cache using lru
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.order.append(key)
            self.order = [k for k in self.order if k != key] + [key]

    def get(self, key):
        """
        pulls from cache
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

