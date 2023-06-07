from flask import Flask, render_template
import os

application = app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/sample')
def sample():
    return render_template('sample.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
