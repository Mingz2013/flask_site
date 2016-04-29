__author__ = 'zhaojm'

from flask import Blueprint, render_template

index_controller = Blueprint('index_controller', __name__, url_prefix='/')

@index_controller.route('/')
def index():
    return render_template('index/index.html')
    pass