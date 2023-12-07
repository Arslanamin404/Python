import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age of Husband': [23, 27, 28, 29, 30, 31, 33, 35, 36, 39],
    'Age of Wife': [18, 22, 23, 24, 25, 26, 28, 29, 30, 32]
}

df = pd.DataFrame(data)

# corelation matrix
correlation_matrix = df.corr()

# Extracting correlation coefficient
correlation_coefficient = correlation_matrix.loc['Age of Husband', 'Age of Wife']


# create plot
plt.scatter(df['Age of Husband'],
            df['Age of Wife'],
            label=f"Corelation Coefficient = {round(correlation_coefficient,3)}")

plt.xlabel('Age of Husband')
plt.ylabel('Age of Wife')
plt.title('Scatter Plot of Age of Husband and Age of Wife')
plt.legend()


plt.show()