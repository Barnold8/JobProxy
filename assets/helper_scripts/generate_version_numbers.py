from random import randint

def generate_version_numbers():
    
    x = []
    words = ["invalid","-1","nothing","__-__---__--","\n\n","asdmkasdmasd"]
    
    for i in range(5):
        words.append(str(randint(1,9)*-1))
        
    for i in range(20):
        if randint(0,100) > 40:
            x.append(f"{randint(1,9)}.{randint(1,9)}.{randint(1,9)}")
        else:
            x.append(f"{words[randint(0,len(words)-1)]}.{words[randint(0,len(words)-1)]}.{words[randint(0,len(words)-1)]}")
    return x
    
for index, elem in enumerate(generate_version_numbers()):
    print(f"\"Test{index}\": \"{elem}\",")