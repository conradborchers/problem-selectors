#!/usr/bin/python3.5

import sys
import json

# Read the JSON input from standard input
input_data = sys.stdin.read()

# Parse the input JSON string into a dictionary
try:
    input_dict = json.loads(input_data)
except ValueError as e:
    sys.stderr.write("Error parsing JSON input: {}\n".format(e))
    sys.exit(1)

# Unseen problems 
unseen_problems = [entry for entry in input_dict['problems'] if entry['completed_count'] == 0]
unseen_tutored_problems = [entry for entry in unseen_problems if entry['name'] not in ['Mid-Question']]

# End if no more unseen tutor problems
ans = 'END' if len(unseen_tutored_problems) == 0 else unseen_tutored_problems[0]['name']

# Check if at least two skills have been mastered
two_skills = sum([entry['p_known'] > .95 for entry in input_dict['skills']]) >= 2

# Once two skills are mastered, show mastery question (once)
if two_skills and 'Mid-Question' in [entry['name'] for entry in unseen_problems]: ans = 'Mid-Question'

# Check if at least 5 skills have been mastered
five_skills = sum([entry['p_known'] > .95 for entry in input_dict['skills']]) >= 5
if five_skills: ans = 'END'

print("""{"problem_name":"%s"}""" % ans)
