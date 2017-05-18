import sys
import os

from settings import Settings
from clarifai_client import Clarifai
from gcvision_client import GCVision
import xmlexporter

EXTENSIONS = ['jpg', 'bmp', 'png', 'tiff', 'jpe', 'jpeg']

def tidy_print(d):
    for f, tags in d.items():
        print("\nТеги для файла", f, ':')
        for k,v in tags.items():
            print(k, ':', v)

def is_image(filename):
    ext = os.path.splitext(filename)[1][1:]
    return ext.lower() in EXTENSIONS

def crawl_recursive(filename):
    if os.path.isfile(filename) and is_image(filename):
        queue.append(filename)
    elif os.path.isdir(filename):
        files = [os.path.join(filename, f) for f in os.listdir(filename)]
        for f in files:
            crawl_recursive(f)

def crawl(filename):
    if os.path.isfile(filename) and is_image(filename):
        queue.append(filename)
    elif os.path.isdir(filename):
        files = [os.path.join(filename, f) for f in os.listdir(filename)]
        for f in files:
            if os.path.isfile(f) and is_image(f):
                queue.append(f)

queue = []
settings = Settings()
clarifai = Clarifai(settings.CLARIFAI_ID, settings.CLARIFAI_SECRET)
gcvision = GCVision(settings.GOOGLE_KEY)

recursive = False
xml_out = False
args = sys.argv[1:]
if '-r' in args:
    recursive = True
    args.remove('-r')
if '-xml' in args:
    xml_out = True
    args.remove('-xml')

for path in args:
    if recursive:
        crawl_recursive(path)
    else:
        crawl(path)

result = clarifai.tag(queue)
if xml_out:
    xmlexporter.to_xml_file(result, "CVTagger_Result.xml")
else:
    tidy_print(result)

