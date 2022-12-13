import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql+psycopg2://crm:root@crm.centralus.cloudapp.azure.com:5432/crm", pool_size=100000, max_overflow=200000000)

with pd.ExcelFile('C:/Users/dakus/OneDrive/Desktop/trainer_details.xlsx') as xls:
    df=pd.read_excel(xls)
    df.to_sql(name='portalapp_trainer',con=engine, if_exists='append',index=False)
    
    
    
    
