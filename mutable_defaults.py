# Code Quality Error 1: Mutable Default Arguments
# WARNING: Using mutable default arguments is dangerous!

def append_to_list(item, items=[]):  # WARNING: Mutable default argument
    """This function has a bug - the list persists between calls!"""
    items.append(item)
    return items

def add_to_dict(key, value, data={}):  # WARNING: Mutable default argument
    """This function has the same bug with dictionaries"""
    data[key] = value
    return data

def register_user(name, roles=[]):  # WARNING: Mutable default argument
    """New users might unexpectedly share roles!"""
    roles.append("user")
    return {"name": name, "roles": roles}

# Test the bug
print(append_to_list(1))  # [1]
print(append_to_list(2))  # Expected [2], but got [1, 2]!
print(append_to_list(3))  # Expected [3], but got [1, 2, 3]!
