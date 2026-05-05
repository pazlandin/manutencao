#!/usr/bin/env bash
# Script de build executado pela plataforma de deploy (ex: Render)
set -o errexit

pip install -r requirements.txt

cd manutencao
python manage.py collectstatic --noinput
python manage.py migrate
