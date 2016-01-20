import xml.etree.ElementTree as ET

class Feed:
    def __init__(self,feedString):
        self.feed_string = feedString

    def items(self):
        root = ET.fromstring(self.feed_string)
        channel = root.find("channel")
        items = channel.findall("item")
        return items
