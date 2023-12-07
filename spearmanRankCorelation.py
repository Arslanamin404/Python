import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Advertisement Cost (in thousands)': [39, 65, 62, 90, 89, 75, 25, 98, 36, 78],
    'Sales (in lakhs)': [47, 53, 58, 86, 62, 68, 60, 91, 51, 84]
}


df = pd.DataFrame(data)

# Spearman's rank corelation coff
correlation_matrix = df.corr(method='spearman')

# Extracting correlation coefficient
correlation_coefficient = correlation_matrix.loc[
    'Advertisement Cost (in thousands)',
    'Sales (in lakhs)'
]


# create plot
plt.plot(df['Advertisement Cost (in thousands)'],
         df['Sales (in lakhs)'],
         label=f"Spearman's Rank Corelation = {round(correlation_coefficient,3)}")

plt.xlabel('Advertisement Cost (in thousands)')
plt.ylabel('Sales (in lakhs)')
plt.title('Scatter Plot of Advertisement Cost (in thousands) and Sales (in lakhs)')
plt.legend()


plt.show()
