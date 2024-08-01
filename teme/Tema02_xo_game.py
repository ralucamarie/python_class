import random

board = {
    'A1': '',
    'A2': '',
    'A3': '',
    'B1': '',
    'B2': '',
    'B3': '',
    'C1': '',
    'C2': '',
    'C3': '',
}


def getValue(position: str):
    if len(board[position]) and board[position].upper() in ['X', '0']:
        return board[position].upper()
    else:
        return '_'


def displayBoard():
    print('   1   2   3')
    print(f'A  {getValue("A1")}   {getValue("A2")}   {getValue("A3")}')
    print(f'B  {getValue("B1")}   {getValue("B2")}   {getValue("B3")}')
    print(f'C  {getValue("C1")}   {getValue("C2")}   {getValue("C3")}')


inputJucator = ''
endOfGame = False
print('Jocul a inceput. Succes!')
pionJucator = input('Alegeti X sau 0\n').upper()
pionCalc = ('x' if pionJucator == '0' else '0').upper()
pionCastigator = ''
compPos = ''


# method to add input to board, returns true if input added or false if the position is ocupied
def addInputToBoard(position: str, input: str):
    if len(board[position.upper()]):
        return False
    else:
        board[position.upper()] = input
        return True


def calculateComputerPosition():
    emptyPositions = []
    for pos in board:
        if not len(board[pos]):
            emptyPositions.append(pos)
    return random.choice(emptyPositions)


def checkEndOfGame():
    global pionCastigator
    global endOfGame
    if (board['A1'] == board['A2'] == board['A3']) and board['A1'] in [pionCalc, pionJucator]:
        pionCastigator = board['A1']
        endOfGame = True
    elif board['B1'] == board['B2'] == board['B3'] and board['B1'] in [pionCalc, pionJucator]:
        endOfGame = True
        pionCastigator = board['B1']
    elif board['C1'] == board['C2'] == board['C3'] and board['C1'] in [pionCalc, pionJucator]:
        endOfGame = True
        pionCastigator = board['C1']
    elif board['A1'] == board['B2'] == board['C3'] and board['A1'] in [pionCalc, pionJucator]:
        endOfGame = True
        pionCastigator = board['A1']
    elif board['A3'] == board['B2'] == board['C1'] and board['A3'] in [pionCalc, pionJucator]:
        endOfGame = True
        pionCastigator = board['A3']


def displayWinner():
    if pionCastigator == pionJucator:
        print('Felicitari, ati castigat!')
    else:
        print('Calculatorul castiga. Mai mult succes data viitoare!')


while inputJucator != 'q' and not endOfGame:
    print(displayBoard())
    inputJucator = input('Introduceti pozitia pe care doriti sa inserati:\n')
    addInputToBoard(inputJucator, pionJucator)
    compPos = calculateComputerPosition()
    addInputToBoard(compPos, pionCalc)
    print(f'Pozitia aleasa de catre calculator: {compPos}')
    print(displayBoard())
    checkEndOfGame()
    if endOfGame:
        displayWinner()
