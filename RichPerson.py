RichPerson = ((1, 2, 3), (3, 4, 5), (7, 8, 6, 5), (4, 3, 2), 2, 3, 4)


def ret_rich_person(RichPerson):
    Result = []

    for person in RichPerson:

        try:

            if len(person) > 1:
                val = sum(person)
                Result.append(val)
        except TypeError:
            Result.append(person)
    Result.sort()
    return max(Result), min(Result), Result, Result[::-1]


res = ret_rich_person(RichPerson)
print(res)