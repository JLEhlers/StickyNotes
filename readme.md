Sticky Notes Django Application

This is a Django web application project that includes one main app:

notes: Allows users to create, view, edit, and delete sticky notes.
Installation and Setup
1. Clone the repository

Clone the project from GitHub and open the project folder:

cd sticky_notes
2. Create a virtual environment

Create a virtual environment using:

python -m venv myenv

Activate the virtual environment on Windows PowerShell:

.\myenv\Scripts\Activate.ps1
3. Install dependencies

Install the required Python packages:

pip install -r requirements.txt

If a requirements.txt file is not available, install Django with:

pip install django
4. Run database migrations

Create the database migrations:

python manage.py makemigrations

Apply the migrations:

python manage.py migrate
5. Create a superuser

Create a Django administrator account:

python manage.py createsuperuser

Follow the instructions and enter a username, email address, and password.

6. Start the development server

Start the Django development server:

python manage.py runserver

Open the application in a web browser at:

http://127.0.0.1:8000/

The Django Admin panel can be accessed at:

http://127.0.0.1:8000/admin/

Log in to the Admin panel using the superuser account created earlier.

7. Run the tests

To run all tests for the project:

python manage.py test
