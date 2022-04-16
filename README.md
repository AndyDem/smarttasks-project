# SmartTasks taskmanager
# Features
## Every user can:
* Sign up, log in and log out
* Create, edit and delete tasks
* Get the list of personal tasks
* Get email notification about deadline
____
## To start project with Docker use:
```
docker-compose up -d --build
```
## To run tests in Docker:
```
docker-compose exec web python manage.py test
```
____
# ToDo
* Days left till deadline
* Make task.text limited by template
* Modal forms