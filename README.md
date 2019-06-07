# Imflask

Imflask is a prototype of simple web application built from [Flask (Python)](http://flask.pocoo.org/), to provide an example of implementing [Jinja](http://jinja.pocoo.org/) template engine in Flask web apps on awesome Bootstrap theme: [Impact](https://templatemag.com/impact/).

## Getting Started

1. Make sure Python 3.x and `venv` module are already installed.

2. Create Python virtual environment and then activate it as shown in [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) tutorial.

3. Let's suppose your working directory right now is your user home directory, so clone the repository:

        $ cd
        $ git clone https://github.com/andisugandi/imflask.git

4. Change working directory to `imflask`:

        $ cd imflask

5. Create `.env` file:
        ```python
        FLASK_ENV="development"
        FLASK_APP="flaskweb.py"
        ```

6. Install Python modules required, and run the server:

        $ pip install -r requirements.txt
        $ run flask

7. Using web browser, go to `http://127.0.0.1:5000` and you'll see the application running.

## Demo
[![Imflask](https://img.youtube.com/vi/tvdV1UAr564/0.jpg)](https://www.youtube.com/watch?v=tvdV1UAr564)
