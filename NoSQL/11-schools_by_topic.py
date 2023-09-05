#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    topic_list = []
    topics_dict = {"topics": topic}

    for elements in mongo_collection.find(topics_dict):
        topic_list.append(elements)

    return topic_list
