from settings import Settings
from clarifai_client import Clarifai
from gcvision_client import GCVision

settings = Settings()
clarifai = Clarifai(settings.CLARIFAI_ID, settings.CLARIFAI_SECRET)
gcvision = GCVision(settings.GOOGLE_KEY)

clarifai.test()

