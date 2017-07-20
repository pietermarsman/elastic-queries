import json


class JsonComposer(dict):

    def __add__(self, other):
        # merge keys
        for key in other:
            if key in self:
                # recursive merge of keys
                self[key] = JsonComposer.combine_values(self[key], other[key])
            else:
                # simple merge: add key to self
                self[key] = other[key]
        return self

    def __repr__(self):
        return json.dumps(self, indent=4, sort_keys=True)

    @staticmethod
    def combine_values(value1, value2):
        if isinstance(value1, dict) and isinstance(value2, dict):
            # merge dicts
            return JsonComposer(value1) + JsonComposer(value2)

        elif isinstance(value1, list) and isinstance(value2, list):
            # merge lists
            return value1 + value2

        else:
            raise ValueError('Trying to combine %s with %s but I do not know how to do this.' % (type(value1), type(value2)))


if __name__ == '__main__':
    exclusive1 = JsonComposer({'a': 1})
    exclusive2 = JsonComposer({'b': 2})
    recursive1 = JsonComposer({'c': {'d': 3}})
    recursive2 = JsonComposer({'c': {'e': 4}})
    list1 = JsonComposer({'f': [5, 6, 7]})
    list2 = JsonComposer({'f': [8, 9, 10]})


    print(exclusive1 + exclusive2 + recursive1 + recursive2 + list1 + list2)