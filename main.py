from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    q = request.args.get('q')
    print(q)
    return { "message": "Hello!" }, 201

@app.route('/number/<num>')
def showNumber(num):
    q = request.args.get('q')
    print(q)
    return { "message": num }, 201

@app.route('/showWeb/<name>')
def showWebSite(name=None):
    return render_template('test.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return { "message" : 'method post เด้อ'}, 201
    elif request.method == "GET":
        return { "message" : 'method GET เด้อ'}, 201
        

if __name__=='__main__':
    app.run(debug=True)