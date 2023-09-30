import random
import string

def generate_password(user_words, length=12):
 
    characters = string.ascii_letters + string.digits + string.punctuation

    chars_per_word = length // len(user_words)

    password = ""

    for word in user_words:
        word_chars = list(word)
        random.shuffle(word_chars)
      
        password += "".join(word_chars[:chars_per_word])
    
    while len(password) < length:
        password += random.choice(characters)

    password_chars = list(password)
    random.shuffle(password_chars)
    final_password = "".join(password_chars)

    return final_password

if __name__ == "__main__":
    user_input = input("Enter words or phrases separated by spaces: ")
    user_words = user_input.split()

    if not user_words:
        print("Please enter at least one word or phrase.")
    else:
        password_length = int(input("Enter the desired password length: "))

        if password_length < len(user_words):
            print("Password length is too short for the provided words.")
        else:
            password = generate_password(user_words, password_length)
            print(f"Generated Password: {password}")
