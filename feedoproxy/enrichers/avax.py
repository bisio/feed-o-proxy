#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib.request

def get_image_url_from_feed_item(feed):
    """ Given an item from the avaxhome feed, returns the image associated to the item."""
    item_url = feed.find("link").text
    response = urllib.request.urlopen(item_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    metas = soup.find_all("meta")
    for meta_element in metas:
        if meta_element.attrs.get("property"):
            property_attribute = meta_element.attrs.get("property")
            if property_attribute == "og:image":
                image_url = meta_element.get("content")
                return(image_url)
    return ""

if  __name__ == "__main__":
    main()

