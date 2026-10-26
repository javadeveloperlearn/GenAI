lang1 = ["Java", "Python", "GenAI", "JavaScript"]
lang2 = ["Python", "GenAI", "C++", "Java"]

set1 = set(lang1)
set2 = set(lang2)

common_lang = set1 & set2

print(common_lang) #{'GenAI', 'Java', 'Python'}