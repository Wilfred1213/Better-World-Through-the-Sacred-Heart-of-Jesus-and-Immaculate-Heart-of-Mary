# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a real secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['bwtsjhihm.pacamara.dev','49.13.31.130']
# ALLOWED_HOSTS = ['*']

# This email settigns are for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =465
EMAIL_USE_SSL=True
EMAIL_USE_TLS = False
EMAIL_HOST_USER = 'mathiaswilfred7@gmail.com'
EMAIL_HOST_PASSWORD= 'rhno myrl okmw uarc'

# this one for development
# EMAIL_BACKEND = "EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"