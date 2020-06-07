import re

url_regex = re.compile( r'^https?://'  # http:// or https://
        		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        		r'localhost|'  # localhost...
        		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        		r'(?::\d+)?'  # optional port
        		r'(?:/?|[/?]\S+)$', re.IGNORECASE)

#Verifies that the user sent a valid URL
def validate_url(url):
 #Return false if the URL is none or does not match URL regex
 return url is not None and url_regex.search(url)

