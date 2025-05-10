from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Print form data to console (replace with database logic)
        print(f"New contact message from {name} ({email}): {message}")
        
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)