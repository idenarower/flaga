from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ua')
def ua():
    return render_template("ua.html")

@app.route('/de')
def de():
    return render_template("de.html")

@app.route('/pl')
def pl():
    return render_template("pl.html")

@app.route('/us')
def us():
    return render_template("us.html")

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")

@app.route('/r_1')
def r_1():
    return render_template('r_1.html')

if __name__=="__main__":
    app.run()
