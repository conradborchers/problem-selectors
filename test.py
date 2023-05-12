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

print("""{"problem_name":"%s"}""" % input_dict['problems'][0]['name'])
