from clarifai.rest import ClarifaiApp

class Clarifai():
    
    def __init__(self, api_id, api_secret):
        self.api_id = api_id
        self.api_secret = api_secret

        self.app = ClarifaiApp(self.api_id, self.api_secret)

    def tag(self, filenames):
        raw_tags = self.app.tag_files(filenames)
        res = {}
        if raw_tags['status']['description'] == 'Ok':
            tagged_files = raw_tags['outputs']
            for index, f in enumerate(tagged_files):
                tags = f['data']['concepts']
                tag_dict = {}
                for tag in tags:
                    tag_dict[tag['name']] = tag['value']
                filename = filenames[index]
                res[filename] = tag_dict
        return res

    def tag_raw(self, files):
        return self.app.tag_files(files)

    def test(self):
        res = self.app.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])
        if res['status']['description'] == 'Ok':
            concepts = res['outputs'][0]['data']['concepts']
            for concept in concepts:
                print(concept['name'], concept['value'])
