def check_balance(text):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in text:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
                
    return len(stack) == 0

test_strings = ["()", "({[]})", "(]", "((()", "{[()]}"]
for s in test_strings:
    print("Test string:", s, "->", check_balance(s))

user_string = input("Enter your own string of brackets to check: ")
print("Result for your string:", check_balance(user_string))

# OUTPUT:
# Test string: () -> True
# Test string: ({[]}) -> True
# Test string: (] -> False
# Test string: ((() -> False
# Test string: {[()]} -> True
# Enter your own string of brackets to check: [
# Result for your string: False