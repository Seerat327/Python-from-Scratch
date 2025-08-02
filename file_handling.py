#Writing a File
f=open('vibes.txt','w')
f.write('Today i learned file handling\n')
f.close()

#Appending a file
with open('vibes.txt','a') as f:
    f.write(' file handling')

#Read from a file
with open('vibes.txt','r') as f:
    for line in f:
        print(line.strip())

#Overwriting a file
with open('vibes.txt','w') as f:
    f.write('File overwritten')
    f.close()

#Count total number of lines in file
with open('vibes.txt', 'r') as f:
    total_lines=0
    for line in f :
        total_lines+=1
print(total_lines)

