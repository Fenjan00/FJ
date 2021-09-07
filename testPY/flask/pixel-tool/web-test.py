from flask import Flask, render_template, url_for, redirect
# import OpenSSL

app = Flask(__name__)

@app.route("/")
def test1():
    # return redirect('http://172.24.118.35:5000/test2')
    return render_template('a.html')

@app.route("/test2")
def test2():
    # return redirect('http://172.24.118.36:5000/test3')
    return render_template('b.html')

@app.route("/test3")
def test3():
    return render_template('c.html')

#test4重定向去test3
@app.route("/test4")
def test4():
    return redirect( 'http://172.24.207.18:5000/')



if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run()