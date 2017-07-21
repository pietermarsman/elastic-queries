import json
from unittest import TestCase

from elastic_queries.json_composer import JsonComposer


class TestJsonComposer(TestCase):
    def test_empty(self):
        empty = JsonComposer()
        empty2 = empty + empty
        self.assertEqual(empty, empty2)

    def test_overlap_exception(self):
        a = JsonComposer(a=1)
        self.assertRaises(ValueError, lambda: a + a)

    def test_additive_keys(self):
        a = JsonComposer(a=1)
        b = JsonComposer(b=2)
        both = a + b
        self.assertIn('a', both)
        self.assertIn('b', both)

    def test_additive_values(self):
        list1 = JsonComposer(list=[1])
        list2 = JsonComposer(list=[2])
        both = list1 + list2
        self.assertIn(1, both['list'])
        self.assertIn(2, both['list'])
        self.assertEqual(len(both['list']), 2)

    def test_additive_dicts(self):
        dict1 = JsonComposer(dict={'a': 3})
        dict2 = JsonComposer(dict={'b': 4})
        both = dict1 + dict2
        self.assertIn('a', both['dict'])
        self.assertEqual(len(both['dict']), 2)

    def test_json_repr(self):
        obj = JsonComposer({'a': {'b': {'c': [1, 2, 3]}, 'd': 'b'}})
        json_repr = str(obj)
        obj2 = json.loads(json_repr)
        self.assertEqual(obj, obj2)
