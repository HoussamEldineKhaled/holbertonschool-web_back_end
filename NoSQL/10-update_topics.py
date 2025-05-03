#!/usr/bin/env python3
"""update"""


def update_topics(mongo_collection, name, topics):
    """

    Args:
       mongo_collection: mongo collection
       name: name to update
       topics: topics in the school
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}
                                  })
