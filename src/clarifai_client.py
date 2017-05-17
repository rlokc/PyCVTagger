from clarifai.rest import ClarifaiApp

class Clarifai():
    
    def __init__(self, api_id, api_secret):
        self.api_id = api_id
        self.api_secret = api_secret

        self.app = ClarifaiApp(self.api_id, self.api_secret)

    def tag(self, files):
        raw_tags = self.app.tag_files(files)
        res = {}
        if raw_tags['status']['description'] == 'Ok':
            # TODO: right now it parses only one image
            tags = raw_tags['outputs'][0]['data']['concepts']
            for tag in tags:
                res[tag['name']] = tag['value']
        return res


    def test(self):
        res = self.app.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])
        if res['status']['description'] == 'Ok':
            concepts = res['outputs'][0]['data']['concepts']
            for concept in concepts:
                print(concept['name'], concept['value'])
