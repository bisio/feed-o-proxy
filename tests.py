#!/usr/bin/env python3

import unittest
from feedoproxy.Feed import Feed

class FeedTest(unittest.TestCase):

    def setUp(self):
        self.feed_string = open("test-data/avax.xml").read()


    def test_can_read_a_feed_in_a_string(self):
        feed = Feed(self.feed_string) 
        
        self.assertEqual(self.feed_string, feed.feed_string)


    def test_feed_items_method_returns_right_number_of_items(self):
        feed = Feed(self.feed_string)

        self.assertEqual(20, len(feed.items()))




if __name__ == '__main__':
    unittest.main(warnings='ignore')    
