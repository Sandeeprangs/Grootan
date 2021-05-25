import pandas as pd

data = pd.read_csv (r'C:\Users\Desktop\Test\Bank.csv')   
df = pd.DataFrame(data, columns= ['Descrption','Deposits','Withdrawl','Balance'])

print(df)