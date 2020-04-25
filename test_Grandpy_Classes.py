import Class.Parser as Parser
import Class.User as User
import Class.Maps as Maps
import Class.Wikipedia as Wikipedia
import pytest
import json

def hello(name):
    return "Hello " + name

def test_hello():
    assert hello("Céline") == "Hello Céline"

class TestUser:
    name = "Où se trouve New York ?"

    def test_splitter(self):
        assert User.User("Où se trouve New York ?").splitter() == \
            ["Où", "se", "trouve", "New", "York", "?"]

class TestParser:
    split_words = ["Où", "se", "trouve", "New", "York", "?"]
    path = "ressources/fr-split/fr.json"
    with open(path, encoding='utf-8') as french:
        words = json.load(french)

    def test_compare(self):
        assert Parser.Parser(self.split_words).compare(self.words) == \
            "New York"

class TestMaps:
    city = "New York"
    coordinates = [40.7127753, -74.0059728]

    def test_mapsextract(self):
        assert Maps.Maps(self.city).mapsextract() == \
            ([40.7127753, -74.0059728], \
                ['New York, État de New York, États-Unis'])

    def test_placeextract(self):
        assert Maps.Maps(self.city).placeextract(self.coordinates) == None

class TestWikipedia:
    city = "New york"
    title = "New York"
    wikitext = Wikipedia.Wikipedia(city).wikiextract(title)

    def test_title(self):
        assert Wikipedia.Wikipedia(self.city).title() == "New_York"

    def test_wikipage(self):
        assert Wikipedia.Wikipedia(self.city).wikipage() == "New York"

    def test_wikiextract(self):
        assert Wikipedia.Wikipedia(self.city).wikiextract(self.title) == \
            self.wikitext

    def test_wikipage_return(self, monkeypatch):

        class MockResponse(object):

            def __init__(self):
                self.status_code = 200
                self.url = "https://fr.wikipedia.org/w/api.php"

            def json(self):
                return {'account': '5687', 'url': 'http://www.testurl.com'}

        def mock_get(url):
            return Mockresponse()

            monkeypatch.setattr(requests, 'get', mock_get)
            assert Wikipedia.Wikipedia(self.city).wikipage() == (200, 'http://www.testurl.com')

    