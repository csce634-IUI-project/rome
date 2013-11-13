# The landing page for the application.
#
# This file directs the application to the various pages based on the URL.

import webapp2

from views import home
from views import questions


app = webapp2.WSGIApplication([
    ('/questions', questions.Questions),
    ('/', home.MainPage),
], debug=True)
