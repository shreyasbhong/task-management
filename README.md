# task-management

****Instructions to Run the Application Locally

1. Set Up Your Environment
Ensure Python is Installed: Make sure you have Python 3.8 or later installed on your machine.
Install Django and Dependencies: You can install Django and other dependencies using pip.
pip install django djangorestframework djangorestframework-simplejwt django-filter
2.Apply Migrations
Create and apply database migrations:
 python manage.py makemigrations
 python manage.py migrate
3. Create a Superuser
To access the Django admin interface, create a superuser:
python manage.py createsuperuser
4. Run the Development Server
Start the Django development server:
python manage.py runserver
5. The server will typically run at http://127.0.0.1:8000/.
Accessing the Application
API Endpoints:
Tasks API: http://127.0.0.1:8000/api/tasks/
Register User: http://127.0.0.1:8000/api/register/
Login: http://127.0.0.1:8000/api/login/
Admin Interface: Access the admin interface at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.



Brief Write-Up on Approach and Assumptions
Approach:

Models: Defined a Task model with fields for status, priority, and due date, among others. Used Django’s built-in User model to associate tasks with users.
Serializers: Created serializers for user registration and task management to handle data validation and transformation between Django models and JSON.
Views: Implemented RegisterView for user registration and TaskViewSets for CRUD operations on tasks, using Django REST framework’s ModelViewSet. Added Home view for a simple authenticated endpoint.
Authentication: Used rest_framework_simplejwt for JWT-based authentication.
Filtering and Search: Applied Django Filter and SearchFilter for filtering and searching tasks.
Assumptions:

Development Environment: The instructions assume you have a development environment setup with Django and necessary packages installed.
Database: The default database setup (SQLite) is assumed. For production, you might use PostgreSQL or another database.
API Documentation Tools: Assumes the use of tools like Swagger or Postman for API documentation. The implementation of Swagger is included, and Postman is suggested for manual testing and sharing.
By following these instructions and understanding the provided approach, you should be able to set up, run, and document your Django application locally.
