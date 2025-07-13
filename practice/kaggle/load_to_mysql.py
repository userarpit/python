import getpass
from sqlalchemy import create_engine
# import pandas as pd


def ask_password():
    return getpass.getpass("Enter your mysql password")


def connect_mysql(password):
    engine = create_engine(
        f"mysql+pymysql://root:{password}@localhost:3306/world"
    )  # mysql+pymysql://<username>:<password>@<host>:<port>/<database>

    try:
        with engine.connect() as connection:
            print("successfully")
    except Exception as e:
        print(f"{e}")
    
    return engine
