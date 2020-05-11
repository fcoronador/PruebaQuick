# PruebaQuick

El siguiente aplicativo basado en Django Rest, es el resultado de los requerimientos expuestos en la prueba.
Es necesario tener el lenguaje Python en su version 3.5, Django Rest Framework.

Para ejecutar el aplicativo:
 - $python3.5 manage.py runserver
Para ejecutar las migraciones
 - $python3.5 manage.py makemigrations prueba
 - $python3.5 manage.py migrate prueba
  
Python genera un servidor local en el puerto 8000 donde puede realizar las operaciones de POST, PUT, GET, DELETE.
Tambien el servidor recibe datos desde postman.
En el código se hace insercion de datos despues definidos los modelos.

Las urls de acceso son:
 - localhost:8000/clientes/ POST-GET
 - localgost:8000/clientes/{num}/ GET-PUT-DELETE
 - localhost:8000/facturas/ POST-GET
 - localgost:8000/facturas/{num}/ GET-PUT-DELETE
 - localhost:8000/productos/ POST-GET
 - localgost:8000/productos/{num}/ GET-PUT-DELETE

