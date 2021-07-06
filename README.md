# Hashing-API
A simple API to hash any provided JSON snippet built using Django Rest Framework, Hashlib and Bcrypt. 

### Endpoints :
http://localhost:8000/hash/create <br>
Method: POST <br>
Headers: 
* Content-Type: application/json <br>

Body: Any valid JSON Object

### Execution guide:
Create a virtual environment <br>
Pip install the following dependencies: 
```
Django, Django cors headers , Django rest framework, bcrypt
```
After installation of the dependencies, run the following command to run the server:
```
py manage.py runserver
```
