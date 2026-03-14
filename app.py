from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
# Mobile frontend ko connect karne ki permission
CORS(app)

@app.route('/')
def home():
    return "Webglut AI Backend is Running successfully!"

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    
    # AI Background removal
    result = remove(img)
    
    # Transparent image wapas bhejna
    img_io = io.BytesIO()
    result.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
