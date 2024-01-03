#!/usr/bin/env python3
"""
a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    a class that creates a caching system that uses lfu
    """

    def __init__(self):
        """
        initializes
        """
        super().__init__()
        self.usage_count = {}

    def put(self, key, item):
        """
        adds item to cache using lfu
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_usage = min(self.usage_count.values())
                least_used_keys = [k for k, v in self.usage_count.items()
                                   if v == min_usage]

                if len(least_used_keys) > 1:
                    lfu_key = min(least_used_keys,
                                  key=lambda k: self.usage_count[k])
                else:
                    lfu_key = least_used_keys[0]

                del self.cache_data[lfu_key], self.usage_count[lfu_key]
                print("DISCARD: {}".format(lfu_key))

            self.cache_data[key] = item
            self.usage_count[key] = self.usage_count.get(key, 0) + 1

    def get(self, key):
        """
        pulls from cache
        """
        if key is not None and key in self.cache_data:
            self.usage_count[key] = self.usage_count.get(key, 0) + 1
            return self.cache_data[key]
        return None
