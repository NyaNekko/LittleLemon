LITTLE LEMON RESTAURANT API - DJANGO REST FRAMEWORK

FEATURES
- Django serves a simple static HTML home page.
- Django REST Framework menu API with CRUD operations.
- Table booking API with CRUD operations.
- MySQL database configuration through environment variables.
- User registration and token authentication.
- Unit tests for menu and booking endpoints.
- Endpoints can be tested using Insomnia.

SETUP
1. Install Python 3.11 and MySQL Server.
2. Install Pipenv:
   python -m pip install pipenv
3. In this project folder, install packages:
   pipenv install
4. Copy .env.example to .env and enter your local MySQL credentials.
5. Create the database in MySQL, for example:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
6. Apply migrations:
   pipenv run python manage.py makemigrations restaurant
   pipenv run python manage.py migrate
7. Create an admin account if desired:
   pipenv run python manage.py createsuperuser
8. Start the development server:
   pipenv run python manage.py runserver
9. Open http://127.0.0.1:8000/

API PATHS TO TEST IN INSOMNIA
GET    http://127.0.0.1:8000/api/menu/
POST   http://127.0.0.1:8000/api/menu/             (authenticated)
GET    http://127.0.0.1:8000/api/menu/1/
PUT    http://127.0.0.1:8000/api/menu/1/           (authenticated)
PATCH  http://127.0.0.1:8000/api/menu/1/           (authenticated)
DELETE http://127.0.0.1:8000/api/menu/1/           (authenticated)

GET    http://127.0.0.1:8000/api/bookings/          (authenticated)
POST   http://127.0.0.1:8000/api/bookings/          (authenticated)
GET    http://127.0.0.1:8000/api/bookings/1/        (authenticated)
PUT    http://127.0.0.1:8000/api/bookings/1/        (authenticated)
PATCH  http://127.0.0.1:8000/api/bookings/1/        (authenticated)
DELETE http://127.0.0.1:8000/api/bookings/1/       (authenticated)

POST   http://127.0.0.1:8000/api/register/
POST   http://127.0.0.1:8000/api/token/login/
POST   http://127.0.0.1:8000/api/token/logout/
GET    http://127.0.0.1:8000/api-auth/login/        (Browsable API login)

AUTHENTICATION
1. POST /api/register/ with JSON:
   {"username":"tester","password":"StrongPass123!","email":"tester@example.com"}
2. POST /api/token/login/ with JSON:
   {"username":"tester","password":"StrongPass123!"}
3. Copy the returned token.
4. For protected endpoints, add this header:
   Authorization: Token YOUR_TOKEN_HERE

EXAMPLE MENU JSON
{
  "title": "Greek Salad",
  "price": "12.50",
  "inventory": 20
}

EXAMPLE BOOKING JSON
{
  "name": "Alex",
  "no_of_guests": 2,
  "booking_date": "2026-11-05T19:00:00Z"
}

RUN TESTS
pipenv run python manage.py test

GIT AND GITHUB
git init
git add .
git commit -m "Build Little Lemon Django REST API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main

NOTES
- Update .env with your own MySQL credentials. Do not commit .env.
- Use a unique username when registering.
- For production, set DJANGO_DEBUG=False and use a strong secret key.
