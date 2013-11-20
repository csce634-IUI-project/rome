import json
import webapp2

from libraries import constants
from libraries import library


class Questions(webapp2.RequestHandler):
  """Class for home page."""

  def post(self):
    asked_questions = self.request.get('asked_questions', '').split(',')
    asked_questions = [x for x in asked_questions if x]
    user_model = json.loads(self.request.get('user_model'))
    count = int(self.request.get('count', 0))
    if not count:
      count = 0
    tags = []
    q_n_a = {}
    related_activities = []
    scores = {}

    if self.request.get('dummy-activity-type') != 'tag' and not self.request.get('from_questions'):
      tags = library.GetTagsFromActivities(self.request.get('dummy-values'))

    if self.request.get('from_questions'):
      asked_questions.extend(self.request.get('q_sl_no').split(','))
      q_n_a = self.GetQuestionsAndAnswers()
      activity_n_votes = self.GetActivityAndVotes()
      tags, related_activities = (
          library.ProcessAnswersAndReturnNewTagsAndSuggestedTasks(
              user_model, q_n_a, activity_n_votes))
    else:
      tags.append(self.request.get('dummy-values'))

    template = constants.JINJA_ENVIRONMENT.get_template(
        constants.HTML_ROOT + 'questions.html')
    questions = library.GetQuestionsFromTags(tags, asked_questions)
    question_sl_nos = []
    for q in questions:
      question_sl_nos.append(q[0])
    output = {
        'asked_questions': ','.join(asked_questions),
        'q_sl_no': ','.join(question_sl_nos),
        'questions': questions,
        'related_activities': related_activities,
        'ra': json.dumps(related_activities),
        'calculated_scores': json.dumps(scores),
        'user_model': json.dumps(user_model),
        'count': json.dumps(count + 1)}
    if count == 10 or not questions:
      output['questions'] = []
      output['finish'] = True
    self.response.write(template.render(output))

  def GetQuestionsAndAnswers(self):
    q_n_a = {}
    qs = self.request.get('q_sl_no').split(',')
    for q in qs:
      q_n_a[q] = self.request.get('question-' + q)
    return q_n_a

  def GetActivityAndVotes(self):
    a_n_v = {}
    av = json.loads(self.request.get('related_activities'))
    for act in av:
      a_n_v[act[0]] = self.request.get('activity-voting-' + act[1])
    return a_n_v
