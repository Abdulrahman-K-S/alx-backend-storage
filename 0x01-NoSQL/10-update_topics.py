#!/usr/bin/env python3
'''
Task 10. Change school topics

A function that changes all topics of a school document based on the name
'''


def update_topics(mongo_collection, name, topics):
    '''update_topics

    This function changes all the topics of a school document based on the
    name.

    Arguments:
        mongo_collection (pymongo Object): The mongo collection we'll be updating in.
        name (string): The name of the school to update it's topics.
        topics (list of strings): A list of the topics to update in the school.
    '''
    schools = { 'name': name }
    values = { '$set': { 'topics': topics }}
    mongo_collection.update_many(
        schools,
        values
    )
