topics = ["Java", "Python", "GenAI"]

topics.append("RAG")
topics.remove("Java")

print(len(topics)) #3
print("Python" in topics) #True

numbers = [2, 8, 7, 5, 6, 2]
print(sorted(numbers)) #2 2 5 6 7 8
print(set(numbers)) # 2 5 6 7 8