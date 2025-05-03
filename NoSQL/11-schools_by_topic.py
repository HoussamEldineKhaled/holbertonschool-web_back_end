#!/usr/bin/env python3
"""return list of school with topic"""


def schools_by_topic(mongo_collection, topic):
    """

    Args:
       mongo_collection: collection
       topic: topic in question

    Returns: list of topics
    """
    return list(mongo_collection.find({"topics" : topic}))
