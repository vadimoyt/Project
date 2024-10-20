from webbrowser import Error

from flask import Flask, render_template, request, url_for, redirect

from db import Database
from db_connection import DB_CONNECTION

db = Database(**DB_CONNECTION)

app = Flask(__name__)

@app.route('/')
def home_page():
    with db.get_cursor() as cursor:
        cursor.execute(
        'select * from tasks'
        )
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/sorted')
def sorted_by_category():
    selected_category = request.args.get('category')
    if selected_category:
        query = 'Select * from tasks where category = %s'
        with db.get_cursor() as cursor:
            cursor.execute(query, (selected_category,))
            tasks = cursor.fetchall()
    else:
        return home_page()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        try:
            selected_category = request.form.get('category')
            selected_title = request.form.get('title')
            selected_description = request.form.get('description')
            selected_status = request.form.get('status')
            selected_dead_line = request.form.get('dead_line')
            add_student = """
            insert into tasks (category, title, description, status, dead_line) 
            values (%s, %s, %s, %s, %s)
            """
            with db.get_cursor() as cursor:
                cursor.execute(add_student, (selected_category, selected_title, selected_description, selected_status, selected_dead_line))
            return redirect(url_for('success'))
        except Error as e:
            return f"Error, {e}"
    return render_template('add_task.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@app.route('/delete', methods=['POST'])
def delete_task():
    selected_task = request.form.get('task_id')
    delet_task = """
    delete from tasks
    where id = %s
    """
    with db.get_cursor() as cursor:
        cursor.execute(delet_task, (selected_task,))
    return redirect(url_for('home_page'))

@app.route('/task')
def open_task():
    selected_task = request.args.get('task_id')
    query = 'Select * from tasks where id = %s'
    with db.get_cursor() as cursor:
        cursor.execute(query, (selected_task,))
        task = cursor.fetchone()
    return render_template('task.html', task=task)

@app.route('/update_task', methods=['POST', 'GET'])
def update_task():
    if request.method == 'GET':
        selected_task = request.args.get('task_id')
        query = 'Select * from tasks where id = %s'
        with db.get_cursor() as cursor:
            cursor.execute(query, (selected_task,))
            task = cursor.fetchone()
        return render_template('update_task.html', task=task)
    else:
        task_id = request.form.get('id')
        field_name = request.form.get('field')
        new_value = request.form.get('new_value')
        query = 'Select * from tasks where id = %s'
        query_update = f"update tasks set {field_name} = %s where id = %s"
        with db.get_cursor() as cursor:
            cursor.execute(query_update, (new_value, task_id))
            cursor.execute(query, (task_id,))
            task = cursor.fetchone()
        return render_template('update_task.html', task=task)


@app.route('/update_task_field')
def update_task_field():
    field_name = request.args.get('field')
    task_id = request.args.get('id')
    return render_template('/update_task_field.html', field_name=field_name, id=task_id)




if __name__ == '__main__':
    app.run(debug=True, port=5001)
