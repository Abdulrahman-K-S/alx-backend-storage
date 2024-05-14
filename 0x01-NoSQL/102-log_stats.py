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
    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        documents = mongo_collection.count_documents({ "method": method })
    print("Methods:")
    print(f"\tmethod {method}: {documents}")
    status = mongo_collection.count_documents({ "method": "GET",
                                              "path": "/status" })
    print(f"{status} status check")

    print("IPs:")
    first_IPs = mongo_collection.aggregate([
        { "$group":
         {
             "_id": "$ip",
             "count": { "$sum": 1 }
         }
         },
        { "$sort": { "count": -1 }},
        { "$limit": 10 },
        { "$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for ips in first_IPs:
        count = ips.get("count")
        ip_address = ips.get("ip")
        print(f"\t{ip_address}: {count}")


if __name__ == "__main__":
    with MongoClient() as client:
        collection = client.logs.nginx
        log_stats(collection)
