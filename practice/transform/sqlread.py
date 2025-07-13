import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(f"mysql+pymysql://root:psra10051986@localhost:3306/world")

df_query = pd.read_sql("uber", con=engine)
print("DataFrame from SQL Query:\n", df_query)


df_sel_col = pd.read_sql("uber", con=engine, columns=["user_id", "amount"])
print(df_sel_col)

for chunk_df in pd.read_sql("SELECT * FROM city", con=engine, chunksize=5):
    print(type(chunk_df))
    # break# Process each chunk as needed4
    
    
engine.dispose()