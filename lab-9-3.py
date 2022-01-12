# Author JRI 1/11/22


def add_foods(lst):
    short_foods = []
    sixth_letter = []
    not_foods = []
    for foods in lst:
        try:
            sixth_letter.append(foods[5])
        except TypeError:
            not_foods.append(foods)
        except IndexError:
            short_foods.append(foods)


    print("sixth_letter: ", sixth_letter)
    print("not_foods: ", not_foods)
    print("short_foods: ", short_foods)


add_foods(["potatoes", "salsa", "cherries", "banana", "apple"])
add_foods(["naan", "celery", "buckwheat", 7, "clementine"])
add_foods(["chesseburger", True, "chicken", "rice", "radish"])