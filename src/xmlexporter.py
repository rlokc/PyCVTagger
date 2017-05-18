from lxml import etree
import os

def to_xml_file(tagdict, filepath):
    root = etree.Element("images")
    for imagepath in tagdict:
        image = etree.SubElement(root, "image", filename=imagepath)
        for tag, prob in tagdict[imagepath].items():
            etree.SubElement(image, "tag", value=tag, prob=str(prob))
    to_file(root, filepath)

def to_string(root):
    print(etree.tounicode(root, pretty_print=True))

def to_file(root, filepath):
    with open(filepath, 'w') as f:
        f.write(etree.tounicode(root, pretty_print=True))
    print("Результат записан в", os.path.abspath(filepath))
