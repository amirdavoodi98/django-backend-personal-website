from pathlib import Path

import environ

# Initialize environment variables
env = environ.Env()

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load the `.env` file dynamically based on ENVIRONMENT
ENVIRONMENT = env.str("ENVIRONMENT", default="local")

# Determine which .env file to load
ENV_FILE = BASE_DIR / "envs" / f".env.{ENVIRONMENT}"

# Load the environment file if it exists
if ENV_FILE.exists():
    environ.Env.read_env(str(ENV_FILE))
    print(f"Loaded environment: {ENVIRONMENT} from {ENV_FILE}")

# Docker-specific settings
DOCKER_ENABLED = env.bool("DOCKER_ENABLED", default=False)

# Service Configuration
SERVICE_VERSION = env.str("SERVICE_VERSION", default="1.0.0")

# Add cors settings
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=False)

# Application Definition
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    # Local apps
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

HEALTH_CHECKS = [
    "health_check.plugins.db.DatabaseHealthCheck",  # Checks database connectivity
    "health_check.plugins.cache.CacheHealthCheck",  # Checks cache
    "health_check.plugins.storage.StorageHealthCheck",  # Checks file storage
]

ROOT_URLCONF = "configs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "configs.wsgi.application"

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static & Media Files
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default Primary Key Field Type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Add Redis configuration
REDIS_URL = env.str("REDIS_URL", default="redis://redis:6379/0")

# Update REST_FRAMEWORK settings
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

# Base Spectacular Settings
SPECTACULAR_SETTINGS = {
    "TITLE": "A",
    "DESCRIPTION": "A",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/v1",
}

# Database Configuration
DATABASES = {"default": env.db()}

# Ensure database connections are properly handled
CONN_MAX_AGE = env.int("CONN_MAX_AGE", 60)
