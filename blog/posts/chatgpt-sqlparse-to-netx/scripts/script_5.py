import sqlglot

with open('query.sql', 'r') as f:
  query_str = f.read()
  
joins = [j for j in sqlglot.parse(query_str).find_all(sqlglot.expressions.Join)]
