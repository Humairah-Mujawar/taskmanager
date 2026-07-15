# taskmanager
Python - Task Manager

•	Task Manager, using Python with Django and Django Rest Framework (DRF)

## Steps to Run
1. Download project
2. Go to project folder, and then subfolder "taskmanager". In settings.py, make two changes as below and save:<br/>
  i. Uncomment line with code
   ```
    ALLOWED_HOSTS = []
   ```
   ii. Comment line with code
   ```
   ALLOWED_HOSTS = ['web-production-4af5b.up.railway.app']
   ```
3. Open Terminal and navigate to project path
4. Type command ``` python manage.py runserver```
5. In the localhost URL tab inside the browser, append "/tasks" and press ENTER. <br/>
   For example:
   ``` http://127.0.0.1:8000/tasks/ ```
