import os
import csv
import operator

# Put everything as a class perhaps?
# Modules Needed 
# Question parsing and storage
# Question Selection
# Usage of initial user input for generating initial list of questions
# Recommendation of Activities
# Upvote Downvote Handling
# Upvoted Activities Saving
# Completion of Conflict Resolution Module

main_db = {}
category = ''
tagFreq = {}
conflict_table = {}
conflict_table_timeline = {}

def read_file():
  with open('../textfiles/hobby_list.csv','r')as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    categorySet = 0
    global category
    global main_db
    global tagFreq
    for row in reader:
      if categorySet == 0:
        category = row
        categorySet = 1
      else:
        key = row.pop(0)
        main_db[key] = row
    category.pop(0)
    for cat in (range(len(category))):
      i = 0
      for key in main_db:
        if(main_db[key][cat]!='x'):
          i+=1
      tagFreq[category[cat]] = i

# Module for conflict resolution

#def timestamp_handler():
# This function is started at the start of the program. Each time any recommendation is generated, this gets incremented.
# Need for a persistent counter

def conflict_table_modifier ( activity ):
  conflict_table[activity] = conflict_table[activity] + 1
  conflict_table_timeline[activity] = timestamp_handler()


def timestamp_handler():
  pass


# Module to return tag position
def tag_position (category, tag):
  tagpos = 0
  for  i in range(len(category)):
    tagpos = i
    if category[i] == tag:
      return tagpos
  return -1

# Module for Incrementing Tags based on labels of the Questions
def increment_main_db (main_db, pushed_dict ):
  #print (category)
  for tag in pushed_dict:
    for index in main_db:
      pos = tag_position(category, tag)
      if(pos != -1):
        if(main_db[index][pos] != 'x'):
          if(int(main_db[index][pos]) < 6):
            if(int(main_db[index][pos]) > 0):
              main_db[index][pos] = str(int(main_db[index][pos]) + 1)

# Module for Decrementing Tags based on labels of the Questions
def decrement_main_db ( main_db, pushed_dict ):
  for tag in pushed_dict:
    for index in main_db:
      pos = tag_position(category, tag)
      if(pos != -1):
        if(main_db[index][pos] != 'x'):
          if(int(main_db[index][pos]) < 6):
            if(int(main_db[index][pos]) > 0):
              main_db[index][pos] = str(int(main_db[index][pos]) - 1)

#Module for returning the name of activity with the highest score
def get_max(temp):
  max = 0
  max_act = ''
  for activity in temp:
    if(temp[activity] > max):
      max = temp[activity]
      max_act = activity
  return max_act

# Module for Generating a ranking
def get_ranking (main_db):
  initial_dict = {}
  d = {}
  for activity in main_db:
    actCount = 0
    activity_sum = 0
    for tag in range(len(main_db[activity])):
      if(main_db[activity][tag] != 'x'):
        activity_sum += int(main_db[activity][tag])
        actCount+=1
      if(activity_sum != 0):
        initial_dict[activity] = activity_sum/actCount
  ranked_dict = {}
  temp = initial_dict.copy()
  for i in range(4):
    max_activity = get_max(temp)
    ranked_dict[max_activity] = temp[max_activity]
    del temp[max_activity]
  return ranked_dict


def GetFile(name):
  """Gets the file with named name."""
  return file(os.path.join(os.path.dirname(os.path.dirname(__file__)),
              'textfiles/' + name))


def GetActivities():
  activities = []
  for row in csv.DictReader(GetFile('hobby_list.csv')):
    activities.append(row['Activity'])
  return activities


def GetTagsFromActivities(activities):
  rows = csv.DictReader(GetFile('hobby_list.csv'))
  tags = []
  # Logic has to be improved.
  for row in rows:
    if row['Activity'] in activities:
      for tag in rows.fieldnames:
        if tag == 'Activity' or tag == 'Sl no':
          continue
        if row[tag] != 'x':
          tags.append(tag)
  tags = list(set(tags))
  return tags


def GetQuestionsFromTags(tags, asked_questions):
  # TODO: filter question from already asked questions and return top 2 questions.
  rows = csv.DictReader(GetFile('questions.csv'))
  questions = []
  # Logic has to be improved.
  for row in rows:
    if row['Tag'] in tags:
      questions.append((row['Sl no'], row['Question']))
  questions = list(set(questions))
  for qno in reversed(range(len(questions))):
    if questions[qno][0] in asked_questions:
      del questions[qno]
  return questions[:2]


def ProcessAnswersAndReturnNewTagsAndSuggestedTasks(user_model, q_n_a, act_with_votes):
  tags_with_answers = GetTagsFromQuestionsAndAssociateAnswers(q_n_a)
  ScoreActivities(user_model, tags_with_answers, act_with_votes)
  related_tasks = GetTopFourTasksWithHighestScore(user_model)
  tags = GetTagsFromActivities([x[0] for x in related_tasks])
  return tags, related_tasks


def GetTopFourTasksWithHighestScore(db):
  initial_dict = {}
  for activity, row in db.iteritems():
    actCount = 0
    activity_sum = 0
    for tag in row.keys():
      if tag in ('Sl no', 'Activity'):
        continue
      if row[tag] != 'x':
        activity_sum = activity_sum + int(row[tag])
        actCount = actCount + 1
    if activity_sum != 0:
      initial_dict[activity] = float(activity_sum)/float(actCount)
  ranked_dict = []
  sorted_x = sorted(initial_dict.iteritems(), key=operator.itemgetter(1))
  sorted_x.reverse()
  for act in sorted_x[:4]:
    ranked_dict.append((act[0], db[act[0]]['Sl no']))
  return ranked_dict


def ScoreActivities(user_model, tags_with_answers, act_with_votes):
  for tag, ans_val in tags_with_answers.iteritems():
    for act in user_model.values():
      if act[tag] != 'x':
        if int(act[tag]) < 6 and ans_val_dict.get(ans_val, 0) == 1:
          act[tag] = int(act[tag]) + 1
        elif int(act[tag]) > 0 and ans_val_dict.get(ans_val, 0) == -1:
          act[tag] = int(act[tag]) - 1
  for act, vote in act_with_votes.iteritems():
    for key, item in user_model[act].iteritems():
      if key not in ('Sl no', 'Activity') and item != 'x':
        if int(item) < 6 and vote > 0:
          user_model[act][key] = int(item) + 1
        elif int(item) > 0 and vote < 0:
          user_model[act][key] = int(item) - 1


ans_val_dict = {
    ('yes', '+'): 1,
    ('yes', '-'): -1,
    ('no', '+'): -1,
    ('no', '-'): 1
}


def GetTagsFromQuestionsAndAssociateAnswers(q_n_a):
  """
  Returns: {'tag_name': (Answer, valence)}
  """
  rows = csv.DictReader(GetFile('questions.csv'))
  tags = {}
  # Logic has to be improved.
  for row in rows:
    if row['Sl no'] in q_n_a.keys():
      tags[row['Tag']] = (q_n_a[row['Sl no']], row['Valence (+/-)'])
  return tags


def GetRelatedActivities(tags, scores):
  pass


def GetUserModel():
  """
  Returns:
    {Activity_name: row from hobby selector as a dict}
  """
  user_model = {}
  for row in csv.DictReader(GetFile('hobby_list.csv')):
    user_model[row['Activity']] = row
  return user_model

