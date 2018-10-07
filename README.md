versions installed are
-----------------------

python==3.6.0
Django==1.9
djangorestframework==3.7.0 [if you use djangorestframework==3.8 in this project it will give error]
PyMySQL==0.9.2 [pip install pymysql]


mysql version 5.0.27
or we can use default sqlite3 also instead of mysql -- go to settings.py file and configure DATABASE to sqlite3


go to cmd prompt, to the path where manage.py file is located and run the below commands
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser    [give username email password]
py manage.py runserver		[ copy http://127.0.0.1:8000 ]

run the url with ending with /feedback to get feedback form
http://127.0.0.1:8000/feedback/

run the url with ending with /api to get json format
http://127.0.0.1:8000/api/

to login into the admin site 
http://127.0.0.1:8000/admin/   [use username and password given in the createsuperuser command]
