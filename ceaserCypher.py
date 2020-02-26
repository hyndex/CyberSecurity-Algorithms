def ceaserEncrypt(text,key):
    result = "" 
    for i in range(len(text)): 
        char = text[i]
        if (char.isupper()): 
            result += chr((ord(char) + key - 65) % 26 + 65) 
        else: 
            result += chr((ord(char) + key - 97) % 26 + 97) 
  
    return result


# taking input
text = input("Please Enter the string to encrypt: ")
key=''
while not type(key) == int:
    key = input("Enter a key: ")
    try:
        key=int(key)
    except:
        key=str(key)
        print(str(key)," is not a valid input: ") 

data = ceaserEncrypt(text,key)
print("Encrypted Data: ",data) 