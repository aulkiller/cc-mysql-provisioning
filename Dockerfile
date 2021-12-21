# Use Python38
FROM python:3.8-slim-buster
# Copy requirements.txt to the docker image and install packages
COPY . /
RUN pip install -r requirements.txt
# Expose port 32111
EXPOSE 32111
ENV PORT 32111
# Run Code
RUN python Service.py &
RUN python container_model.py