"""Print the completed packets from the clock simulation as a Markdown table."""

import pandas

from run_simulation import simulation

records = pandas.DataFrame(simulation.get_all_records())
print(records[['node', 'exit_date']].to_markdown(index=False))
