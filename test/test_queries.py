from unittest import TestCase

from elastic_queries.query import Source, Match, Sort


class TestQueries(TestCase):
    def test_source(self):
        q = Source('field')
        self.assertIn('_source', q)
        self.assertIn('field', q['_source'])

    def test_query(self):
        field = 'field'
        value = 'value'
        q = Match(field, value)
        query = {
            'query': {
                'bool': {
                    'must': [
                        {
                            'match': {
                                field: value
                            }
                        }
                    ]
                }
            }
        }
        self.assertEqual(q, query)

    def test_sort(self):
        q = Sort('post_date', order='asc')
        query = {
            "sort": [
                {
                    "post_date": {
                        "order": "asc"
                    }
                }
            ]
        }
        self.assertEqual(q, query)
