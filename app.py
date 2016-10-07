from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/indus')
def indus():
	return render_template("indus.html")

@app.route('/moodi')
def moodi():
	return render_template("moodi.html")

@app.route('/projectrishi')
def projectrishi():
	return render_template("projectrishi.html")

@app.route('/zahanat')
def zahanat():
	return render_template("zahanat.html")

@app.route('/blog')
def blog():
	return render_template("blog.html")

if __name__=="__main__":
	app.run(debug=False)