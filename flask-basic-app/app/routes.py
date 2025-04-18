from flask import Blueprint, render_template, request
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/addTask', methods=['POST'])
def add_task():
    task_name = request.form.get('title')
    description = request.form.get('description')
    deadline = request.form.get('deadline')

    task_data = {
        "title": task_name,
        "description": description,
        "deadline": deadline
    }

    with open('tasks.json', 'a') as json_file:  # 'a'モードで追記
        json.dump(task_data, json_file)
        json_file.write('\n')  # 各タスクを改行で区切る

    # print(f"タスクが保存されました: {task_data}")
    return render_template('base.html')