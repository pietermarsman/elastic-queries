from elastic_queries.json_composer import JsonComposer


class Source(JsonComposer):
    def __init__(self, fields):
        if type(fields) is not list:
            fields = [fields]
        super().__init__(_source=fields)


class Query(JsonComposer):
    def __init__(self, *args, combine='must'):
        query = {
            'bool': {
                combine: list(args)
            }
        }
        super().__init__(query=query)


class Sort(JsonComposer):
    def __init__(self, field, order='desc'):
        super().__init__(sort=[{field: {'order': order}}])


# Full text queries

class Match(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'match': {field: value}}, **kwargs)


class MatchPhrase(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'match_phrase': {field: value}}, **kwargs)


class MatchPhrasePrefix(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'match_phrase_prefix': {field: {'query': value}}}, **kwargs)


class MultiMatch(Query):
    def __init__(self, fields, value, **kwargs):
        # todo add **kwargs besides query
        super().__init__({'multi_match': {'query': value, 'fields': fields}}, **kwargs)


class Common(Query):
    def __init__(self, field, value, combine='must'):
        # todo add **kwargs besides query
        super().__init__({'common': {field: {'query': value}}})


class QueryString(Query):
    def __init__(self, value):
        # todo add **kwargs besides query
        super().__init__({'query_string': {'query': value}})


class SimpleQueryString(Query):
    def __init__(self, value):
        # todo add **kwargs besides query
        super().__init__({'simple_query_string': {'query': value}})


# Term level queries

class Term(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'term': {field: value}}, **kwargs)


class Terms(Term):
    pass


class Range(Query):
    def __init__(self, field, ranges, **kwargs):
        super().__init__({'range': {field: ranges}}, **kwargs)


class Exists(Query):
    def __init__(self, field, **kwargs):
        super().__init__({'exists': {'field': field}}, **kwargs)


class Prefix(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'prefix': {field: value}}, **kwargs)


class Wildcard(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'wildcard': {field: value}}, **kwargs)


class Regexp(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'regexp': {field: value}}, **kwargs)


class Fuzzy(Query):
    def __init__(self, field, value, **kwargs):
        super().__init__({'fuzzy': {field: value}}, **kwargs)


class Type(Query):
    def __init__(self, type, **kwargs):
        super().__init__({'type': {'value': type}}, **kwargs)


class Ids(Query):
    def __init__(self, ids, **kwargs):
        super().__init__({'ids': {'values': ids}}, **kwargs)
