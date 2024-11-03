from flask import Flask

application = Flask(__name__)


@application.route('/')
def home():  # put application's code here
    return '<h1>Hello World, I am changing from my local machine again </h1>'


if __name__ == '__main__':
    application.run()
