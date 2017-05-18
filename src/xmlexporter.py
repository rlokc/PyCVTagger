from lxml import etree

def to_xml_file(tagdict, filepath):
    root = etree.Element("images")
    for imagepath in tagdict:
        image = etree.SubElement(root, "image", filename=imagepath)
        for tag, prob in tagdict[imagepath].items():
            etree.SubElement(image, "tag", value=tag, prob=str(prob))
    tostring(root)

def tostring(root):
    print(etree.tostring(root, pretty_print=True, encoding="unicode"))
