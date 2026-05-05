#!/usr/bin/env bash
# Script de build executado pela plataforma de deploy (ex: Render)
set -o errexit
 
pip install -r requirements.txt
 
cd manutencao
python manage.py collectstatic --noinput
python manage.py migrate
 
# Cria o superusuário automaticamente se não existir
python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin123')
    print('Superusuário criado com sucesso!')
else:
    print('Superusuário já existe.')
EOF