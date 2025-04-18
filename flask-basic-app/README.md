# Flask Basic App

This is a basic Flask application template. It serves as a starting point for building Flask web applications.

## Project Structure

```
flask-basic-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── base.html
├── requirements.txt
└── README.md
```

## Requirements

To run this application, you need to have Python and Flask installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

To run the Flask application, navigate to the project directory and use the following command:

```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command:

For Windows:
```
set FLASK_APP=app
```

For macOS/Linux:
```
export FLASK_APP=app
```

Once the server is running, you can access the application in your web browser at `http://127.0.0.1:5000/`.