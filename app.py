from flask import Flask, render_template, request
from google import genai

client = genai.Client(api_key="")

# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def response():
 # If method is POST, get the number entered by user
 # Calculate the square of number and pass it to answermaths 
    if request.method == 'POST':
        if(request.form['prompt'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            prompt = request.form['prompt']
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return render_template('answer.html', 
                          prompt=prompt, resp=response.text)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("index.html")