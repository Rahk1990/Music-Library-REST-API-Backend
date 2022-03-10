
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uc02a4e@*a9g=w83-x01!2_i4t+s8&p&ak8ih*^l($frg49juw'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'songs_database',
        'HOST': 'local_host',
        'USER': 'root',
        'PASSWORD': '199028'
    }
}
