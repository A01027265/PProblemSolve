'''
Created November 11, 2020

@Authors:
- Emilio Popovits Blake (A01027265)
- Patricio Tena (A01027293)
- Ana Paola Minchaca (A01026744)
- Rodrigo Benavente (A01026973)
'''

from os import listdir, path

def psolve(parsedProblem):
    fileLines = parsedProblem

    # Save first 3 lines (problem description) into inputDesc array, and save clauses into inputProblem array
    inputDesc = [fileLines[0], fileLines[1], fileLines[2]]
    inputProblem = fileLines[3:len(fileLines)]

    # Cast inputProblem variables in clauses to integers
    for indexC, clause in enumerate(inputProblem):
        for indexV, variable in enumerate(clause):
            inputProblem[indexC][indexV] = int(variable)

    # Convert binarystring into array
    inputBinaryString = inputDesc[2]
    
    binaryString = []
    for char in inputBinaryString[0 : len(binaryString)-1 : 1]:
        binaryString.append(char)
    
    binaryString.append(inputBinaryString[len(inputBinaryString)-1])

    # print(inputProblem)
    # print(binaryString)
    # print('\n')
    rejectFlag = False
    for clause in inputProblem:
        # print('Clause: ', clause)

        clauseValue = 0
        # print('Binary Values: ')
        for variable in clause:
            binaryValue = int(binaryString[abs(variable)-1])
            if variable > 0:
                clauseValue += binaryValue
            else:
                if binaryValue == 1:
                    binaryValue = 0
                else:
                    binaryValue = 1
                clauseValue += binaryValue
            # print([binaryString[abs(variable)-1],binaryValue])
        
        if clauseValue == 0:
            rejectFlag = True
        
        # print('Value: ' + str(clauseValue))
        # print()
    
    if rejectFlag:
        return 0
    else:
        return 1

if __name__ == '__main__':
    # Select input problem file
    print('Files in ./Input/ directory:')
    fileArray = []
    count = 1
    for file in listdir('./Input'):
        if file.endswith('.txt'):
            print(path.join(str(count) + '. ', file))
            fileArray.append(file)
            count += 1
    
    prompt = input('\nWhich file number contains the P problem that you want to solve? ')
    selectedFile = fileArray[int(prompt)-1]
    file = open('./Input/' + selectedFile,)
    
    # Save all lines in selected file into array
    fileLines = []
    for line in file:
        fileLines.append(line)
    file.close()

    # Remove '\n' from every line and make input problem clauses and first three lines into array
    for index, line in enumerate(fileLines):
        fileLines[index] = ''.join(line.split('\n'))
        if index > 2:
            fileLines[index] = fileLines[index].split(' ')
            fileLines[index].remove('0')

    solution = psolve(fileLines)

    print(solution)
