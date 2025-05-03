#!/usr/bin/env python3
"""list all document in python"""


def list_all(mongo_collection):
    """

    Args:
       mongo_collection: database collection

    Returns: collections list
    """
    return list(mongo_collection.find())
