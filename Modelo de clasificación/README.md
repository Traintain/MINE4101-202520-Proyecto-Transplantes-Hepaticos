# API para nuevas predicciones de complicaciones
Para desplegar el API donde se pueda consultar el modelo, siga estos pasos:
1. Instale Docker, en caso de no tenerlo instalado
2. Descargue los archivos presentes en esta carpeta
3. Cree una imagen de Docker
```
    docker build -t api:latest .
```
4. Ejecute el contenedor
```
    docker run -d -p 8000:8000 --restart always api
```
5. Compruebe que el contenedor está ejecutándose
```
    docker ps -a
```

6. Realize predicciones haciendo peticiones POST en el endpoint `/complicaciones`

Para consultar la documentación del enpoint acceda a:
```
    {{ip_de_despliegue}}/docs
```
con el motivo de la entrega, se realiza un despliegue en la siguiente URL http://3.17.69.69:8000/docs