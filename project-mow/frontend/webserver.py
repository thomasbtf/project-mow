from flask import Flask, render_template
from flask_socketio import SocketIO


def start_webserver(robot, host="0.0.0.0", port=5000, debug=False):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret!"
    socketio = SocketIO(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    # The names message, json, connect and disconnect
    # are reserved and cannot be used for named events.
    @socketio.on("steering-command")
    def handle_steering_command(json):
        print("received data: " + str(json))
        robot.move(json.dx, json.dy)

    socketio.run(app, host=host, port=port, debug=debug)


if __name__ == "__main__":
    start_webserver(debug=True)
