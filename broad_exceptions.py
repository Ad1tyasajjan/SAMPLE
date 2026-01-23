# Code Quality Error 2: Broad Exception Handling
# WARNING: Catching all exceptions hides bugs!

import json

def parse_json_bad(data):
    """Bad practice - catches ALL exceptions"""
    try:
        result = json.loads(data)
        return result
    except:  # WARNING: Bare except catches everything!
        return None

def read_file_bad(filename):
    """Bad practice - catches generic Exception"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception:  # WARNING: Too broad - hides real errors
        return ""

def divide_numbers_bad(a, b):
    """Bad practice - catches BaseException"""
    try:
        return a / b
    except BaseException:  # WARNING: Even catches KeyboardInterrupt!
        return 0

def process_data_bad(data):
    """Multiple broad exceptions"""
    try:
        result = data['key']['nested']
        return int(result)
    except:  # WARNING: Which error occurred? We'll never know!
        print("Something went wrong")
        return None
