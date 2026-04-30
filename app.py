from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.args.get("name")
	surname=request.args.get("surname")

	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["GET", "POST"])
def pozdrav_post():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=None
	surname=None

	if request.method=="POST":
		name=request.form.get("name")
		surname=request.form.get("surname")

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname)

if __name__=="__main__":
	app.run(debug=True)