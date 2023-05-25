# Django Rest Framework drone assessment

## Steps/Commands

1) Virtual Environment - Open a terminal and use the following command to create a virtual environment. 
```
python -m venv venv
```
Now activate the virtual environment with the following command.
```
# windows machine
venv\Scripts\activate.bat

#mac/linux
source venv/bin/activate
```
You will know your virtual environment is active when your terminal displays the following:
```
(venv) path\to\project\drf_course>
```

2) Packages and requirements -
Let's go ahead and install our project requirements. Add the following code to you terminal.

```
pip install -r backend/requirements.txt
```

3) Database and Migrations
```
python manage.py makemigrations drone
python manage.py makemigrations medication

python manage.py migrate

```

4) Run the server
python manage.py runserver

5) run these commands to start the dependency on celery 
celery -A drone_assessment beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery -A drone_assessment worker --loglevel=info 

6) start your redis server