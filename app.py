from flask import Flask, render_template, request
import os
from detect import pred
from suggestions import returnSuggestions
app = Flask(__name__)

@app.route('/')
def trial():
    return render_template('input.html')

@app.route('/trial', methods=['GET', 'POST'])  
def home():
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
 