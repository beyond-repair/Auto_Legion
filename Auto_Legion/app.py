# Auto_Legion/app.py
from flask import Flask, render_template
from task_manager import TaskManager
from develop_tool.develop_tool import run_example

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    """
    Route for the home page.
    """
    print("Debugging: Inside index route")
    return render_template('index.html', agents=task_manager.ai_agents)

if __name__ == '__main__':
    print("Debugging: Before running app")
    run_example()  # Assuming this is the intended behavior

