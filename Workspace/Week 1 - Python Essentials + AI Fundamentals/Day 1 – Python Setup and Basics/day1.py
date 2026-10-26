def create_learning_message(name, topic, hours):
    text_message = f"Hello {name}, we are learning about {topic} and will take {hours} hours to complete"
    return text_message

name = input("What is your name: ")
topic = input("What is your topic: ")
hours_text = input("What is your hours: ")

if not name or not topic:
    print("Name and Topic cannot be empty")
else:
    try:
        hours = int(hours_text)

        if hours < 0:
            print("Hours cannot be negative")
        else:
            message = create_learning_message(name, topic, hours)
            print(message)
    except ValueError:
        print("Please enter a valid numbers of hours")