#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        result = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if a_dictionary[key] == result:
                return (key)
