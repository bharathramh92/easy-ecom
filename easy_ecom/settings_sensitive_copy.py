# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecom_db', #your db name
        'USER': 'ecom_admin', #your username
        'PASSWORD': 'admin', #your user password
        'HOST': 'localhost', #your host name
        'PORT': '', #your port number
    }
}

#Email settings
#we are using gmail for now
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_gmail_id'
EMAIL_HOST_PASSWORD = 'your_gmail_password'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True