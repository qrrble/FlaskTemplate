# FlaskTemplate
A simple template for a Flask app.

## Instructions
Start the app in the terminal by running `./run.py`.

## Files and folders
- `functions.py`: This is where all the functions for the app are located. You can put `import` statements in here as well. You can also put functions in `flaskexample/views.py`, but it's cleaner to put them in a separate file like this.
- `run.py`: This runs the Flask app.

- `flaskexample/views.py`: This interfaces between the backend and HTML part of your app.
- `flaskexample/templates/`: All your HTML templates go in here (ex. `index.html` and `result.html`).
- `flaskexample/static/styles/`: Javascript and CSS files go in here. These are loaded in the headers of `flaskexample/templates/index.html` and `flaskexample/templates/result.html`
