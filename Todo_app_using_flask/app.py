from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

todo_list = []


# -------- LOAD TASKS --------
def load_tasks():
    global todo_list
    try:
        with open("tasks.json", "r") as file:
            todo_list = json.load(file)
    except:
        todo_list = []


# -------- SAVE TASKS --------
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(todo_list, file)


# -------- HOME PAGE --------
@app.route("/")
def index():
    load_tasks()
    return render_template("index.html", tasks=todo_list)


# -------- ADD TASK --------
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    category = request.form.get("category")

    todo_list.append({
        "task": task,
        "category": category,
        "Status": "Pending"
    })

    save_tasks()
    return redirect("/")


# -------- MARK COMPLETE --------
@app.route("/complete/<int:index>")
def complete_task(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["Status"] = "Completed"
        save_tasks()
    return redirect("/")


# -------- DELETE TASK --------
@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
        save_tasks()
    return redirect("/")


# -------- RUN APP --------
if __name__ == "__main__":
    app.run(debug=True)
