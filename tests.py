#!/usr/bin/env python3

import unittest
from feedoproxy.Feed import Feed

class FeedTest(unittest.TestCase):


    def test_can_read_a_feed_in_a_string(self):
        feed_string = open("test-data/avax.xml").read()

        feed = Feed(feed_string) 
        
        self.assertEqual(feed_string, feed.feed_string)

if __name__ == '__main__':
    unittest.main(warnings='ignore')    
