import csv


def generate_insert_query(csv_file, table_name):
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        columns = next(reader)  # First row contains column names
        queries = []

        for row in reader:
            values = [f"'{value}'" if value else "NULL" for value in row]
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});"
            queries.append(query)

        return queries


if __name__ == "__main__":
    # Example usage
    csv_file_path = "data.csv"  # Replace with your CSV file path
    table_name = "pediatrics.employee_occupation"  # Replace with your table name
    insert_queries = generate_insert_query(csv_file_path, table_name)

    # Print or save the queries
    with open("insert_queries.sql", "w", encoding="utf-8") as output_file:
        for query in insert_queries:
            output_file.write(query + "\n")

