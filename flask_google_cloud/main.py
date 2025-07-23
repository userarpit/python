from flask import Flask, render_template
import os
import datetime

from google.cloud import datastore

app = Flask(__name__)
# Replace 'your-project-id' with your actual Google Cloud Project ID
project_id = "glowing-reserve-466406-r8"  # Example, use your real ID
client = datastore.Client(project=project_id)


def store_time(dt):
    entity = datastore.Entity(key=client.key("visit"))
    entity.update({"timestamp": dt})

    client.put(entity)


def fetch_times(limit):
    query = client.query(kind="visit")
    query.order = ["-timestamp"]

    times = query.fetch(limit=limit)

    return times


# Define the base directory of your application
# This helps in creating absolute paths for extra_files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    title = "My app"
    heading = "Welcome"
    items = ["item 1", "item 2"]
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now(tz=datetime.timezone.utc))

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template(
        "index.html", title=title, heading=heading, items=items, times=times
    )


@app.route("/about")
def about():
    return "Arpit"


if __name__ == "__main__":
    # List extra files to watch and add them in the app
    extra_files_to_watch = [
        os.path.join(BASE_DIR, "templates", "index.html"),
        # You can add other files or even entire directories here if needed
        # For example, to watch all files in a 'static' folder:
        # os.path.join(BASE_DIR, 'static')
    ]
    app.run(debug=True)
