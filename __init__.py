from flask import Flask, request, render_template
from report.route import calendar

app = Flask(__name__)

app.register_blueprint(calendar)

if __name__ == '__main__':
	app.run(debug=True)