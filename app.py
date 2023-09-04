from flask import Flask, request, make_response
from flask_cors import CORS
from math import floor
import cv2
import numpy as np
import base64
import tools


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "<p> Hello, World!</p>"

@app.route("/api/id_photo", methods=["POST"])
def id_photo():
    print(request.form)
    print(request.form.get("photoSize"))
    photo_size = parse_cm_size_to_resolution(request.form.get("photoSize"))
    paper_size = parse_cm_size_to_resolution(request.form.get("paperSize"))
    
    #  read encoded image
    image = request.files['photo'].read()

    #  convert binary data to numpy array
    nparr = np.fromstring(image, np.uint8)

    #  let opencv decode image to correct format
    img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
    _,im_bytes_np = cv2.imencode(".png", img)
    paper_image = tools.id_photo_layout(img, photo_size, paper_size,[255,0,0])
    _,im_bytes_np = cv2.imencode(".png", paper_image)
    # response = make_response(im_bytes_np.tobytes())
    response = make_response(im_bytes_np.tobytes())
    response.headers.set('Content-Type', 'image/png')
    return response

# 英寸size(1=5*10)转化成像素分辨率, 默认DPI 300
def parse_cm_size_to_resolution(size_str, dpi=300):
    width_cm=float(size_str.split('=')[1].split('*')[0]);
    height_cm=float(size_str.split('=')[1].split('*')[1]);
    CM_PER_INCH = 2.54;
    width_pixel = floor(width_cm * dpi / CM_PER_INCH);
    height_pixel = floor(height_cm * dpi / CM_PER_INCH);
    size = tools.Size(width=width_pixel, height=height_pixel);
    return size;