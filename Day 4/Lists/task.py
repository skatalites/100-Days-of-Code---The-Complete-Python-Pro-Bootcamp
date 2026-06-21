import random

languages = ["Chinese", "English", "Spanish", "Arabic", "French", "Persian", "German", "Russian", "Malay", "Portuguese", "Italian", "Turkish", "Lahnda", "Tamil", "Urdu", "Korean", "Hindi", "Bengali", "Japanese", "Vietnamese", "Telugu", "Marathi"]

print(languages[2])
print(languages[-1])
print(languages[random.randint(0, len(languages))])

print(languages[2:4]) # Slicing

indigenousLang = ["Kogui", "Emberá", "Quechua", "Aymara", "Nahuatl", "Zapotec", "Guaraní", "Mapudungun", "Navajo", "Māori", "Ainu", "Khoisan"]

languages.extend(indigenousLang)

print(languages[-1])
last = languages.pop()
languages.append(last)

print(languages[-1])

languages.sort()
print(languages)
languagesInv = sorted(languages)
languagesInv.sort(reverse=True)
print(languagesInv)


