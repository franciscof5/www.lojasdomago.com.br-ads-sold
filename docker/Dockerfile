# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
#COPY ../backend /code/
#COPY requirements.txt /code/

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
#COPY . ../backend
#WORKDIR /backend
COPY . /code/

#COPY ../backend /code/

#EXPOSE 9000

# runs the production server
#ENTRYPOINT ["python", "backend/manage.py"]
#CMD ["runserver", "0.0.0.0:9000"]