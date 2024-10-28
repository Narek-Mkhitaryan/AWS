from flask import Flask, render_template, url_for, send_file
app = Flask("__name__")

@app.route('/')
def index():
    return render_template("index.html", active_page='projects')
@app.route('/skills')
def skills():
    return render_template("skills.html", active_page='skills')


@app.route('/contacts')
def contacts():
    return render_template("contacts.html", active_page='contacts')

@app.route('/download')
def download():
    path = 'static/Profile.pdf'
    return send_file(path, as_attachment=True)

if __name__ =="__main__":
    app.run(debug=True)
