f = open('input.txt', 'r')
for line in f:
    print(line.rstrip())

f.seek(0)
S1 = f.read()
List_of_strs = S1.split('\n')
print(List_of_strs)
print(".".join(List_of_strs))

# r+ - чтение и запись
# w+ - запись и чтение
# a+ - дополнить файл

f = open('out1.txt', 'w')
S1 = "Hello World\n"
S2 = 'Goodbye'
S3 = 'See you soon\n'
f.write(S1)
f.flush() # скинуть на диск информацию, при этом не закрывая сам файл
f.write(S1)
f.close()

with open('out1.txt', 'w') as f:
    S1 = "Hello World\n"
    S2 = 'Goodbye'
    S3 = 'See you soon\n'
    L1 = [S1, S2, S3]
    f.writelines(L1)

with open('input.txt', 'r') as f, open('out1.txt', 'w') as g:
    for line in f:
        g.write(line)
    f.seek(0)
    # или 
    for line in f:
        print(line.rstrip(), file = g)


with open('input.txt', 'r') as f:
    with open('out1.txt', 'w+') as g:
        for line in f:
            if line.startswith('I'):
                g.write(line)
        g.seek(0)
        print(g.readline())

slovar = {}
with open('input1.txt', 'r') as f:
    f.readline()
    for line in f:
        Pr = line.split(' ')
        name, age, height, school = Pr[0], Pr[1], Pr[2], Pr[3]
        slovar[name] = {}
        slovar[name]["age"] = age
        slovar[name]["height"] = height
        slovar[name]["school"] = school.strip()
print(slovar)
