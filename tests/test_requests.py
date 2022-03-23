import request_handler as rh
import mapper as m
import unittest
from tests.data import git_data, modified_git_data
from main import GIT_TOKEN, FRESHDESK_TOKEN

class TestRequests(unittest.TestCase):

    # Make sure we get the correct data and status code
    def test_github_get(self):
        username = 'fabpot'
        token = GIT_TOKEN

        res = rh.get_github_user(username, token)
        self.assertEqual(res.status_code, 200)

    # Make sure we can post a freshdesk contact with the github data
    # NOTE: Since data does not change and the test will be run a few times, we expect status code 409 (conflict)
    def test_freshdesk_post(self):
        domain = 'qbtest'
        freshdesk_data = m.map_to_freshdesk_data(git_data)
        req = rh.post_freshdesk_contact(domain, FRESHDESK_TOKEN, freshdesk_data)

        # Since the contact will be existing, we expect status code 409 and an error message
        self.assertEqual(req.status_code, 409)
    
    # Make sure that we can update an existing freshdesk contact
    def test_freshdesk_put(self):
        domain = 'qbtest'
        id = 101025388504
        freshdesk_data = m.map_to_freshdesk_data(modified_git_data)
        req = rh.update_existing_contact(domain, FRESHDESK_TOKEN, id, freshdesk_data)
    
        self.assertEqual(req.status_code, 200)

    if __name__ == '__main__':
        unittest.main()