import re
from caesar_cipher.corpus_loader import count_words

def encrypt(plain, key):
    plain = re.sub(r'[^A-Za-z]+','_', plain)
    encrypted_text = ""
    for char in plain:

        if char =="_":
            encrypted_text += " "
            continue
        num=ord(char)
        if char.islower():
            shifted_num = (num + key -97) % 26 +97
        else:
            shifted_num = (num + key -65) % 26 +65
        
        encrypted_text += f"{str(chr(shifted_num))}" 
    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)



def crack(text):

    result=""
    
    for i in range(1,27):
        to_check=decrypt(text,i)
        count=count_words(to_check)
        percentage = int(count / len(text.split()) * 100)
        if percentage > 50:
            result= (to_check, i)
             
    
    if result:
      return result

    



if __name__ == "__main__":
    pins = [
        "anas check"
    ]

    
    x=encrypt("Good man",8)
    # y=crack(x)
    # print(f"the encrypted  message was {x}") 
    print(x)
    # print(y)