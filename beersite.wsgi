import logging
import sys
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/home/owool/.local/lib/python3.9/site-packages')

from flask_app import app as application
application.secret_key = 'anything you wish'
