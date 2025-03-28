
 
def read_file(file_name):
    '''loads the contents of the file into python'''
    with open(file_name) as file_object:
        '''reads the content of the file into the program'''
        global contents
        contents=file_object.read()
    true_texts=contents.lower().replace('?',"").replace(',',"").replace("''","").replace("'","").replace("!","")
    true_texts=true_texts.replace(':',"").replace('-',"")
    global formatted_texts
    formatted_texts=true_texts.split(' ')
    
def count_words():
    '''counts the total number of words in  a .txt file'''
    number=len(formatted_texts)
    return number
    
def freq_particular_word(word):
    '''counts the number of times a particular word appears'''
    if word in formatted_texts:
        freq=formatted_texts.count(word)
    print('The total number of times '+word+' appears in this text file is :'+str(freq))
    
def freq_of_all_words():
    '''gives the frequency of all unique words and stores it in a list'''
    dict_1={}
    unique=formatted_texts.set()
    for words in unique:
        frequency=unique.count('words')
        dict_1[words]=frequency
    return dict_1

def total_characters():
    'gives the total number of characters in a text file'
    characters=len(contents)
    print('the total number of characters are: '+str(characters))


file="C:/Users/LENOVO L460/Documents/alice in wonderland.txt"
read_file(file)
