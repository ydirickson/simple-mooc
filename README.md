# SIMPLE-MOOC
Simple MooC (Massive Open Online Course) made with Django Framework (Python backend) and PureCSS for CSS (Frontend)

## Inspiration

This project was created inpired at an online course at [Udemy](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario), from instructor Gileno Alves. The course is free, but only on Portuguese.

## Requirements

The following are required for this project:

* Python 3.6.x (3.5.x and 3.4.x should also work, but was not tested)
* Django 2.0.X (There are few modifications to work with 1.11.X)
* PureCSS ?

## Running

The project is redy for running locally or in the cloud at [Heroku](https://heroku.com)

### Run Locally

To run the project on your local PC, you have to install the requirements and use the local server.

1. Clone the repository:
```
git clone https://github.com/ydirickson/simple-mooc.git
cd simple-mooc
```

2. Install Python Virtual Environment:
```
pip install virtualenv
```

3. Prepare the virtual environment:
```
virtualent venv
```

4. Activate the virtual environment:
```
(Windows)
venv\Scripts\activate
(Unix)
venv/bin/activate
```

5. Install the requirements:
```
pip install -r requirements.txt
```

6. Run local server:
```
python manage.py runserver
```

7. Navigate to http://localhost:8000 on the browser


### Deploy to Heroku

## Errors, problemas and contributions

## Credits

Thanks for @gileno for it's wonderfull Django courses at [Udemy](https://udemy.com)
