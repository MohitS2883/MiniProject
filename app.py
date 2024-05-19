from flask import *
import os
from detect import pred
from suggestions import returnSuggestions
import threading
from langchainlogic import main as langchain_main
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def getinput():
    return render_template('input.html')

@app.route('/trial', methods=['GET', 'POST'])  
def result():
    if request.method == 'POST':
        print("Form submitted successfully!")
        image = request.files['inpimage']
        path = "static/Image"
        print(image)
        os.makedirs(path, exist_ok=True)  
        image_path = os.path.join(path, image.filename)
        image.save(image_path)
        print("Image saved successfully at:", image_path)
        ans = pred(image_path)
        sugg = returnSuggestions(ans)
        print("Prediction result:", ans)
        print("suggestions",sugg)
        return render_template('index.html', ans=ans, path=image_path,sugsend = sugg)
    return render_template('input.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/home')
def redirect_home():
    return redirect("/")

def run_chatlit_server():
    # Run the LangChain logic
    langchain_main()


if __name__ == "__main__":
    langchain_thread = threading.Thread(target=run_chatlit_server)
    langchain_thread.start()
    app.run(host="0.0.0.0", debug=True)
 