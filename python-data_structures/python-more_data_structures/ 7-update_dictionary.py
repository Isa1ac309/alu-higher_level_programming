#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    backup_dictionary = a_dictionary.copy()
    backup_dictionary[key] = value
    return backup_dictionary