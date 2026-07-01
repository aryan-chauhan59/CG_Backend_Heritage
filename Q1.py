# Design a login cache where username lookup is as fast as possible.


login_cache = {}

def add_to_cache(username, user_id):
    login_cache[username] = user_id
    print(f"Added {username} to cache.")

def find_user(username):
    
    user_data = login_cache.get(username)
    
    if user_data:
        return f"User found! ID: {user_data}"
    else:
        return "User not found in cache."

add_to_cache("aryan123", 98765)
print(find_user("aryan123"))
print(find_user("bikram456"))