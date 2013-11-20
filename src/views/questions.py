import json
import webapp2

from libraries import constants
from libraries import library


class Questions(webapp2.RequestHandler):
  """Class for home page."""

  def post(self):
    asked_questions = self.request.get('asked_questions', '').split(',')
    user_model = json.loads(self.request.get('user_model'))
    tags = []
    q_n_a = {}
    related_activities = []
    scores = {}

    if self.request.get('dummy-activity-type') != 'tag' and not self.request.get('from_questions'):
      tags = library.GetTagsFromActivities(self.request.get('dummy-values'))

    if self.request.get('from_questions'):
      asked_questions.extend(self.request.get('q_sl_no').split(','))
      q_n_a = self.GetQuestionsAndAnswers()
      tags, related_activities = (
          library.ProcessAnswersAndReturnNewTagsAndSuggestedTasks(user_model,
                                                                  q_n_a))
      print 'tags', tags
    else:
      tags.append(self.request.get('dummy-values'))


    # print q_n_a, asked_questions, tags

    print 'tags', tags
    template = constants.JINJA_ENVIRONMENT.get_template(
        constants.HTML_ROOT + 'questions.html')
    questions = library.GetQuestionsFromTags(tags, asked_questions)
    question_sl_nos = []
    for q in questions:
      question_sl_nos.append(q[0])
    self.response.write(template.render({
        'asked_questions': ','.join(asked_questions),
        'q_sl_no': ','.join(question_sl_nos),
        'questions': questions,
        'related_activities': related_activities,
        'calculated_scores': json.dumps(scores),
        'user_model': json.dumps(user_model)}))

  def GetQuestionsAndAnswers(self):
    q_n_a = {}
    qs = self.request.get('q_sl_no').split(',')
    for q in qs:
      q_n_a[q] = self.request.get('question-' + q)
    return q_n_a