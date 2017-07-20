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
