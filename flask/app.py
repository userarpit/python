from flask import Flask, url_for, redirect, abort, render_template
import os

app = Flask(__name__)

# Define the base directory of your application
# This helps in creating absolute paths for extra_files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route("/")
def index():
    title = "My app"
    heading = "Welcome"
    items = ["item 1", "item 2"]

    return render_template("index.html", title=title, heading=heading, items=items)


if __name__ == "__main__":
    
    # List extra files to watch and add them in the app
    extra_files_to_watch = [
        os.path.join(BASE_DIR, 'templates', 'index.html'),
        # You can add other files or even entire directories here if needed
        # For example, to watch all files in a 'static' folder:
        # os.path.join(BASE_DIR, 'static')
    ]
    app.run(debug=True)
