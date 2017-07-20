# Composable elasticsearch queries

Elasticsearch queries can sometimes be difficult to create and manage. However, the structure of a query is consistent and consists of multiple independent parts. This package allows to create queries by adding several query components. 

Lets see an example: 

```
# Select all messages from a specific user
query = Source('message') + \
        Exists('message') + \
        Term(user_id=123)
```

This package tries to mimick the [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) as much as possible. 