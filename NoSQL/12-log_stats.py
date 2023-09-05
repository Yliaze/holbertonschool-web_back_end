#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs

    """Count total logs"""
    logs_count = db.nginx.count_documents({})
    print(f"{logs_count} logs")

    """Count total of each methods"""
    print(f"Methods:")
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    """Count checked status"""
    status_dict = {"method": "GET", "path": "/status"}
    status_count = db.nginx.count_documents(status_dict)
    print(f"{status_count} status check")
