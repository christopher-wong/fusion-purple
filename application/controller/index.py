# -*- coding: utf-8 -*-
# !/usr/bin/python

from flask import Flask, render_template, request, Blueprint, redirect, flash

index_bp = Blueprint('index_controller', __name__)

# Controller

@index_bp.route('/')
def index():
    return redirect('/home')


@index_bp.route('/home')
def home():
    return render_template('index.html')


@index_bp.route('/submit', methods=['POST'])
def submit():
    # get inputs from form as dict
    if request.method == 'POST':
        formInputs = request.form.to_dict()
        flash("Form inputs sucessfully submitted")
        flash(formInputs)

    return render_template('index.html',
                           formInputs=formInputs)
