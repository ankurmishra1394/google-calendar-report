from flask import Flask, Blueprint, request, jsonify, redirect, url_for

app = Flask(__name__)
calendar = Blueprint('report', __name__, url_prefix='/report')

@calendar.route('', methods=['GET', 'POST'])
def hello_world():
	data = request.data
	print data
	return 'Hello World'