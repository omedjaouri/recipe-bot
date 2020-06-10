import os
from app import create_app
from bot import RecipeBot

#Run the app
bot = RecipeBot()
app = create_app(bot)
#app.run()
