#!/usr/bin/env python3
"""
Task 15. Log stats - new version

Improve 12-log_stats.py by adding the top 10 of the most present IPs
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """log_stats

    An improved version of 12-log_stats.py that adds the top 10 most present
    IPs in the collection nginx of the database logs.

    Arguments:
        mongo_collection (pymongo Object): The mongo DB.
    """
    print('{} logs'.format(mongo_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(mongo_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        mongo_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))
    print('IPs:')
    request_logs = mongo_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)
