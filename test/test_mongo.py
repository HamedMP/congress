import unittest


from tasks import vote_info

class TestMongoCache(unittest.TestCase):


    def test_output_vote(self):

        vote_info.output_vote()
