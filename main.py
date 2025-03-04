from flask import Flask, request
from service_layer import service, models

app = Flask(__name__)

app.register_blueprint(service.leave_request)


if __name__ == '__main__':
    app.run(debug=True)