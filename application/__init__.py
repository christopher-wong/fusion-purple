# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask, render_template, request, url_for, flash
import os

from .controller.about import about_bp
from .controller.form_controller import form_controller_bp
from .model.model import model_bp

app = Flask(__name__)
# allow clean page on each refresh
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# generate random secret key
app.secret_key = os.urandom(24)

# register blueprints
app.register_blueprint(about_bp)
app.register_blueprint(form_controller_bp)
app.register_blueprint(model_bp)
