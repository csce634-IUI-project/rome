# File to store all the constants for hobby_selector

import os
import csv

import jinja2


HTML_ROOT = 'html/'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__))),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def GetFile(name):
  """Gets the file with named name."""
  return file(os.path.join(os.path.dirname(os.path.dirname(__file__)),
              'textfiles/' + name))

def GetActivities():
  activities = []
  for row in csv.DictReader(GetFile('activities.csv')):
    activities.append(row['Activity'])
  return activities