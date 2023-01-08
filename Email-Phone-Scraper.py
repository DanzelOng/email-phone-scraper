#! python3
import re 
import pyperclip
import pprint

#Possible phone format: 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
#Create a Regex for phone numbers
phoneRegex = re.compile(r'''
( ( \(?\d{3}?\)? )           #area code (optional)
.?                           #first dash (optional) 
\d{3}                        #first 3 digits
.                            #second dash
\d{4})                       #last 4 digits
([ext]{3}\.?\s|x)?           #extension word-part (optional)
(\d{5})?                     #extension number-part (optional)
''', re.VERBOSE)

#Create a Regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.*]+                #name part
@                              #@ symbol 
[a-zA-Z0-9_.*]+                #domain name symbol
''', re.VERBOSE)

#copy info and paste to clipboard with paste()
info = pyperclip.paste()

extractedPhone = phoneRegex.findall(info)
extractedEmail = emailRegex.findall(info)

#Create an Empty Dict to store the extracted numbers and emails
filteredPhones = []
for AllPhones in extractedPhone:
    filteredPhones.append(AllPhones[0])

resultDict = {}
x = 0

for phones in filteredPhones:
    resultDict[phones] = extractedEmail[x]
    x += 1

#Use pprint to organize the dict
results = pprint.pformat(resultDict)
print(results)
















