import json
import webapp2

from libraries import constants
from libraries import library


class MainPage(webapp2.RequestHandler):
  """Class for home page."""

  def get(self):
    template = constants.JINJA_ENVIRONMENT.get_template(
        constants.HTML_ROOT + 'home.html')
    self.response.write(template.render(
        {'activities': json.dumps(library.GetActivities()),
         'activity_list': library.GetActivities(),
         'user_model': json.dumps(library.GetUserModel())}))
