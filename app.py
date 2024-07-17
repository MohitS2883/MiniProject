from flask import *
import os
from detect import pred
from suggestions import returnSuggestions
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def getinput():
    return render_template('input.html')

@app.route('/trial', methods=['POST'])  
def result():
    if request.method == 'POST':
        image = request.files['inpimage']
        path = "static/Image"
        os.makedirs(path, exist_ok=True)  
        image_path = os.path.join(path, image.filename)
        image.save(image_path)
        ans = pred(image_path)
        sugg = returnSuggestions(ans)
        return render_template('index.html', ans=ans, path=image_path,sugsend = sugg)
    return render_template('input.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/home')
def redirect_home():
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
 
