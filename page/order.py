from flask import Blueprint
from flask import render_template


order=Blueprint('order', __name__, template_folder='templates')

@order.route('/')
def orders():
    return render_template('page/order.html')