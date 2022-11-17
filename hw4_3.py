queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

def word_count(q_list):

    keys = []
    count = 0
    result = {}

    for query in q_list:
        count +=1
        if len(query.split()) not in keys:
            keys.append(len(query.split()))
            result.setdefault(len(query.split()),1)
        else:
            result[len(query.split())] += 1

    return result


# print(word_count(queries))