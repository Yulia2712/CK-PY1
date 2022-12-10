import random
def get_unique_list_numbers() -> list[int]:
    random_int = random.randint(-10, 10)
    list_unic = random.sample(range(-10,10), 15)

    return list_unic




list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

