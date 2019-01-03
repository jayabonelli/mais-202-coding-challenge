import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv('data.csv')
dt = (df.groupby('purpose').mean())[["int_rate"]]
dt.rename(columns = {'int_rate':'avg_rate'}, inplace = True)
dt = dt.applymap(lambda s: (((s*1000) // 1)/1000))
dt.to_csv(r'output_table.csv')
print(dt)
#dt.plot.bar(color = "Set2")
plt.figure(figsize=(15, 8))
sns.barplot(x = 'purpose', y = 'avg_rate', data = dt.reset_index(), palette = "Set2")
plt.ylabel("mean(int_rate)")
plt.savefig('output_plot.png', bbox_inches = 'tight')
plt.show()