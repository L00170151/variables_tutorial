line_length = 30
top = "^"*line_length
empty = ("<" + (" "*(line_length-2)) +  ">")
# middle = < + xspaces a string + yspaces + >

title = "Title"
option_a = "A   Option A"
option_b = "B   Option B"
option_c = "C   Option C"
bottom = "~"*line_length

print(top)
print(empty)
print(empty)
print("<" + title.center(line_length - 2) + ">")
print(empty)
print(empty)
print("<" + option_a.center(line_length - 2) + ">")
print("<" + option_b.center(18) + ">")
print("<" + option_c.center(18) + ">")
print(empty)
print(empty)
print(bottom)
print("hello")