import re


def find_name(line):
    #pattern = r'[Dr.]\s*\w[\s|\.]'
   # pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    #original pattern from Z's code
   # result = re.findall(pattern,line)

    pattern=r'[A-Z]\w*\s[A-Z]\w*'
    result = re.findall(pattern,line)
  
    pattern=r'[A-Z]\w*\s[A-Z]\w*\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    pattern=r'[A-Z]\.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
  
    pattern=r'Dr.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
  
    pattern=r'Mr.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
  
    pattern=r'Mrs.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    pattern=r'Ms.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    pattern=r'Mrs.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
    return result

f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)