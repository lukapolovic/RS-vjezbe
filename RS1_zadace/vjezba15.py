vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(text):
    result = {'vowels': 0, 'consonants': 0}
    
    temp = text.lower().split()

    for word in temp:
        for character in word:
            if character in vowels:
                result["vowels"] += 1
            elif character in consonants:
                result["consonants"] += 1

    return result

print(count_vowels_consonants(tekst))