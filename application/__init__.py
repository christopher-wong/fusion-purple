# -*- coding: utf-8 -*-
# !/usr/bin/python

import os

from flask import Flask

from .controller.about import about_bp
from .controller.index import index_bp
from .model.model import model_bp

import application.controller.about

app = Flask(__name__)
# allow clean page on each refresh
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# generate random secret key
app.secret_key = os.urandom(24)

# register blueprints
app.register_blueprint(about_bp)
app.register_blueprint(index_bp)
app.register_blueprint(model_bp)
