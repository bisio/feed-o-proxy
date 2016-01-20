#!/usr/bin/env python3

import unittest
from feedoproxy.Feed import Feed
from feedoproxy.enrichers.avax import get_image_url_from_feed_item

class FeedTest(unittest.TestCase):

    def setUp(self):
        self.feed_string = open("test-data/avax.xml").read()


    def test_can_read_a_feed_in_a_string(self):
        feed = Feed(self.feed_string) 
        
        self.assertEqual(self.feed_string, feed.feed_string)


    def test_feed_items_method_returns_right_number_of_items(self):
        feed = Feed(self.feed_string)

        self.assertEqual(20, len(feed.items()))


class AvaxTest(unittest.TestCase):

    def test_get_image_url_from_feed_item_returns_an_image_url(self):
        self.feed_string = open("test-data/avax.xml").read()
        feed = Feed(self.feed_string) 
        firstItem = feed.items()[0]

        imageUrl = get_image_url_from_feed_item(firstItem)

        self.assertTrue("jpeg" in imageUrl)


if __name__ == '__main__':
    unittest.main(warnings='ignore')    
