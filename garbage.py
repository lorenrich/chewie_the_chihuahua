# Garbage I wrote that I'm too afraid to get rid of just yet but it didn't work anyway so who cares?


# Create a dictionary to store the manually calculated indentation values so centering will look consistent across frames
line_length = []
indent = []
b=SCREEN_WIDTH
for a in range(0, SCREEN_WIDTH):
    a += 1
    line_length.append(a)

for b in range(SCREEN_WIDTH, 0, -1):
    b -= 1
    c = b // 2
    indent.append(c)

indent_dict = dict(zip(line_length, indent))
print(indent_dict)


def get_indentation_need(text):
    """Manually calculate how to center frame drawings for consistency on screen"""
    line_length = len(text)
    indent_needed = " " * indent_dict.get(line_length, 0)
    
    print(f"DEBUG - Line: '{text}'")
    print(f"DEBUG - Length: {line_length}")
    print(f"DEBUG - Character by character:")
    for i, char in enumerate(text):
        if char == ' ':
            print(f"  {i}: [SPACE]")
        else:
            print(f"  {i}: '{char}'")
    print(f"DEBUG - Indent from dict: {indent_dict.get(line_length, 0)} spaces")
    print("-" * 50)

    return indent_needed