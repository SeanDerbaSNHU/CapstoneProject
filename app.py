# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)