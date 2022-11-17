ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def filter_unique(dict_):
    result = []
    for i in dict_.values():
        result.extend(i)

    result = list(set(result))
    return result

# print(filter_unique(ids))