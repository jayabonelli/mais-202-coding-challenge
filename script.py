#importing necessary python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#setting on seaborn
sns.set()
#importing the data.csv file into a panda DataFrame
df = pd.read_csv('data.csv')
#making a new DataFrame that calculates the average interest rate (after grouping together all entries of the same purpose)
dt = (df.groupby('purpose').mean())[["int_rate"]]
#minor changes to the data set (renaming one of the columns, rounding down the numbers)
dt.rename(columns = {'int_rate':'avg_rate'}, inplace = True)
dt = dt.applymap(lambda s: (((s*1000) // 1)/1000))
#exporting the newly made data table of average interest rates as a new csv file
dt.to_csv(r'output_table.csv')
#printing out the data table
print(dt)
#setting the scale for the data plot
plt.figure(figsize=(15, 8))
#plotting the average interest rates for each given purpose using the Seaborn library, in the desired colors
sns.barplot(x = 'purpose', y = 'avg_rate', data = dt.reset_index(), palette = "Set2")
#renaming the y-axis
plt.ylabel("mean(int_rate)")
#exporting the graph we just made as a png image
plt.savefig('output_plot.png', bbox_inches = 'tight')
#displaying the graph
plt.show()
