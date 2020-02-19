
from sqlalchemy import create_engine
import pandas as pd

def mySQLtoDataframe(userName,password,host,databaseName,tableName):
    # This will connect with a MySQL table and convert its data into pandas dataframe
    db_connection_str = 'mysql+pymysql://{}:{}@{}/{}'.format(userName,password,host,databaseName)
    db_connection = create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM {}'.format(tableName), con=db_connection)

    return df

#df = mySQLtoDataframe('rbt','rbt.1234','10.0.0.21','anushan','uploaded_contents')

#print(df['name'])


