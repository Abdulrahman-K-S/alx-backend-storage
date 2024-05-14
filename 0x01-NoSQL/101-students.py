#!/usr/bin/env python3
'''
Task 14. Top students

A function that returns all students sorted by average score.
'''


def top_students(mongo_collection):
    """top_students
    
    Arguments:
        mongo_collection (pymongo Object): The mongo collection to get the students documents.

    Return:
        (List): A list of all the students sorted by their average scores.
    """
    return mongo_collection.aggregate([
        { '$project': {
            'name': 1,
            'averageScore': { '$avg': '#topics.score' }
        }},
        { '$sort': { 'averageScore': -1 }}
    ])
