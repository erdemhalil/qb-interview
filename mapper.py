import json

def map_to_freshdesk_data(GitHub_json):
    """
    Select useful fields from GitHub response and make it into a "Freshdesk-friendly" Python Object

    :param GitHub_json: JSON response from GitHub
    """ 
    contact = {
        "name": GitHub_json['name'],
        "email": GitHub_json['email'],
        "twitter_id": GitHub_json['twitter_username'],
        "address": GitHub_json['location'],
        "description": GitHub_json['bio']
    }

    # Turn Python object into JSON object
    contact_json = json.dumps(contact)
    
    return contact_json