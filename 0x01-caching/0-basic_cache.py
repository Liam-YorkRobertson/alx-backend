#!/usr/bin/env python3
"""
a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    function that creates a basic caching system
    """
    def put(self, key, item):
        """
        puts items into the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        pulls items from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
