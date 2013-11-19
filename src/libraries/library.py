import os
import csv


def GetFile(name):
  """Gets the file with named name."""
  return file(os.path.join(os.path.dirname(os.path.dirname(__file__)),
              'textfiles/' + name))


def GetActivities():
  activities = []
  for row in csv.DictReader(GetFile('activities.csv')):
    activities.append(row['Activity'])
  return activities


def GetTagsFromActivities(activities):
  rows = csv.DictReader(GetFile('activities.csv'))
  tags = []
  # Logic has to be improved.
  for row in rows:
    if row['Activity'] in activities:
      for tag in rows.fieldnames:
        if tag == 'Activity':
          continue
        if row[tag] != 'F':
          tags.append(tag)
  tags = list(set(tags))
  return tags


def GetQuestionsFromTags(tags):
  rows = csv.DictReader(GetFile('questions.csv'))
  questions = []
  # Logic has to be improved.
  for row in rows:
    if row['Tag'] in tags:
      questions.append(row['Question'])
  questions = list(set(questions))
  return questions


def GetRelatedActivities(tags, scores):
  pass