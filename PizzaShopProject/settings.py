import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ze0w_rd@#yidljw0!q@y$e8fw-^3)op=j-ccb=jj1xe2!6+ve&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ 'ms-pizza-shop-app.herokuapp.com', 'localhost', '127.0.0.1' ]

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'PizzaShopApp',
	'bootstrap4',
	'rest_framework',
	'oauth2_provider',
	'social_django',
	'rest_framework_social_oauth2',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'PizzaShopProject.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [ os.path.join( BASE_DIR, 'templates' ) ]
		,
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.media',
				'social_django.context_processors.backends',
				'social_django.context_processors.login_redirect',
			],
		},
	},
]

WSGI_APPLICATION = 'PizzaShopProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join( BASE_DIR, 'db.sqlite3' ),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join( BASE_DIR, 'static' ),
)

STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )

LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
	'social_core.backends.facebook.FacebookOAuth2',
	'rest_framework_social_oauth2.backends.DjangoOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

# REST_FRAMEWORK = {
# 	'DEFAULT_AUTHENTICATION_CLASSES': (
# 		# 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
# 		'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
# 		'rest_framework_social_oauth2.authentication.SocialAuthentication',
# 	),
# }

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '498207460939686'
SOCIAL_AUTH_FACEBOOK_SECRET = '6080fa14405c89f2ecfd0e6053406c40'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = [ 'email' ]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
	'fields': 'id, name, email'
}

SOCIAL_AUTH_PIPELINE = (
	'social_core.pipeline.social_auth.social_details',
	'social_core.pipeline.social_auth.social_uid',
	'social_core.pipeline.social_auth.auth_allowed',
	'social_core.pipeline.social_auth.social_user',
	'social_core.pipeline.user.get_username',
	'social_core.pipeline.user.create_user',
	'PizzaShopApp.social_auth_pipeline.create_client',  # <--- set the path to the function
	'social_core.pipeline.social_auth.associate_user',
	'social_core.pipeline.social_auth.load_extra_data',
	'social_core.pipeline.user.user_details',
)

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
