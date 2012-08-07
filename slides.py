import json
import utils
from flask import Flask, jsonify, render_template


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/slide-list/')
def get_slide_list():
    slides = utils.read_slides_dir()
    return jsonify(slides=slides)


@app.route('/slide/<int:slide_id>')
def show_slide(slide_id):
    slide = utils.get_slide(slide_id)
    return jsonify(slide=slide)


if __name__ == '__main__':
    app.run()
