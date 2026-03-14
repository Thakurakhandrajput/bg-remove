from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove, new_session
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Yahan humne Lite AI model (u2netp) set kiya hai jo 512MB RAM mein aaram se chalega
lite_session = new_session("u2netp")

@app.route('/')
def home():
    return "Webglut AI Backend is Running successfully!"

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    
    # AI ko batana ki lite engine se background hatao
    result = remove(img, session=lite_session)
    
    img_io = io.BytesIO()
    result.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
