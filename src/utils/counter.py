from typing import List, Any

from src.classes.counter import Counter


def recursive_list_count(collection: List[Any], count_result=None) -> Counter:
    if count_result is None:
        count_result: Counter = Counter()

    if not len(collection):
        return Counter()

    for item in collection:
        if isinstance(item, list):
            recursive_list_count(item, count_result)

        else:
            count_result[item] += item.per_craft

    return count_result


def count_all_items(item, amount=1, counter=None):
    if counter is None:
        counter = Counter()
    counter[item] += amount
    if item.recipe:
        for sub_item in item.recipe:
            count_all_items(sub_item, amount, counter)
    return counter
