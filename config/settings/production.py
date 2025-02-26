from .base import *

ALLOWED_HOSTS = [
    "api.example.com",
    "admin.example.com",
    "localhost",
    "127.0.0.1",
    "server's ip must be"
]

CSRF_TRUSTED_ORIGINS = ["https://api.example.com", "https://admin.example.com"]
CORS_ALLOWED_ORIGINS = ["https://api.example.com", "https://admin.example.com"]

DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_ALLOW_ALL = False

REST_FRAMEWORK.update(
    {'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderer.JSONRenderer',)}
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT')
    }
}