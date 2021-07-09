What is this what I have to build?
# A course model, which will have basic data about the courses. It should be accessible via a rest API (CRUD).
* Name of the course
* Name of the author
* Date of the course
* Price of the course
* Users enrolled in this course
# A wishlist model, which will have a user and a course.  -
* User showing all data about the user
* Course showing all data about the course
# A user, who can be logged in using TokenAuthentication. This should also be a CRUD API.
The following features are desirables - 
* Register
* Login
* Forgot Password
* Forgot Email
---
# My solution contain:-
* GET, POST, DELETE methods all working properly for courses and wishlist.
* Properly presented JSON formatted data.
* Comments and Docstrings, explaining what your code does.
* Course and Wishlist endpoints showing all the relative data property formatted.
---

## Requirements - 
The following are the requirements for the project, which will be installed in the docker automatically while creating docker file -

* django
* djangorestframework
* danjo-allauth

---

## Docker - 
Dockerfile is created inside the repository which contains the steps to create a docker image.

Size of Docker image will be approx 962 MB.

To build the docker image from docker file - 
 * Download project and go to project directory.
 * To build the project in docker container.
    * docker-compose build.
 * Run following command in terminal to start the project in docker. 
    * docker-compose up

 * Docker image id-  78929293017d

## Running Django App - 
    * To use Rest api services(CRUD operation) for Course, open -
   http://127.0.0.1:8000/course/
    * To use Rest api services(CRUD operation) for Wishlist, open -
   http://127.0.0.1:8000/wishlist/
    * For authentication use-
   http://127.0.0.1:8000/accounts/login/
   http://127.0.0.1:8000/accounts/logout/
