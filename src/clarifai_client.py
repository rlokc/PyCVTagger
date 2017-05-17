from clarifai.rest import ClarifaiApp

class Clarifai():
    
    def __init__(self, api_id, api_secret):
        self.api_id = api_id
        self.api_secret = api_secret

        self.app = ClarifaiApp(self.api_id, self.api_secret)

    def test(self):
        res = self.app.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])
        print(res)
