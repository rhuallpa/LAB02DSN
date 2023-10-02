# Usar una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo en /app
WORKDIR /LAB05-NUBE-H

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /app/

# Instalar las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual al directorio de trabajo
COPY . /LAB05-NUBE-H/


RUN git clone https://github.com/rhuallpa/LAB05-NUBE-H.git

# Exponer el puerto 9000 para la aplicación Django
EXPOSE 9000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
