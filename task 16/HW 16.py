# 1
def File_to_Str(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()


# 2

def FirstStrFromFile(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.readline()


# print(FirstStrFromFile("input.txt"))

# 3
def ListFile(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.readlines()


# print(ListFile("input.txt"))
# 4

def ListFileWithoutNewLines(file):
    with open(file, 'r', encoding="utf-8") as f:
        L1 = f.read().split('\n')
    return L1


# print(ListFileWithoutNewLines("input.txt"))

# 5
def PrintFile(file):
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')


# print(PrintFile("input.txt"))
# 6
def UnoinFileLines(file):
    with open(file, 'r', encoding="utf-8") as f:
        L1 = f.read().split('\n')
        text = ' '.join(L1)
    return text


print(UnoinFileLines("input.txt"))

# 7

def LineWithoutSpace(text):
    return text.rstrip(' \n\t')


# 8

def LineWithoutSymbols(text):
    return text.rstrip('!?.')


# 9
def WriteIntoFile(file_name, text):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(text)


# WriteIntoFile("out1.txt", "Hellodfklsdfjjeqi9r\ndlfksdkf")
# 10

def WriteIntoFileNewLine(file_name, text):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.writelines([text, '\n'])


# WriteIntoFileNewLine("out1.txt", "Hellodfklsdfjjeqi9r\ndlfksdkf")
# 11

def WriteIntoFileList(file_name, list):
    with open(file_name, 'w', encoding="utf-8") as f:
        f.writelines(list)


# 12

def WriteFileToAnotherone(file1, file2):
    with open(file1, 'r', encoding="utf-8") as f, open(file2, 'w', encoding="utf-8") as g:
        print(f.read(), file=g)


# WriteFileToAnotherone('input.txt', 'out2.txt')
# 13

def OnlyHelloWorld(file1, file2):
    with open(file1, 'r', encoding="utf-8") as f, open(file2, 'w', encoding="utf-8") as g:
        L1 = f.read().split('\n')
        for line in L1:
            if line.startswith('hello') and line.endswith('world'):
                g.write(line + '\n')


# OnlyHelloWorld('input.txt', 'out3.txt')

# 14

def analyzer(file_name):
    slovar = {}
    with open(file_name, 'r', encoding="utf-8") as f:
        f.readline()
        L1 = f.read().split('\n')
        for line in L1:
            parm = line.split()
            name, pet, pets_age = parm[0], parm[1], parm[2]
            slovar[name] = (pet, pets_age)
    return slovar

print(analyzer('input3.txt'))
