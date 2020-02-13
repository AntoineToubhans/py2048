# %%
import pandas as pd
import matplotlib.pyplot as plt

from src.agent.random_agent import RandomAgent
from src.agent.runner import run_agent

# %%
random_agent = RandomAgent()

# %%
NUMBER_RUN = 1000

# %%
trace_descriptions = []

for run_index in range(NUMBER_RUN):
    trace = run_agent(random_agent)
    trace_description = trace.describe()

    print(f'{run_index}: {trace_description}')

    trace_descriptions.append(trace_description)

    del trace

# %%
descriptions_df = pd.DataFrame(trace_descriptions)

# %%
descriptions_df.hist(figsize=(12, 12))
plt.show()

# %%
descriptions_df.score.hist(bins=50)
plt.show()
