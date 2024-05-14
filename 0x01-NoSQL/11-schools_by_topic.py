#!/usr/bin/env python3
'''
Task 11. Where can I learn Python?

A functino that returns the list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''schools_by_topic

    This function returns the list of school which has a specific topic.

    Arguments:
        mongo_collection (pymongo Object): The mongo collection we'll be searching in.
        topic (string): The topic to search by.

    Return:
        (list): The list of documents found by the inputed paramter.
    '''
    return mongo_collection.find({ 'topics': topic })
