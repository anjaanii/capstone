from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quality')
def quality():
    return render_template('quality.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sex')
def sex():
    return render_template('sex.html')


if __name__=="__main__":
    app.run(debug=True)