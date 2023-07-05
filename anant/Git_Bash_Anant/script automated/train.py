import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
def train(df):
    df.dropna(inplace=True)
    y=df['Price']
    df.drop('Price',axis=1,inplace=True)
    for column in df.columns:
    if df.dtypes[column]=='object':
        df.drop(column,axis=1,inplace=True)
    lin_reg = LinearRegression()
    lin_reg.fit(df,y)
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("no data directory provided")
        sys.exit(1)
    path=sys.argv[1]
    df =pd.read_csv(f"{path}/melb_data.csv")
    train(df)
    
    
        
