import requests
import json

def wikipage():
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": "New York",
        "formatversion": "2",
        "format": "json"
    }
    req = requests.get(url, params)
    extracted = json.loads(req.content.decode('UTF-8'))
    title = extracted['query']['search'][0]['title']

    return req.status_code, url


def test_wikipage_return(monkeypatch):

    class MockResponse(object):

        def __init__(self):
            self.status_code = 200
            self.url = "https://fr.wikipedia.org/w/api.php"

        def json(self):
            return {'account': '5687', 'url': 'http://www.testurl.com'}

    def mock_get(url):
        return Mockresponse()

        monkeypatch.setattr(requests, 'get', mock_get)
        assert wikipage() == (200, 'http://www.testurl.com')