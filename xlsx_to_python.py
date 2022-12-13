import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql+psycopg2://USERNAME:PASSWORD@localhost:PORT/DATABASE", pool_size=100000, max_overflow=200000000)

with pd.ExcelFile('C:/Users/dakus/OneDrive/Desktop/trainer_details.xlsx') as xls:
    df=pd.read_excel(xls)
    df.to_sql(name='portalapp_trainer',con=engine, if_exists='append',index=False)
    
    
    
    
