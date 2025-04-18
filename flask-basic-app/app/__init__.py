from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/submit_goal', methods=['POST'])
def submit_goal():
    goal = request.form.get('goal')
    description = request.form.get('description')
    deadline = request.form.get('deadline')
    # ここでデータを処理する（例: データベースに保存）
    return f"目標: {goal}, 説明: {description}, 期限: {deadline}"

if __name__ == '__main__':
    app.run(debug=True)