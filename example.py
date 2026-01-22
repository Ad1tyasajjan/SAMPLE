"""
Example Python file for testing the code validator
This file demonstrates valid Python code
"""
import os
import json
from datetime import datetime

def greet(name: str) -> str:
    """Greet a person by name"""
    return f"Hello, {name}!"

def main():
    """Main function"""
    print(greet("World"))
    print(f"Current time: {datetime.now()}")
    
    # Example of using standard library
    data = {"message": "This is valid code"}
    print(json.dumps(data))

if __name__ == "__main__":
    main()




