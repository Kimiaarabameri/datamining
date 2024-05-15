from matplotlib import pyplot as plt
import pandas as pd  
import numpy
from scipy import stats
import matplotlib
data = pd.read_csv('USA_Housing.csv')  
data_price=data.loc[:, ['mean_Price']]
data_income=data.loc[:, ['mean_Avg.AreaIncome']]
def avg(avgp,avgi):
    
    mean_price=avgp/5000
    mean_income=avgi/5000
    print(f'{mean_price}')
    print(f'{mean_income}')
 

miane_price=numpy.median(data_price)
miane_income=numpy.median(data_income)
nama_price=stats.mode(data_price)
nama_income=stats.mode(data_income)
print(f'median Price is:{miane_price}')
print(f'median Avg.AreaIncome is:{miane_income}')
print(f'mode is Price:{nama_price}')
print(f'mode is Avg.AreaIncome:{nama_price}')
x=data_price
y=data_income
plt.scatter(x,y)
plt.show()
avgP=data_price.sum()
avgI=data_income.sum()
avg(avgP,avgI)



