from flask import Flask, render_template, request
from datetime import datetime

SPRAVNE_HESLO="12345678"
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
	heslo=None
	zprava=None
	valid=False

	if request.method=="POST":
		name=request.form.get("name")
		surname=request.form.get("surname")

		if not name or not surname:
			zprava="Musíš zadat jméno i příjmení!"

		elif len(name) > 50:
			zprava="Jméno smí být maximálně 50 znaků dlouhé!"

		elif len(surname) > 50:
			zprava="Příjmení smí být maximálně 50 znaků dlouhé!"
		
		else:
			valid=True
			heslo=request.form.get("heslo")

			if heslo==SPRAVNE_HESLO:
				zprava="Zítra přiletí mimozemšťané!"
			else:
				zprava="Nesprávné heslo!"

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, zprava=zprava, valid=valid)

if __name__=="__main__":
	app.run(debug=True)