#####################################################################
#  COMP-570A Assignment 2                                           #
#  Author: Sathyanarayanan Subramanian                              #
##################################################################### 

import re
from fileinput import close

from _ctypes import Union

#        Getting User Input from Url or File         

input_choice = input("##########################################################################\n\t\t\tHow you want to give input\n##########################################################################\n1.Url \n2.Physical File\nEnter your Choice:\t")

if(input_choice=='1'):
    url_input = input("Enter url:\t")
    from urllib.request import urlopen
    file = urlopen(url_input).read().decode('utf-8')
elif (input_choice=='2'):
    file_name = input("Enter the file Name:\t")
    text = open(file_name)
    file = text.read()
    
else:
    print("Invalid Input")



def striphtml(file):
    result = re.sub("<.*?>"," ",file)
    return result
# This retrieves only <p>


def get_count(str1):
    word_freq = {}
    from collections import defaultdict
    word_freq = defaultdict(int)
    for word in str1.split():
        word_freq[word] += 1
    print ("\t",word_freq)
    
    return 0



print ("****************************** R E S U L T ******************************")
#################################################################### Find title of the page  #################3############################################## 
pattern = re.findall("<[t|T][i|I][t|T][l|L][e|E]>(.*)</[t|T][i|I][t|T][l|L][e|E]>", file)
patt = ''.join(pattern)
print ("TITLE OF THE GIVE PAGE IS :\t",patt)

########################################################  Find number of occurences of a word in the paragraph############################################### 

#Removing all the HTML tags in a file
para1 = re.findall("<[p|P]>([\s\S]*?)<[p|P]>", file)
para2 = re.findall("<[p|P]>([\s\S]*?)</[p|P]>",file)
para3 = para1 + para2
str1 = ' '.join(para3)
str1 = striphtml(str1)
out_file1 = striphtml(str1)

print ("\nNUMBER OF OCCURENCE OF EACH WORD IN THE PARAGRAPH:\n")
get_count(out_file1)

#############################################################  3.) Find links available in the webpage ##########################################
links = re.findall("[H|h][r|R][e|E][f|F]=(.*)", file)

#Filtered Mail from the hyperlink list
remove_mail = re.compile("mailto:")
filtered = filter(lambda i: not remove_mail.search(i), links)
filtered = [i for i in links if not remove_mail.search(i)]
print ("\nNUMBER OF HYPER_LINKS AFTER FILTERING E-MAILS :\t",len(filtered))

################################################################   E - MAIL Check #############################################
#abc@psu.edu
email = re.findall("[\w\.-]+@[\w\.]+", file)
if email != []:
    print ("Email:\t",email)

email1 = re.findall("([\w]+\(at\)[\w]+\(dot\)[\w]+)+", file)
if email1 != []:
    print ("Email:\t",email1)

#abc at psu dot edu
email3 = re.findall("(\w+ at \w+ dot \w+)", file)
if email3 != []:
    print ("Email:\t",email3)

obfus_email = re.findall("obfuscate\(.*\)", file)
str2 = ''.join(obfus_email)
mail = re.findall("\'(.+?)\'", str2)
if mail != []:
    o_mail = mail[1]+"@"+mail[0]
    print ("Email:\t", o_mail)

#Character entity email format:
input = re.findall(r"mailto: &(.*)>", file)
input = ''.join(input)
input1 = re.findall('\d+', input)
inp =   re.findall("[\d]+", input) 
ascii_email = ""
for i in inp:
        i = int(i)
        ascii_email += (chr(i))
if ascii_email != '':
    print("Email: \t",ascii_email)    
    
    
job_number = re.findall("Job Numer: \d\d\d\d\d\d", file)
print (job_number)


