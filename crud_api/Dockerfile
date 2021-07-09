# Base image is python
FROM python:3   
#Environment Variables
ENV PYTHONUNBUFFERED 1
#Working directory is 
WORKDIR /app
#adding all the files to app
ADD . /app
#We will copy the requirements. txt to the current folder with name requirements.txt
COPY ./requirements.txt /app/requirements.txt
#Then we will run the installation
RUN pip install -r requirements.txt
#we will copy the app
COPY . /app
