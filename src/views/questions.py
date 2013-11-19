import webapp2

from libraries import constants
from libraries import library


class Questions(webapp2.RequestHandler):
  """Class for home page."""

  def post(self):
    print self.request
    tags = [self.request.get('dummy-values')]
    scores = {}
    if self.request.get('dummy-activity-type') != 'tag':
      tags = library.GetTagsFromActivities(self.request.get('dummy-values'))
    template = constants.JINJA_ENVIRONMENT.get_template(
        constants.HTML_ROOT + 'questions.html')
    self.response.write(template.render({
        'questions': library.GetQuestionsFromTags(tags),
        'related_activities': library.GetRelatedActivities(tags, scores)}))
