#!/usr/bin/env python3
"""8. all documents at python. """


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
