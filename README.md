# Sweeft-Acceleration-Program-Python-Web-Task
Making Science Sweeft Python Web task

1. Install all the dependencies from the requirements.txt file by running the following docker command: `docker-compose up -d --build`

In case to start the project you have to migrate with the following command:
`docker-compose exec web python manage.py migrate`

Finally you can start the project by running the following command: `docker-compose up` or `docker-compose up -d` - for detached mode.

Go to following urls to test the api with: "http://localhost:8000/swagger/" or "http://localhost:8000/redoc/"

For authentication JWT Token is implemented.
There are predefined exercises in the database. User can create their personal workout plan with this exercises.


