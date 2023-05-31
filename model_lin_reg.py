from sklearn.linear_model import LinearRegression
import pandas as pd

dt = pd.read_csv('03_height_and_weight.csv')
dt.drop(columns=['Index'], inplace=True)

inp_X = dt[['Height(In)']]  # Your input feature is Height
feature_names = inp_X.columns
out_y = dt['Weight(lbs)']  # You're trying to predict Weight

Model = LinearRegression()
Model.fit(inp_X, out_y)

# Use a DataFrame for prediction
predict_df = pd.DataFrame([[60]], columns=feature_names)
result = Model.predict(predict_df)

print(result)
