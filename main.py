import request_handler as rh
import mapper as m
import json

############################
### Hardcoded API Tokens ###
############################

# Remember to create trial GitHub account and replace the token!
GIT_TOKEN = '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'
FRESHDESK_TOKEN = 'udQTpShDifX24kN0QA'

def main():

    # Ask for user input
    username = input("Please enter a GitHub username: ")
    domain = input("Please enter a freshdesk domain name: ")
    
    # Get GitHub user information based on username
    user = rh.get_github_user(username, GIT_TOKEN).json()
    
    # Map GitHub user information to Freshdesk-friendly one
    contact_json = m.map_to_freshdesk_data(user)
    
    # Send JSON to Freshdesk domain
    contact_req = rh.post_freshdesk_contact(domain, FRESHDESK_TOKEN, contact_json)

if __name__ == '__main__':
    main()