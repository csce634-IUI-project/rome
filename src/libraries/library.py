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
	return null
	

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
  
print ("NULL")
