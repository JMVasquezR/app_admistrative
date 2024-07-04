FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo requirements.txt al contenedor
COPY requirements/requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . /app/

RUN mkdir -p /app/static
RUN mkdir -p /app/media

# Recopila los archivos estáticos
RUN python manage.py collectstatic --noinput

# Ejecuta las migraciones y crea el usuario superadmin
COPY init/init.sh /app/
RUN chmod +x /app/init/init.sh

CMD ["/app/init/init.sh"]

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app_administrative.wsgi:application"]
