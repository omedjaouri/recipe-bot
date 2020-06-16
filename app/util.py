import requests
import re
from bs4 import BeautifulSoup

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

#Formats a list of ingredients into a listed recipe
def to_recipe(ingredients):
    ret_string = "Ingredients: \n"
    for ingredient in ingredients:
        ret_string = ret_string + "\t- "+ingredient+"\n"
    return ret_string

#Processes requests with recipes from a BA site
def process_ba(soup):
    #Find certain tags that we want to use to create our response to the user
    ingredient_strs = soup.find_all(class_="ingredients__text")

    #If we were unable to find any ingredients, likely not a BonAppetit site
    if ingredient_strs is None:
        return None

    #Process list of ingredients
    ingredients = []
    for ingredient_str in ingredient_strs:
        ingredient = remove_tags(str(ingredient_str))
        ingredients.append(ingredient)

    #Convert to returnable string
    return to_recipe(ingredients)


#Processes a user's request to handle a recipe link
def process_request(req):
    #Issue an HTTP Get command to the url
    resp = requests.get(req)
    #If the http request returns bad response, error
    if resp.status_code != 200:
        return None
    
    #Pass the text to BeautifulSoup to analyze
    soup = BeautifulSoup(resp.text, 'html.parser')    
    
    #Check for specific websites
    if "bonappetit" in req:
        return process_ba(soup)

#Basic main for testing purposes.
if __name__ == "__main__":
    url = "https://bonappetit.com/recipe/brown-butter-peach-cobbler"
    url = "http://www.google.com" 

    #Process a basic request
    recipe = process_request(url)

    print(recipe)


