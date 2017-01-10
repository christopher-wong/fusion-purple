# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import webbrowser

from application import app

# if deploying as local web server, uncomment the line below
# webbrowser.open('http://localhost:5000', new=0, autoraise=True)

# Run the app
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	host = '0.0.0.0'
	app.jinja_env.cache = {}
	app.run(host = host, 
			port = port,
			debug = True,
			threaded = True)