# Dockerfile
FROM python:3.10

# Definir el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
