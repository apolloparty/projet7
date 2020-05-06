import Class.Wikipedia as Wikipedia
import Class.User as User
import Class.Parser as Parser
import Class.Maps as Maps
import json

from flask import Flask, request, jsonify, render_template, make_response

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('app.html')


@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.get_json()
    name = response["message"]
    print(name)
    split_words = User.User(name).splitter()
    words = Parser.Parser(split_words).parser()
    city = Parser.Parser(split_words).compare(words)
    coordinates, address = Maps.Maps(city).mapsextract()
    wikititle = Wikipedia.Wikipedia(city).title()
    title = Wikipedia.Wikipedia(city).wikipage()
    wikitext = Wikipedia.Wikipedia(city).wikiextract(title)
    link = Wikipedia.Wikipedia(city).wikilink()
    print(link)
    return make_response(jsonify({"myCity": city}, {"myList": coordinates}, {"myText": wikitext}, {"myTitle": link}), 200)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(debug=True)
