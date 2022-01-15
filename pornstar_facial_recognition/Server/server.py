from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET','POST'])

def classify_image():
	image_data = request.form['image data']

	response = jsonify(util.classify_image(image_data))

	respons.header.add('Access-Control-Allow-Origin', '*')

	return response
if __name__ ==  "__main__":

	print('starting python flask')
	util.load_saved_artifacts()
	app.run(port= 5000)