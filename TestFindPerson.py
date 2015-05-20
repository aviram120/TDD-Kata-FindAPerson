import unittest
from crowdmap import Crowdmap

class FindPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley",
                                  "Or in Tel-Aviv","Or in Las Vegas"])

    def test_getAllPostsForName(self):
        posts = self.crowdmap.get_all_posts_for("Or")
        self.assertIn("Or in Las Vegas",posts)

    def test_get_all_posts_for_missing_name(self):
        posts = self.crowdmap.get_all_posts_for("Or")
        self.assertFalse(posts)