import unittest
import python_repos_visual

class ReposTestCase(unittest.TestCase):
    """ A class to test if the values of python_repos are as expected. """
    def test_status_code(self):
        status_code = python_repos_visual.r.status_code
        self.assertEqual(status_code, 200)
    
    def test_repo_dicts_amount(self):
        repo_dict_amount = len(python_repos_visual.repo_dicts)
        self.assertEqual(repo_dict_amount, 30)
    
    def test_repos_returned(self):
        repos_returned = python_repos_visual.response_dict['total_count']
        self.assertGreaterEqual(repos_returned, 60000)

if __name__ == '__main__':
    unittest.main()
