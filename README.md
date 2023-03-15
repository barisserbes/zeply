# zeply
To run the project, new python virtual environment is recommended than
1. pip install requirements.txt
2. python manage.py migrate (for creating tables but i pushed the one I used so you can use my sqlite dbase for test purposes)
3. python manage.py runserver (to start app)

Endpoints:
admin/    (default django admin panel) 

create-btc-address/

btc-address/

btc-address/<int:pk>/

create-eth-address/

eth-address/

eth-address/<int:pk>/

I would normally use PostgreSQL for the project for demonstration purposes I used SQLite
I used encryption for security purposes.
