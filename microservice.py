from flask import jsonify

import store
import covid19
import json

app = Flask(__name__)

@@ -29,4 +31,22 @@ def welcome():
def getPosts():
    name = request.args.get('name')
    posts = store.searchTextData(name)
    return jsonify(posts) 
    return jsonify(posts)

@app.route('/sendSinglePost', methods=['POST'])

def sendSinglePost():

    response = {}

    if request.method == 'POST':

        options = json.loads(request.data)

        filename = covid19.getImageFilename(options)

        options['url'] = store.addImageData(filename)

        store.addTextData(options)

    return jsonify(options) 