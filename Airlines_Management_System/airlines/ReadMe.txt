REQUIREMENTS-------------------------------
asgiref==3.8.1
Django==5.1.3
djangorestframework==3.15.2
pytz==2024.2
sqlparse==0.5.2
Python 3.13.0
An SMTP service for sending emails (e.g., Gmail)

FOR ALL OF THE CODES BELOW FOR MAC/LINUX USE "python3" for WINDOWS USE "python"
FOR ALL OF THE CODES BELOW FOR MAC/LINUX USE "pip3" for WINDOWS USE "pip"

INSTALLATION-------------------------------
Create A folder Called "ABC"
Then past unzipped version of the project in that ABC folder.

Follow the steps below to set up and run the project locally.


1. Set Up a Virtual Environment in "ABC FOLDER"
IN ORDER TO USE PROJECT VIRTUAL ENVIRONMENT NEEDS TO REMAIN ACTIVATED.

Create and activate a virtual environment to isolate the project dependencies:
# For Linux/macOS
python3 -m venv myenv
source myenv/bin/activate
# For Windows
python -m venv myenv
myenv\Scripts\activate

2. Install Dependencies
Install the required packages using pip:
You can use SQLite for development, which requires minimal setup.

3. Migrate the Database
Run the migrations to set up your database schema:
python manage.py migrate
python manage.py makemigrations

4. Set Up Email Backend was provided you can use it. You might need to add certificate.
Moreover you can assign EMAIL_BACKEND as # django.core.mail.backends.console.EmailBackend
to view in terminal rather than sending email.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


5. Create a Superuser
To access the Django admin panel, create a superuser:
python manage.py createsuperuser
YOU CAN ASSIGN ENTITIES AT THERE ALSO


6. Run the Development Server
Start the Django development server:
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to access the application.

URLS and POSTMAN_COLLECTION was provided. At POSTMAN request names were name according to function
of the request. Therefore, there won't be any confusion. 


