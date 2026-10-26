developer = {"name": "Ganesha", "experience": 11}
print(developer.get("name")) #Ganesha
print(developer.get("location", "Not provided")) #Not provided

developer["language"] = "Python"
print(developer) #{'name': 'Ganesha', 'experience': 11, 'language': 'Python'}