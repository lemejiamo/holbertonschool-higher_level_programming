#!/usr/bin/python3
""" script to add elements to a python list
and then save the them to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    list = load_from_json_file("add_item.json")
except:
    list = []

list.extend(sys.argv[1:])
save_to_json_file(list, "add_item.json")
