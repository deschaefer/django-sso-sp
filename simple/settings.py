"""
Django settings for simple project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import sys
from os import path
from pathlib import Path

import saml2
# from saml2.saml import NAME_FORMAT_URI
from saml2.saml import NAMEID_FORMAT_TRANSIENT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-g&eazwg*kxnlg$zd2brj!45w71jgen8#r995h(4g)y@a)12u^z"  # noqa: E501

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "djangosaml2",  # new application
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "djangosaml2.middleware.SamlSessionMiddleware",
]

ROOT_URLCONF = "simple.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "simple.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_USER_MODEL = "accounts.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(levelname)s %(asctime)s %(module)s: %(message)s"},  # noqa: E501
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": sys.stdout,
        },
    },
    "loggers": {
        "saml2": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# djangosaml - https://djangosaml2.readthedocs.io/contents/setup.html#prepare-environment-and-install-requirements  # noqa: E501
SAML_SESSION_COOKIE_NAME = "saml_session"
SESSION_COOKIE_SECURE = True
LOGIN_URL = "/saml2/login/"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "djangosaml2.backends.Saml2Backend",
)

BASEDIR = path.dirname(path.abspath(__file__))

SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'email'
SAML_CREATE_UNKNOWN_USER = True

# saml - key django - value
SAML_ATTRIBUTE_MAPPING = {
    "subject": ("username",),
    "email": ("email",),
    "first_name": ("first_name",),
    "last_name": ("last_name",),
}

SAML_CONFIG = {
    # full path to the xmlsec1 binary programm
    "xmlsec_binary": "/usr/local/bin/xmlsec1",
    # your entity id, usually your subdomain plus the url to the metadata view
    "entityid": "http://staging.anodyneclinical.com/saml2/metadata/",
    # directory with attribute mapping
    "attribute_map_dir": path.join(BASEDIR, "attribute-maps"),
    # Permits to have attributes not configured in attribute-mappings
    # otherwise...without OID will be rejected
    "allow_unknown_attributes": True,
    # this block states what services we provide
    "service": {
        # we are just a lonely SP
        "sp": {
            "name": "Anodyne Clinical",
            "name_id_format": NAMEID_FORMAT_TRANSIENT,
            # For Okta add signed logout requests. Enable this:
            # "logout_requests_signed": True,
            "endpoints": {
                # url and binding to the assertion consumer service view
                # do not change the binding or service name
                "assertion_consumer_service": [
                    ("http://localhost:8000/saml2/acs/", saml2.BINDING_HTTP_POST),  # noqa: E501
                ],
                # url and binding to the single logout service view
                # do not change the binding or service name
                "single_logout_service": [
                    # Disable next two lines for HTTP_REDIRECT for IDP's that only support HTTP_POST. Ex. Okta:  # noqa: E501
                    # ('http://localhost:8000/saml2/ls/',
                    #  saml2.BINDING_HTTP_REDIRECT),
                    ("http://localhost:8000/saml2/ls/post", saml2.BINDING_HTTP_POST),  # noqa: E501
                ],
            },
            "signing_algorithm": saml2.xmldsig.SIG_RSA_SHA256,
            "digest_algorithm": saml2.xmldsig.DIGEST_SHA256,
            # Mandates that the identity provider MUST authenticate the
            # presenter directly rather than rely on a previous security context.   # noqa: E501
            "force_authn": False,
            # Enable AllowCreate in NameIDPolicy.
            "name_id_format_allow_create": False,
            # attributes that this project need to identify a user
            "required_attributes": [
                "subject",
                "practiceID",
                "departmentID",
                "usertype",
            ],
            # attributes that may be useful to have but not required
            "optional_attributes": [
                "email",
                "firstName",
                "lastName",
                "fullName",
                "patient_id",
                "position",
                "extraidentifier",
            ],
            "want_response_signed": True,
            "authn_requests_signed": True,
            "logout_requests_signed": True,
            # Indicates that Authentication Responses to this SP must
            # be signed. If set to True, the SP will not consume
            # any SAML Responses that are not signed.
            "want_assertions_signed": True,
            "only_use_keys_in_metadata": True,
            # When set to true, the SP will consume unsolicited SAML
            # Responses, i.e. SAML Responses for which it has not sent
            # a respective SAML Authentication Request.
            "allow_unsolicited": False,
            # # in this section the list of IdPs we talk to are defined
            # # This is not mandatory! All the IdP available in the metadata will be considered instead.  # noqa: E501
            # 'idp': {
            #     # we do not need a WAYF service since there is
            #     # only an IdP defined here. This IdP should be
            #     # present in our metadata
            #
            #     # the keys of this dictionary are entity ids
            #     'https://localhost/simplesaml/saml2/idp/metadata.php': {
            #         'single_sign_on_service': {
            #             saml2.BINDING_HTTP_REDIRECT: 'https://localhost/simplesaml/saml2/idp/SSOService.php',  # noqa: E501
            #             },
            #         'single_logout_service': {
            #             saml2.BINDING_HTTP_REDIRECT: 'https://localhost/simplesaml/saml2/idp/SingleLogoutService.php',  # noqa: E501
            #             },
            #         },
            #     },
        },
    },
    # where the remote metadata is stored, local, remote or mdq server.
    # One metadatastore or many ...
    "metadata": {
        "local": [path.join(BASEDIR, "remote_metadata.xml")],
        # 'remote': [{"url": "https://idp.testunical.it/idp/shibboleth"},],
        # 'mdq': [{"url": "https://ds.testunical.it",
        #          "cert": "certficates/others/ds.testunical.it.cert",
        #         }]
    },
    # set to 1 to output debugging information
    "debug": 1,
    # Signing
    "key_file": path.join(BASEDIR, "private.key"),  # private part
    "cert_file": path.join(BASEDIR, "public.cert"),  # public part
    # Encryption
    "encryption_keypairs": [
        {
            "key_file": path.join(BASEDIR, "private.key"),  # private part
            "cert_file": path.join(BASEDIR, "public.cert"),  # public part
        }
    ],
    # own metadata settings
    "contact_person": [
        {
            "given_name": "Joseph",
            "sur_name": "DiPoala",
            "company": "Anodyne Clinical",
            "email_address": "jdipoala@anodyneclinical.com",
            "contact_type": "owner",
        },
    ],
    # you can set multilanguage information here
    "organization": {
        "name": [("Anodyne Clinical", "es"), ("Anodyne Clinical", "en")],
        "display_name": [("Anodyne Clinical", "es"), ("Anodyne Clinical", "en")],  # noqa: E501
        "url": [
            ("https://www.anodyneclinical.com", "es"),
            ("https://www.anodyneclinical.com", "en"),
        ],
    },
}
