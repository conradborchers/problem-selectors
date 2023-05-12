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

# Remove seen problems
input_dict['problems'] = [entry for entry in input_dict['problems'] if entry['completed_count'] == 0]

# Custom selection
has_mastered_a_skill = sum([entry['p_known'] > .8 for entry in input_dict['skills']]) >= 3

# Default is next problem
ans = input_dict['problems'][0]['name']

# Once three skills are mastered, show a specific problem
if has_mastered_a_skill: ans = '1+2(2x-1)=7'

print("""{"problem_name":"%s"}""" % ans)
