# import Flask and render_template
from flask import Flask, render_template
from repositories import task_repository

# import Blueprint class from flask
from flask import Blueprint

# creat a new instance of Blurprint called 'tasks'
task_blueprint = Blueprint("tasks", __name__)

# Declare a route for the list of tasks

# INDEX
# GET '/tasks'
@task_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks=tasks)


# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'
