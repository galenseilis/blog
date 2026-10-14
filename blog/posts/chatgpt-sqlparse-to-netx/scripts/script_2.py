import sqlparse
import networkx as nx

# Create a NetworkX MultiGraph
G = nx.MultiGraph()

# Define a function to extract table and column information from SQL queries
def extract_tables_columns(sql_query):
    parsed = sqlparse.parse(sql_query)
    tables = set()
    join_conditions = []

    for stmt in parsed:
        from_seen = False
        last_table = None

        for token in stmt.tokens:
            if token.value.upper() == 'FROM':
                from_seen = True
            elif from_seen and isinstance(token, sqlparse.sql.Identifier):
                table_name = token.get_real_name()
                tables.add(table_name)
                if last_table:
                    join_conditions.append((last_table, table_name))
                last_table = table_name

    for table in tables:
        G.add_node(table)

    for left, right in join_conditions:
        G.add_edge(left, right)

# Load your SQL queries from .sql files
with open('queries.sql', 'r') as file:
    sql_queries = file.read().split(';')  # Split queries by semicolon

# Extract tables and columns from the SQL queries
for sql_query in sql_queries:
    extract_tables_columns(sql_query)

# Print the nodes and edges to verify
print("Nodes:")
print(G.nodes())
print("Edges:")
print(G.edges())

# Now, G should correctly represent the relationships between tables and columns in your SQL queries.

# You can perform various network analysis tasks on G using NetworkX functions.

import matplotlib.pyplot as plt
# Create a plot
plt.figure(figsize=(10, 10))

# Draw nodes with labels
pos = nx.spring_layout(G, seed=42)  # You can use other layouts as well
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')

# Draw edges
nx.draw(G, pos, with_labels=False, node_size=300, node_color='skyblue', alpha=0.7, linewidths=0.5, font_size=10)

# Draw edge labels manually for multi-edges
edge_labels = {}
for u, v, keys, data in G.edges(data=True, keys=True):
    label = data.get('label', '')
    if label:
        if (u, v) not in edge_labels:
            edge_labels[(u, v)] = label
        else:
            edge_labels[(u, v)] += f", {label}"

# Draw edge labels manually
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_isze=10)

# Save the plot
plt.axis('off')
plt.savefig('chatgpt_create_multigraph_from_sql.png', dpi=300, transparent=True)
plt.close()
