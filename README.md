# App Administrative

Este proyecto es una aplicación web construida con Django, utilizando PostgreSQL como base de datos, y Nginx como
servidor web en un entorno Dockerizado.

## Requisitos

- Docker
- Docker Compose

## Instalación

Sigue estos pasos para configurar y ejecutar la aplicación:

### 1. Clona el repositorio y la imagen

```sh
https://github.com/JMVasquezR/app_admistrative.git
docker pull mvasquezr/app_administrative
```

### 2. Construir y ejecutar los contenedores Docker

```sh
docker-compose up --build
```

### 3. Migrar la base de datos

Abre otra terminal y ejecuta las migraciones de Django:

```sh
docker-compose run --rm migrate
```

### 4. Crear un usuario superadmin

```sh
docker-compose run --rm migrate python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Acceso a la aplicación

Una vez que todos los contenedores estén en ejecución, puedes acceder a la aplicación desde tu navegador web:

URL: http://localhost/
Usuario: <usuario_que_creaste>
Contraseña: <la_contraseña_que_creaste>

### Detener y limpiar
Para detener los contenedores y limpiar los recursos:

```sh
docker-compose down -v
```

Esto detendrá y eliminará los contenedores, junto con los volúmenes asociados.

¡Disfruta usando la aplicación administrativa!