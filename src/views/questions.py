import webapp2

from libraries import constants


class Questions(webapp2.RequestHandler):
  """Class for home page."""

  def post(self):
    print self.request.get('dummy-activity-type'), self.request.get('dummy-values')
    template = constants.JINJA_ENVIRONMENT.get_template(
        constants.HTML_ROOT + 'questions.html')
    self.response.write(template.render({}))
