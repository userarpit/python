import pandas as pd
from load_to_mysql import ask_password, connect_mysql


def read_csv_file(engine):
    df = pd.read_csv("student_habits_performance.csv")
    print(df.head())

    df.fillna({"parental_education_level": "High school"}, inplace=True)
    df.info()

    new_df = df.loc[:, ["student_id", "age", "gender", "study_hours_per_day"]]

    new_df.to_sql("student_habits", con=engine, if_exists="append", index=False)


def read_sql(engine):
    query = """
    select count(*) from student_habits where gender = 'Male'
    """

    male_df = pd.read_sql(query, con=engine)
    print(male_df)


if __name__ == "__main__":
    # load_to_mysql.connect_mysql()
    # load_to_mysql.load_to_mysql(df, "student_habits_performance")
    password = ask_password()
    engine = connect_mysql(password)
    # print(type(engine))
    # read_csv_file(engine)
    read_sql(engine)

