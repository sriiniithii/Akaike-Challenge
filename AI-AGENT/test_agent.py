
from agent.basic_data_agent import create_agent, run_query

csv_file = "data/dress.csv"
agent = create_agent(csv_file)

queries = [
    "Top 5 customers with the most purchases?","How many customers bought Laptop?","List all products purchased by Alice","Who purchased Phone?","Total unique products purchased?"
]

for query in queries:
    print(f"Q: {query}")
    print(f"A: {run_query(agent, query)}\n")