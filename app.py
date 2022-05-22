import cv2
from flask import Flask, render_template, Response
from camera import Video
from temp import exercise

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise_page')
def exercise_page():
    return render_template('exercise_page.html')

@app.route('/bmi_calculator')
def bmi_calculator():
    return render_template('bmi.html')

def gen(camera):
    while True:
        img = camera.get_original_frame()
        frame = exercise.output(img)
        yield(b'--frame\r\n'
              b'Content-Type:  image/jpeg\r\n\r\n' + frame +
              b'\r\n\r\n')
        cv2.waitKey(1)


@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(debug=True)
