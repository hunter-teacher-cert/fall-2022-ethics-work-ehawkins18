import re


def find_name(line):
    #pattern = r'[Dr.]\s*\w[\s|\.]'
   # pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    #original pattern from Z's code
   # result = re.findall(pattern,line)

    pattern=r'[A-Z]\w*[\s|.]{1,2}'
    result = re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)