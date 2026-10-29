# Little Lemon Restaurant API

A restaurant management REST API built with **Django**, **Django REST Framework (DRF)**, and **MySQL**. The project provides menu management, table booking CRUD operations, user registration, token authentication, and API testing support with Insomnia.

## Features

- Django serves a static HTML homepage.
- Menu API with create, read, update, and delete (CRUD) operations.
- Table booking API with CRUD operations.
- User registration and token-based authentication.
- MySQL database integration.
- Django REST Framework browsable API.
- Unit tests for menu, booking, registration, and authentication behavior.
- API endpoints documented for testing with Insomnia.

## Technology Stack

- Python 3.11
- Django
- Django REST Framework
- MySQL
- Pipenv
- Insomnia (API testing)
- Git and GitHub

## Project Structure

```text
littlelemon_drf/
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── restaurant/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
├── templates/
│   └── index.html
├── .env.example
├── .gitignore
├── Pipfile
├── manage.py
└── README.md
```

## Prerequisites

Install the following before running the project:

- Python 3.11
- MySQL Server
- Pipenv
- Git (optional, for version control)
- Insomnia (optional, for API testing)

## Installation and Setup

### 1. Clone the repository

Replace the URL with your GitHub repository URL:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

If you downloaded the ZIP instead, extract it and open the project folder in VS Code.

### 2. Install Pipenv and project dependencies

```bash
python -m pip install pipenv
pipenv install
```

Activate the virtual environment if desired:

```bash
pipenv shell
```

### 3. Configure environment variables

Copy `.env.example` to a new file named `.env`, then update the values for your local MySQL setup.

Example:

```dotenv
DJANGO_SECRET_KEY=replace-with-a-long-random-secret
DJANGO_DEBUG=True
MYSQL_DATABASE=littlelemon
MYSQL_USER=littlelemon_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

**Do not commit `.env` or real credentials to GitHub.**

### 4. Create the MySQL database

Log in to MySQL and create the database:

```sql
CREATE DATABASE littlelemon
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Make sure the MySQL user specified in `.env` has permission to access this database. Use your own local MySQL username and password if you already have a configured user.

### 5. Apply migrations

```bash
pipenv run python manage.py makemigrations restaurant
pipenv run python manage.py migrate
```

### 6. Create an administrator (optional)

```bash
pipenv run python manage.py createsuperuser
```

### 7. Start the development server

```bash
pipenv run python manage.py runserver
```

Open these pages in your browser:

- Homepage: http://127.0.0.1:8000/
- Menu API: http://127.0.0.1:8000/api/menu/
- Bookings API: http://127.0.0.1:8000/api/bookings/
- Django admin: http://127.0.0.1:8000/admin/
- DRF browsable API login: http://127.0.0.1:8000/api-auth/login/

The bookings API requires authentication.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

### Menu API

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/api/menu/` | List menu items | Not required |
| POST | `/api/menu/` | Create a menu item | Required |
| GET | `/api/menu/1/` | Retrieve menu item with ID 1 | Not required |
| PUT | `/api/menu/1/` | Replace menu item with ID 1 | Required |
| PATCH | `/api/menu/1/` | Partially update menu item with ID 1 | Required |
| DELETE | `/api/menu/1/` | Delete menu item with ID 1 | Required |

Replace `1` with an existing menu item ID.

Example menu request body:

```json
{
  "title": "Greek Salad",
  "price": "12.50",
  "inventory": 20
}
```

### Table Booking API

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/api/bookings/` | List bookings belonging to the signed-in user | Required |
| POST | `/api/bookings/` | Create a booking | Required |
| GET | `/api/bookings/1/` | Retrieve a booking by ID, if it belongs to the signed-in user | Required |
| PUT | `/api/bookings/1/` | Replace a booking owned by the signed-in user | Required |
| PATCH | `/api/bookings/1/` | Partially update a booking owned by the signed-in user | Required |
| DELETE | `/api/bookings/1/` | Delete a booking owned by the signed-in user | Required |

Example booking request body:

```json
{
  "name": "Alex",
  "no_of_guests": 2,
  "booking_date": "2026-11-05T19:00:00Z"
}
```

Use a valid ISO 8601 date-time for `booking_date`.

### User Registration and Authentication

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/api/register/` | Register a new user | Not required |
| POST | `/api/token/login/` | Obtain an authentication token | Not required |
| POST | `/api/token/logout/` | Invalidate the user's token | Required |

Registration request:

```json
{
  "username": "tester",
  "email": "tester@example.com",
  "password": "StrongPass123!"
}
```

Login request:

```json
{
  "username": "tester",
  "password": "StrongPass123!"
}
```

The login response includes a token. For protected endpoints, include this HTTP header:

```http
Authorization: Token YOUR_TOKEN_HERE
```

Logout request: send a `POST` request to `/api/token/logout/` with the token header.

## Testing with Insomnia

1. Start the Django development server.
2. Create a user using `POST /api/register/`.
3. Log in using `POST /api/token/login/` and copy the returned token.
4. For protected endpoints, set the authentication header to `Authorization: Token YOUR_TOKEN_HERE`.
5. Test menu and booking endpoints using `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
6. Use the JSON request examples above as a starting point.

## Run Unit Tests

Run the test suite with:

```bash
pipenv run python manage.py test
```

The tests cover menu listing and creation, booking creation and listing, authentication requirements, and user registration.

## GitHub Submission

If Git has not been initialized in the project folder, run:

```bash
git init
git add .
git commit -m "Build Little Lemon Django REST API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

If the repository already exists, commit and push your latest changes:

```bash
git add README.md
git commit -m "Add project README and API endpoint documentation"
git push
```

Replace the example GitHub URL with your own repository URL. Ensure `README.md` is committed and pushed before submitting your project for peer review.

## Notes

- MySQL credentials differ between development machines. Update `.env` for your local database.
- The `.env` file should remain private and should not be pushed to GitHub.
- The booking API is restricted to the authenticated user's own bookings.
- This project is intended for local development and coursework. Before production deployment, configure a secure secret key, disable debug mode, configure allowed hosts, and review deployment security settings.
