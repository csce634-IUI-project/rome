# The landing page for the application.
#
# This file directs the application to the various pages based on the URL.

import webapp2

from views import home


app = webapp2.WSGIApplication([
    ('/', home.MainPage),
], debug=True)
