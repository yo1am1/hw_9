# hw_9
## Installation guide

1. Mirror the project:
   * ``git clone --bare https://github.com/yo1am1/hw_9.git``
2. Install the requirements:
   * ``pip install -r requirements.txt``
3. Run in terminal:
   * ``python manage.py makemigrations``
   * ``python manage.py migrate``
4. Run this project with command:
   * ``TWILIO_TOKEN={YOUR_TOKEN} python manage.py runserver``
   , where {YOUR_TOKEN} is your private Twilio token
5. Input in terminal to run Celery:
   * ``celery -A hw_9  worker -l INFO``
