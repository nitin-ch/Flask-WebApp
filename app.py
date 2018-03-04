import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    img_data = request.files['webcam'].save('test.jpg')
    # import base64
    # with open("imageToSave.jpg", "wb") as fh:
    #    fh.write(base64.decodebytes(img_data))

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    # file.save(f)

    return render_template('index.html')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8888'))
    except ValueError:
        PORT = 8888
    app.run(HOST, PORT)
