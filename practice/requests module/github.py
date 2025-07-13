# import asyncio
import requests


def main():
    response = requests.get(
        "https://api.github.com/search/repositories",
        [("q", "language:python"), ("sort", "stars"), ("order", "desc")],
    )

    if response:
        # print(response.json())
        popular_repos = response.json().get("items", [])
        print((popular_repos[0]))
        for repo in popular_repos:
            print(f"Name: {repo['name']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")
            print("-" * 40)
    else:
        print("Error: Unable to fetch data from GitHub API.")


if __name__ == "__main__":
    main()
