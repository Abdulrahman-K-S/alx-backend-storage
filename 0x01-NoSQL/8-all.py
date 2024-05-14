#!/usr/bin/env python3
'''
Task 8. List all documents in Python

A function that lists all documents in a collection
'''


def list_all(mongo_collection):
    '''list_all

    This function's purpose is to list all documents in
    the collection that is passed to it's parameter.

    Attributes:
        mongo_collection (pymongo Object): The mongo collection to list its documents.

    Return:
        (List): The collection of the documents if exists otherwise an empty
                list
    '''
    return mongo_collection.find({})