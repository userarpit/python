import json

# from functools import cache
import requests
# import pprint

# import asyncio
from collections import defaultdict


users = []


def keep(todo: dict) -> bool:
    is_completed = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_completed and has_max_count


# @cache
def main() -> None:
    global users
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = response.json()
    # print(todos)

    # pprint.pprint(todos[:2]) 
    todo_by_user = defaultdict(int)

    for todo in todos:
        # print(type(todo))
        if todo["completed"]:
            todo_by_user[todo["userId"]] += 1

    # pprint.pprint(todo_by_user)

    top_users = sorted(todo_by_user.items(), key=lambda x: x[1], reverse=True)
    # print(f"Top 3 users with most completed todos are {top_users}:")
    # print(top_users)
    max_complete = max(todo_by_user.values())

    for k, v in top_users:
        if v < max_complete:
            break
        users.append(str(k))
    print(users)
    max_users = " and ".join(users)

    print(f"{max_users} completed {max_complete} todos.")

    with open("filtered_data_file.json", "w") as data_file:
        filtered_todos = list(filter(keep, todos))
        json.dump(filtered_todos, data_file, indent=4)


if __name__ == "__main__":
    main()
