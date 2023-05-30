from sklearn.linear_model import LinearRegression
import pandas as pd

# Set the display option to show all columns and rows without truncation
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)

dt = pd.read_csv('03_height_and_weight.csv')
dt.drop(columns=['Index'], inplace=True)

inp_X = dt.drop(columns=['Weight(lbs)'])
print(dt)
