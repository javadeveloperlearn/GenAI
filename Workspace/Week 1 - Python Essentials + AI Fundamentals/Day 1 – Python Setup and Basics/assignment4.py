name = input("Enter your name: ")
topic = input("Enter your topic: ")

if not name or not topic:
    print("Please enter your name and topic")
else:
    print(f"Hi {name} and the topic to learn today is {topic}")