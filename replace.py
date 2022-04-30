with open("sample.txt") as f:
    content = f.read()

content =content.replace("donkey","##%@4")

with open("sample.txt","w") as f:
    f.write(content)