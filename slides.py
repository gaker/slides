from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/slide/<int:slide_id>')
def show_slide(slide_id):
    return 'Slide {0}'.format(slide_id)

if __name__ == '__main__':
    app.run()


    
