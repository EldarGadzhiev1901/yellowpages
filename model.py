def get_data():
    # with open('file.txt', 'r') as file:
    #     data = file.read().split('\n')
    #     file.close()
    path = 'file.txt'
    data = open(path, 'r')
    data.readlines()
    data.close()



def add_contact(contact):
    with open ('file.txt', 'a', encoding='utf-8') as file:
       
        file.write(contact)
        file.write('\n')
        file.close
    

def search(word):
    with open('file.txt', 'r', encoding='utf-8') as file:
        found = False
        for line in file:
            if word in line:
                print(line, end='')
                found = True
        if found == False:
            print("По вашему запросу ничего не найдено ")
        # for line in file:
        #     if word in line:
        #         print(line, end='')
        #         break
        #     else:
        #         print("По вашему запросу ничего не найдено ")
        #         print('\n')
            

def change(contact, new):
    with open('file.txt', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.txt', 'w', encoding='utf-8') as file:
        filedata = filedata.replace(contact, new)
        file.write(filedata)
        file.close()
        

def delete(contact):
    with open('file.txt', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.txt', 'w', encoding='utf-8') as file:
        null = ""
        filedata = filedata.replace(contact, null)
        filedata = filedata.replace('\n\n','\n')
        file.write(filedata)
        file.close()
        
    
         
    