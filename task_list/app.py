from flask import Flask, render_template

from controllers.task_controller import task_blueprint

app = Flask(__name__)

# Register the blueprint with Flask app
app.register_blueprint(task_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
