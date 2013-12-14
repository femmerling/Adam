# Update Note

This is stil being developed. Expect a ready product in about a week or so.

# Description

Adam is a boilerplate framework for developing python web applications. The underlying web framework is Flask, a python microframework based on werkzeug, jinja2 and good intentions. Adam is highly inspired by EmeraldBox and Backyard and Adam itself is a combination of both framework so you can have a speedy fullstack development
or API development all in a single framework.

# Motivation

Developing web apps should be done in the easiest and most efficient ways.
After developing EmeraldBox, which is a fullstack framework, and backyard, which is a framework to generate backend APIs, it is nice to have a framework that can handle both. Thus, Adam is written.

# Installer package

To run Adam, you need python 2.5 and above. However, Python 3 is not yet supported. Ideally, use Python 2.7.

Adam utilizes virtualenv in a rather different way. It will build the environment but you don't have to activate it. Keep reading to see why :)

# Setup
You can get Adam using two ways:
* Get the stable version from http://adam.emfeld.com
* Get the bleeding edge version by cloning this repo. 

    git clone https://github.com/femmerling/Adam.git <project_name>

To get started with Adam, use terminal and go to the Adam root folder and run:

    python setup.py

The setup will then automatically download dependencies and adjust your settings.

If you clone from git and want to control your project using git do the followings:

change to directory of <project_name>

    cd <project_name>

add replace remote

    git remote rm origin
    git remote add origin <new_remote like git@github.com:your_name/project_name.git>
    git commit -am "initial setup"
    git push origin master

# Server and Deployment

As all python frameworks, Adam is dependent on WSGI. Worry not! Adam comes with the not 1 but 2 WSGI standalone server.

Just like EmeraldBox, Adam comes with Tornado and Gunicorn in the box. 

# Usage

This section will be updated, but most likely it will follow a pattern similar to that of EmeraldBox and Backyard.

# Other Notes

No documentation is available for now, this repo is your friend for now.

for documentation on python see http://www.python.org <br>
for documentation on Flask see http://flask.pocoo.org <br>
for documentation on SQLAlchemy see http://www.sqlalchemy.org <br>

# Getting Help

Leave an issue here or email the author directly at erich@emfeld.com

# Contributing

If you found any issues please put them in the issue section.

To contribute, simply fork the repo, create a branch and place a pull request.

# Ending Note

This framework adds the diversity in python, a language which have more web frameworks than keywords.
Thank you for trying it out and all suggestions are welcome.