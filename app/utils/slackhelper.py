from slackclient import SlackClient
from config import get_env

#Slack API Helper Class
class SlackHelper:

    #Initialize slack client 
    def __init__(self):
        self.slack_token = get_env('SLACK_BOT_TOKEN')
        self.slack_client = SlackClient(self.slack_token)


