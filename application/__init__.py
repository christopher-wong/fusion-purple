# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask, render_template, request, url_for, flash
import os

from .views.index import index_bp
from .views.about import about_bp

app = Flask(__name__)
# allow clean page on each refresh
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# generate random secret key
app.secret_key = os.urandom(24)

# register blueprints
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)
