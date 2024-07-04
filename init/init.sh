#!/bin/bash

# Ejecutar migraciones
python manage.py migrate

# Crear un usuario superadmin si no existe
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      User.objects.filter(username='admin').exists() or \
      User.objects.create_superuser('admin', 'admin@example.com', 'django20')" \
      | python manage.py shell

# Iniciar el servidor de desarrollo de Django
python manage.py runserver 0.0.0.0:8000
