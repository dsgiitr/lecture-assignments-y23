import sys
import pandas as pd
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("no data directory provided")
        sys.exit(1)
    path=sys.argv[1]
    df =pd.read_csv("{path1}/melb_data.csv".format(path1=path))#melb_data is the name of the file with training data
    '''
    train the model
    save the output in dataframe
    '''
    predictions_dataframe.to_csv(output_path,index=False)
    
    
        
