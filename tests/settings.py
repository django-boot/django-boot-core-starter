import os.path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = ["django_boot_core"]

DJANGO_BOOT = {"APPLICATION_CONFIGURATION": {"TYPE_ESTIMATE": False}}

MIDDLEWARE = []

USE_TZ = True
TIME_ZONE = "UTC"
SECRET_KEY = "foobar"
