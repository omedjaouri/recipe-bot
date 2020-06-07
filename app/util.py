from urllib.parse import urlparse

#Verifies that the user sent a valid URL
def validate_url(url):
    #Return false if the URL is none or does not match URL regex
    parsed_url = urlparse(url)
    if scheme == '' or netloc == '':
        return None #Bad URL
    else:
        return parsed_url


#Processes a user's request to handle a recipe link
def process_request(req):
    #Validate the url
    url = validate_url(req)
    #If the url is invalid, report None
    if url is None:
        return None

    


    recipe = True
    return recipe
