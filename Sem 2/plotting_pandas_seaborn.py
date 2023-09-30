# %%
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
df.plot(subplots=True)

# %%
s = pd.Series(np.random.randn(10))
s.plot.bar()

# %%
df = pd.DataFrame(
    np.random.rand(6, 4),
    index=["one", "two", "three", "four", "five", "six"],
    columns=pd.Index(["A", "B", "C", "D"], name="Genus"),
)
df.plot.bar()

# %%
df.plot.bar(stacked=True)
# %%
sns.barplot(data=df)
# %%
data = pd.Series(np.random.randn(1000), np.random.randn(1000))
sns.scatterplot(data)
# %%
