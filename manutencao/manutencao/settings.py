"""
Django settings for manutencao project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ===========================================================
# SEGURANÇA
# ===========================================================

# Em produção, defina a variável de ambiente DJANGO_SECRET_KEY
# Nunca deixe a chave real no código-fonte.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-7ct53+5n^+8d#ch4@hn06#6s%_km4^4hadmwe2h3mj4x#%-bwe'
)

# Em produção, defina DEBUG=False via variável de ambiente
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts permitidos: separe múltiplos por vírgula na variável ALLOWED_HOSTS
# Ex: ALLOWED_HOSTS=meusite.render.com,meudominio.com.br
_allowed = os.environ.get('ALLOWED_HOSTS', '*')
ALLOWED_HOSTS = [h.strip() for h in _allowed.split(',') if h.strip()]


# ===========================================================
# APPS
# ===========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'manutencao_app',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # serve estáticos em produção
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'manutencao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'manutencao.wsgi.application'


# ===========================================================
# BANCO DE DADOS
# ===========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===========================================================
# VALIDAÇÃO DE SENHA
# ===========================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===========================================================
# INTERNACIONALIZAÇÃO
# ===========================================================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ===========================================================
# ARQUIVOS ESTÁTICOS
# ===========================================================

STATIC_URL = '/static/'

# Pasta onde o collectstatic vai juntar tudo (necessário em produção)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise: compressão e cache de arquivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ===========================================================
# CSRF / ORIGENS CONFIÁVEIS
# ===========================================================

# Adicione aqui a URL do seu serviço de deploy (Render, Railway, etc.)
# Ex: CSRF_TRUSTED_ORIGINS=https://meusite.onrender.com
_csrf = os.environ.get('CSRF_TRUSTED_ORIGINS', 'https://*.ngrok-free.dev')
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf.split(',') if o.strip()]


# ===========================================================
# AUTENTICAÇÃO
# ===========================================================

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'


# ===========================================================
# CHAVE PADRÃO DE CAMPO
# ===========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
