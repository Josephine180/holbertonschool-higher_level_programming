#!/usr/bin/python3

class VerboseList(list):
    pass

    def append(self, item):
        print(f'Added {item} to the list.')
        super().append(item)

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f'Extended the list with {num_items} items.')

    def remove(self, item):
        print(f'Removed {item} from the list.')
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f'Popped {item} from the list.')
        super().pop(index)
