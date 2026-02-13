from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rituals')
def rituals():
    return render_template('rituals.html')

@app.route('/sanctuaries')
def sanctuaries():
    return render_template('sanctuaries.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    success = False
    if request.method == 'POST':
        # Logic to save the application would go here
        success = True
    return render_template('membership.html', success=success)

if __name__ == '__main__':
    app.run(debug=True, port=5000)