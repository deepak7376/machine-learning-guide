Let's create a more complex application using Redis, Flask, and Docker Compose. In this example, we'll build a simple task management application with the ability to add, list, and mark tasks as completed. We'll use Redis to store the task data.

1. **Create the Directory Structure**:

   Start by creating a directory for your project:

   ```bash
   mkdir redis-flask-tasks
   cd redis-flask-tasks
   ```

2. **Create a Python Flask Application**:

   Create a Python Flask application to manage tasks. Create a file named `app.py`:

   ```python
   # app.py
   from flask import Flask, request, render_template, redirect
   import redis

   app = Flask(__name__)
   redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

   @app.route('/')
   def list_tasks():
       tasks = [task.decode('utf-8') for task in redis_client.lrange('tasks', 0, -1)]
       return render_template('tasks.html', tasks=tasks)

   @app.route('/add', methods=['POST'])
   def add_task():
       task = request.form.get('task')
       redis_client.rpush('tasks', task)
       return redirect('/')

   @app.route('/complete/<int:index>')
   def complete_task(index):
       redis_client.lset('tasks', index, 'COMPLETED')
       return redirect('/')

   if __name__ == '__main__':
       app.run(host='0.0.0.0', debug=True)
   ```

3. **Create an HTML Template for Tasks**:

   Create a directory named `templates` and create an HTML file named `tasks.html`:

   ```html
   <!-- templates/tasks.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Task List</title>
   </head>
   <body>
       <h1>Task List</h1>
       <ul>
           {% for task in tasks %}
               <li>
                   {% if task != 'COMPLETED' %}
                       {{ task }}
                       <a href="/complete/{{ loop.index0 }}">[Complete]</a>
                   {% else %}
                       <del>Task completed</del>
                   {% endif %}
               </li>
           {% endfor %}
       </ul>
       <form method="post" action="/add">
           <label for="task">Add Task:</label>
           <input type="text" id="task" name="task" required>
           <input type="submit" value="Add Task">
       </form>
   </body>
   </html>
   ```

4. **Create a Dockerfile for the Web Application**:

   Create a `Dockerfile` for the web application:

   ```Dockerfile
   # Dockerfile
   FROM python:3.8

   WORKDIR /app
   COPY requirements.txt /app
   RUN pip install -r requirements.txt
   COPY . /app

   CMD ["python", "app.py"]
   ```

5. **Create a `requirements.txt` File**:

   Create a `requirements.txt` file in the same directory:

   ```plaintext
   Flask==2.0.1
   redis==3.7.0
   ```

6. **Create a Docker Compose Configuration**:

   Create a `docker-compose.yml` file to define the services and dependencies:

   ```yaml
   version: '3'
   services:
     web:
       build: .
       ports:
         - "5000:5000"
       depends_on:
         - redis
     redis:
       image: "redis:alpine"
   ```

7. **Build and Run the Application**:

   Build and run the application using Docker Compose:

   ```bash
   docker-compose up -d
   ```

8. **Access the Application**:

   Open your web browser and navigate to `http://localhost:5000`. You can add tasks, mark them as completed, and see the list of tasks.

9. **Stop and Remove the Containers**:

   When you're done testing, stop and remove the containers using:

   ```bash
   docker-compose down
   ```

This example creates a more complex application with a web interface for managing tasks using Flask and Redis. It demonstrates the power of combining Flask, Redis, and Docker Compose for building multi-container applications.
