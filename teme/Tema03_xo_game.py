import random


def generateStartBoard() -> list:
    return [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def displayBoard(board: list):
    print(' ' + ' 1 ' + '2 ' + '3')
    for index, row in enumerate(board):
        print(index + 1, row[0], row[1], row[2])


# method to add input to board, returns true if input added or false if the position is ocupied
def addInputToBoard(position: str, playerInput: str, board: list):
    board[int(position[0]) - 1][int(position[1]) - 1] = playerInput


def checkEndOfGame(board: list) -> (bool, str):
    endOfGame = False
    emptySpaces = getEmptyPositions(board)
    winner = ''

    def checkWinnerLines() -> (bool, str):
        winnerLine = False
        winnerPlayer = ''
        for i in range(0, 3):
            if all((el == board[i][0]) and el != '_' for el in board[i]):
                winnerLine = True
                winnerPlayer = board[i][0];
                break
        return winnerLine, winnerPlayer

    def checkWinnerCols() -> (bool, str):
        foundColWinner = False
        winnerPlayer = ''
        for col in range(0, 3):
            winnerCol = True
            for line in range(0, 3):
                if board[line][col] != board[0][col]:
                    winnerCol = False
                    continue
                if line == 2 and winnerCol and board[0][col] != '_':
                    foundColWinner = True
                    winnerPlayer = board[0][col]
                    break
        return foundColWinner, winnerPlayer

    def checkWinnerDiagonals() -> (bool, str):
        foundDiagWinner = False
        winnerPlayer = ''
        if (board[0][0] == board[1][2] == board[2][2]) and board[0][0] != '_':
            foundDiagWinner = True
            winnerPlayer = board[0][0]
        elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != '_':
            foundDiagWinner = True
            winnerPlayer = board[2][0]
        return foundDiagWinner, winnerPlayer

    winnerCheck = [checkWinnerLines(), checkWinnerCols(), checkWinnerDiagonals()]
    foundWinner = list(filter(lambda result: result[0], winnerCheck))

    if len(foundWinner):
        endOfGame = True
        winner = foundWinner[0][1]
    if not len(foundWinner) and not emptySpaces:
        endOfGame = True
        winner = 'Remiza'

    return endOfGame, winner


def displayWinner(pionCastigator: str, pionJucator: str, pionCalc: str):
    if pionCastigator == pionJucator:
        print('Felicitari, ati castigat!')
    elif pionCastigator == pionCalc:
        print('Calculatorul castiga. Mai mult succes data viitoare!')
    else:
        print('Remiza')


def checkValidPosition(playerSelection: str, board: []) -> bool:
    if int(playerSelection[0]) not in range(1, 4) or int(playerSelection[1]) not in range(1, 4):
        return False

    if board[int(playerSelection[0]) - 1][int(playerSelection[1]) - 1] != '_':
        return False
    return True


def getEmptyPositions(board: list) -> list:
    emptyPositions = []
    for lineIndex, line in enumerate(board):
        for colIndex, col in enumerate(line):
            if board[lineIndex][colIndex] == '_':
                emptyPositions.append(str(lineIndex + 1) + str(colIndex + 1))
    return emptyPositions


def getComputerPosition(board: list) -> str:
    emptyPositions = getEmptyPositions(board)
    return random.choice(emptyPositions)


def main():
    inputJucator = ''
    endOfGame = False

    board = generateStartBoard()
    print('Jocul a inceput. Succes!')
    pionJucator = input('Alegeti X sau 0\n').upper()
    pionCalc = ('x' if pionJucator == '0' else '0').upper()
    print(displayBoard(board))

    while inputJucator != 'q' and not endOfGame:
        # TODO randomize who starts the game
        playerSelection = input('Introduceti pozitia pe care doriti sa inserati (linie+coloana, ex: 11):\n')
        validPosition = checkValidPosition(playerSelection, board)
        while not validPosition and playerSelection != 'q':
            playerSelection = input('Pozitie incorecta!\nIntroduceti pozitia pe care doriti sa inserati:\n')
            validPosition = checkValidPosition(playerSelection, board)

        # TODO: abstract function to handle both player moves as the steps are exatly the same.
        addInputToBoard(playerSelection, pionJucator, board)
        print(displayBoard(board))
        endOfGame, winner = checkEndOfGame(board)
        if endOfGame:
            displayWinner(winner, pionJucator, pionCalc)
            break

        compPos = getComputerPosition(board)
        addInputToBoard(compPos, pionCalc, board)
        print(f'Pozitia aleasa de catre calculator: {compPos}')
        print(displayBoard(board))
        endOfGame, winner = checkEndOfGame(board)
        if endOfGame:
            displayWinner(winner, pionJucator, pionCalc)


main()
