# from unittest import TestCase
# from elasticsearch import Elasticsearch
# from query import Match, Range
#
#
# def get_docs(ret):
#     return ret['hits']['hits']
#
#
# class TestLive(TestCase):
#     es = None
#
#     @staticmethod
#     def query(query):
#         return TestLive.es.search('test_index', 'test_doc', query)
#
#     def setUp(self):
#         TestLive.es = Elasticsearch(
#             'localhost',
#             http_auth=('elastic', 'changeme'),
#             port=9200
#         )
#
#         doc = {
#             'bool': True,
#             'number': 5,
#             'text': 'Lorum ipsum'
#         }
#         TestLive.es.index('test_index', 'test_doc', doc, id=1)
#
#     def test_connection(self):
#         ret = TestLive.es.ping()
#         self.assertTrue(ret)
#
#     def test_all(self):
#         q = {}
#         ret = TestLive.es.search('test_index', 'test_doc', q)
#         self.assertEquals(type(ret), dict)
#         self.assertIn('hits', ret)
#         self.assertEquals(len(get_docs(ret)), 1)
#
#     def test_match(self):
#         q = Match('text', 'lorum')
#         ret = TestLive.es.search('test_index', 'test_doc', q)
#         self.assertEquals(len(get_docs(ret)), 1)
#
#     def test_range(self):
#         q = Range('number', {'gte': 10})
#         ret = TestLive.query(q)
#         self.assertEquals(len(get_docs(ret)), 0)