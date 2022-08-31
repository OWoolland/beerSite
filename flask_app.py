from flask import Flask

import helpers as hp

app = Flask(__name__)

@app.route('/')
def index():
   recipies = hp.getRecipies()
   return recipies

if __name__ == "__main__":
   app.run()
