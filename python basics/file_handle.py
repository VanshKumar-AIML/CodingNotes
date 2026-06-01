try:
    f = open('ex.txt','w')
    data = '''1.first line
2.second_line
3.third * line'''
    f.write(data)
    f.close()

    f = open('ex.txt','a')
    f.write('\n4.Appended line')
    f.close()

    f= open('ex.txt','r')
    data3 = f.read()
    f.close()

    print(data3)

except FileNotFoundError:
    print('File not found')

vowel = ['a','e','i','o','u']
line_count = 0
num_count = 0 
alpha_count = 0
vowel_count = 0
con_count = 0
space_count = 0
sp_count = 0

with open('ex.txt','r') as f:
                for line in f:
                    line_count += 1
                    for i in line:
                        if i.isnumeric():
                            num_count += 1
                        elif i.isalpha():
                            alpha_count += 1
                            if i in vowel:
                                vowel_count +=1
                            else:
                                con_count += 1
                        elif i.isspace():
                            space_count += 1
                        else:
                            sp_count += 1

print(f"Line count ={line_count}")
print(f"numeric count ={num_count}")
print(f"alphabet count ={alpha_count}")
print(f"vowel count ={vowel_count}")
print(f"consonent count ={con_count}")
print(f"Spaces = {space_count}")
print(f"Special characters = {sp_count}")

import os
file_path='ex.txt'
if os.path.exists(file_path):
    print('file exists')
else:
    print('file not exists')