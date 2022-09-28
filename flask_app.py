from flask import Flask
import bs4

import helpers as hp

beerSite = Flask(__name__)

@beerSite.route('/')
def index():
   recipies = hp.getRecipies()

   soup = bs4.BeautifulSoup(recipies)
   css_link = soup.new_tag("link",
                           rel="stylesheet",
                           href="static/main.css")

   soup.head.append(css_link)
   
   return str(soup)

if __name__ == "__main__":
   beerSite.run(host='0.0.0.0', port=5000)
