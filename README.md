# django-healthcare-backend
# Django Healthcare Backend

A REST API backend for managing healthcare data — users can register, log in, and manage patients and doctors.

## Features
- JWT Authentication
- CRUD APIs for Patients, Doctors, and Mappings
- PostgreSQL Integration

## Setup
Clone the repo
Create a virtual environment and install dependencies:
   
   pip install -r requirements.txt                                                             Create a .env file (refer .env.example)

Run migrations:

python manage.py makemigrations
python manage.py migrate


Run the server:

python manage.py runserver
