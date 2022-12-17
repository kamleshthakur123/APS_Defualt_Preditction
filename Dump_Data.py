import pymongo
import pandas as pd  
import json 

### provide the mongodb localhost url to connect mongodb with python

client=pymongo.MongoClient("mongodb+srv://root:kam1993@cluster0.o5a8fjl.mongodb.net/?retryWrites=true&w=majority")

Data_File_Path="/config/workspace/aps_failure_training_set1.csv"
Database_Name="aps"
collection_Name="sensor"

if __name__=="__main__":
    df=pd.read_csv(Data_File_Path)
    print(f"shape of the data is :{df.shape}")


    ### convert dataframe to json so that we can dump this dataframe to mongodb
    df.reset_index(drop=True,inplace=True)

    json_records= list(json.loads(df.T.to_json()).values())

    print(json_records[0])

    ### insert converted json into mongodb
    client[Database_Name][collection_Name].insert_many(json_records)
