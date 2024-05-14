#!/usr/bin/env python3
'''
Task 9. Insert a document in Python

A function that inserts a new document in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''insert_school

    This functions purpose is to take some information through kwargs and
    insert it into mongo_collection as a new document. Then return the
    new id of the newly inserted document.

    Arguments:
        mongo_collection (pymongo Object): The mongo collection that we'll be inserting in.
        kwargs (dictionary): The data which we want to insert into the collection.

    Return:
        (int): The id of the new document inserted.
    '''
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
