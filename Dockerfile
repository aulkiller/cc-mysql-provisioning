# Use Python38
FROM python:3.8-slim-buster
# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN apt-get update -y
RUN pip3 install -r requirements.txt
# Set the WORKDIR to be the folder
COPY . /app
# Expose port 32111
EXPOSE 32111
ENV PORT 32111
WORKDIR /app
# Use gunicorn as the entrypoint
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 0 deploy:app