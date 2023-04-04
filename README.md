# Image-Recognizer
The final project of the course Python for Data Science, on the Web framework - Django.

With this application, you will be able to make a prediction of the uploaded picture using the trained cifar10 and cifar100 datasets, as well as the integrated chatGPT will help you find answers to questions about neural networks from the book "Deep Learning in Python" by FRANÇOIS CHOLLET.


## Table of contents:
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info:
**Image-Recognizer** - it performs the following functions:
* **[cifar10](https://telegra.ph/Sifar10-03-28)** - Identifies images in pictures and makes predictions for them based on the 10 image classes that have been trained.
* **cifar100** - Identifies images in pictures and makes predictions for them based on the 100 image classes that have been trained.
* **chatGPT** - will help you find answers to questions about neural networks from the book "Deep Learning in Python" by FRANÇOIS CHOLLET. The author hopes that this book will be useful to you and help you start creating intelligent applications and solving problems that are important to you.


## Technologies:
Project is mainly based on:
* Web framework: Django
* Frontend: HTML/CSS, Tailwind.css, Node.js
* Backend: python, JavaScript, Google Colab, Anaconda, Tensorflow, Keras, Numpy


## Setup:
* The first thing to do is download [Node.js](https://nodejs.org/en/download) and install it:

* The second thing to do is to clone the repository:

```sh
$ git clone git@github.com:maracasabat/Image-Recognizer.git
```

* Activate virtual environment and install dependencies:

```sh
$ pipenv  shell
(env)$ pipenv  install
```

* Once `pipenv` has finished downloading the dependencies:


* Create .env file in project root and fill in the file like this example:
```sh
SECRET_KEY=secret_key
ALLOWED_HOSTS=*

POSTGRES_DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432

OPENAI_API_KEY=OPENAI_API_KEY
```

* If you want to use Cloudinary add next steps:
```sh
CLOUD_NAME=cloudinary_NAME
API_KEY=cloudinary_KEY
API_SECRET=cloudinary_SECRET
```
* Or you can choose local storage on file settings.py


```sh
if you use Windows choose next option on file settings.py:
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd" # Windows
else:
    NPM_BIN_PATH = '/usr/local/bin/npm'  # MacOS
```   
    
```sh
First terminal:
(env)$ cd recognizer
(env)$ python manage.py migrate
(env)$ python manage.py tailwind install
(env)$ python manage.py tailwind build
(env)$ python manage.py tailwind start
```

```sh
Second terminal:
(env)$ cd recognizer
(env)$ python manage.py runserver     
```
* And navigate to `http://127.0.0.1:8000/.

## Docker setup

1. Build containers via `docker-compose`:

    ```bash
    docker-compose build
    ```

2. Start containers:

    ```bash
    docker-compose up
    ```

3. Open `http://localhost:8000` in a browser. You should see the main page.

    ```bash
    docker pull maracasabat/recognizer-project
    ```

    ```bash
    docker run -p 8000:8000 maracasabat/recognizer-project
    ```

    ```bash
    https://naai-project-maracasabat.koyeb.app/
    ```

* Links to the models:
  * **[cifar10](https://drive.google.com/file/d/1-oVU8YGdNXper8XTQCKj5Up67q0PTPFA/view?usp=sharing)**
  * **[cifar100](https://drive.google.com/file/d/1wGkwfOPPQQFDv-Ka8SpX1pJcwo-ks8yx/view?usp=sharing)**

If there are any problems with the models, they can be downloaded from Google Disk and added to `mediauploadapp
/model/` folder.


