def rack_query(rack):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_letters = {letter: rack.count(letter) for letter in alphabet}
    query = "SELECT word\nFROM Word\nWHERE " + "\nAND ".join([f"num_{letter} <= {num}" for (letter, num) in num_letters.items()]) + ";"

    return query


def list_query(length=None, contain_letters=tuple(), contains_all=True, without_letters=tuple()):
    where_inserted = False
    query = "SELECT word, anagram\nFROM Word"

    if length is not None:
        query += f"\nWHERE length = {length}"
        where_inserted = True

    if len(contain_letters) > 0:
        if where_inserted:
            if contains_all:
                query += f"\nAND (num_{contain_letters[0].upper()} > 0"
                for letter in contain_letters[1:]:
                    query += f"\nAND num_{letter.upper()} > 0"

                query += ")"

            else:
                query += f"\nAND (num_{contain_letters[0].upper()} > 0"
                for letter in contain_letters[1:]:
                    query += f"\nOR num_{letter.upper()} > 0"

                query += ")"

        else:
            if contains_all:
                query += f"\nWHERE (num_{contain_letters[0].upper()} > 0"
                for letter in contain_letters[1:]:
                    query += f"\nAND num_{letter.upper()} > 0"

                query += ")"

            else:
                query += f"\nWHERE (num_{contain_letters[0].upper()} > 0"
                for letter in contain_letters[1:]:
                    query += f"\nOR num_{letter.upper()} > 0"

                query += ")"

            where_inserted = True

    if len(without_letters) > 0:
        if where_inserted:
            for letter in without_letters:
                query += f"\nAND num_{letter.upper()} = 0"

        else:
            query += f"\nWHERE num_{without_letters[0].upper()} = 0"
            for letter in without_letters[1:]:
                query += f"\nAND num_{letter.upper()} = 0"

            where_inserted = True

    query += ";"

    return query


if __name__ == "__main__":
    print(rack_query(("A", "B", "C", "D", "E", "F", "G")))
    print("-" * 50)
    print(rack_query(""))
    print("-" * 50)
    print(list_query())
    print("-" * 50)
    print(list_query(length=3))
    print("-" * 50)
    print(list_query(contain_letters=("Q", "U")))
    print("-" * 50)
    print(list_query(without_letters=("Q", "U")))
    print("-" * 50)
    print(list_query(length=4, contain_letters=("A", "B"), contains_all=False, without_letters=("Q", "U")))
    print("-" * 50)
    print(rack_query(("C", "D", "D", "E", "F", "G", "I")))

    pass