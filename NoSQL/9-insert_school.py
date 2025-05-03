#!/usr/bin/env python3
"""insert document python"""


def insert_school(mongo_collection, **kwargs):
    """insert new doc
    Args:
       mongo_collection: mongo collection
       kwargs: collection base
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
