def animal_crackers(text):
    word = text.split()
    if word[0][0].lower() == word[1][0].lower():
        return True
    else:
        return False


print(animal_crackers('Levelheaded llama'))
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('levelheaded Llama'))
print(animal_crackers('Levelheaded Blama'))
