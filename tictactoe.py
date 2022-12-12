
class Game():
    boardValues = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def board(self):
        count = 0
        for i in range(3):
            print("|",end = " ")
            for j in range(3):
                print(self.boardValues[i+j+count], "|",end = " "),
            count +=2
            print("\n+++++++++++++")

    def gameState(self):
        agents = ["Agent1","Agent2"]
        nextValue = ' '
        for i in range(9):
            if(i%2==0):
                selectedAgent = agent1
                nextValue = 'X'
            else:
                selectedAgent = agent2
                nextValue ='O'
            print(selectedAgent + " Agent! Placed it's " + nextValue + " at:")
            self.board()
            print("\n")
            if nextValue == 'X':
                if selectedAgent == "QLearning":
                    idx = self.QLMove(game)
                else:
                    idx = finalMove(game, selectedAgent)
            else:
                if selectedAgent == "QLearning":
                    idx = self.QLMove(game)
                else:
                    idx = finalMove(game, selectedAgent)
            if self.boardValues[idx] == " ":
                self.boardValues[idx] = nextValue
                if self.gameOver() == 'X':
                    self.board()
                    print("OMG! We have a winner.Congratulations " + agent1)
                    break
                elif self.gameOver() == 'O':
                    self.board()
                    print("OMG! We have a winner.Congratulations "+ agent2)
                    break
                elif self.gameOver() == 0:
                    self.board()
                    print("OOPS! Unfortunatly we don't have a winner.")
                    break
                else:
                    continue

    def placeAgent(self, position, currentAgent):
        player = None
        if(currentAgent == " "):
            self.boardValues[position] = " "
        else:
            if (currentAgent == agent1):
                player = 'X'
            else:
                player = 'O'
            self.boardValues[position] = player

    def isGameOverTemp(self,memory, currentAgent):
        if(currentAgent == agent1):
            if self.gameOverTemp(memory) == 'X':
                return 1
            elif self.gameOverTemp(memory) == 'O':
                return -1
            elif self.gameOverTemp(memory) == 0:
                return 0
            else:
                return -10
        elif(currentAgent == agent2):
            if self.gameOverTemp(memory) == 'X':
                return -1
            elif self.gameOverTemp(memory) == 'O':
                return 1
            elif self.gameOverTemp(memory) == 0:
                return 0
            else:
                return -10


    def gameOverTemp(self, memory):
        if (memory.boardValues[0] == memory.boardValues[1] == memory.boardValues[2] != " "):
            return memory.boardValues[2]
        elif (memory.boardValues[3] == memory.boardValues[4] == memory.boardValues[5] != " "):
            return memory.boardValues[5]
        elif (memory.boardValues[6] == memory.boardValues[7] == memory.boardValues[8] != " "):
            return memory.boardValues[8]
        elif (memory.boardValues[0] == memory.boardValues[3] == memory.boardValues[6] != " "):
            return memory.boardValues[6]
        elif (memory.boardValues[1] == memory.boardValues[4] == memory.boardValues[7] != " "):
            return memory.boardValues[7]
        elif (memory.boardValues[2] == memory.boardValues[5] == memory.boardValues[8] != " "):
            return memory.boardValues[8]
        elif (memory.boardValues[0] == memory.boardValues[4] == memory.boardValues[8] != " "):
            return memory.boardValues[8]
        elif (memory.boardValues[2] == memory.boardValues[4] == memory.boardValues[6] != " "):
            return memory.boardValues[6]
        else:
            for i in range(0,9):
                if(memory.boardValues[i] == " "):
                    return 1
            return 0

    def gameOver(self):
        if (self.boardValues[0] == self.boardValues[1] == self.boardValues[2] != " "):
            return self.boardValues[2]
        elif (self.boardValues[3] == self.boardValues[4] == self.boardValues[5] != " "):
            return self.boardValues[5]
        elif (self.boardValues[6] == self.boardValues[7] == self.boardValues[8] != " "):
            return self.boardValues[8]
        elif (self.boardValues[0] == self.boardValues[3] == self.boardValues[6] != " "):
            return self.boardValues[6]
        elif (self.boardValues[1] == self.boardValues[4] == self.boardValues[7] != " "):
            return self.boardValues[7]
        elif (self.boardValues[2] == self.boardValues[5] == self.boardValues[8] != " "):
            return self.boardValues[8]
        elif (self.boardValues[0] == self.boardValues[4] == self.boardValues[8] != " "):
            return self.boardValues[8]
        elif (self.boardValues[2] == self.boardValues[4] == self.boardValues[6] != " "):
            return self.boardValues[6]
        else:
            flag = False
            for i in range(0,9):
                if(self.boardValues[i] == " "):
                    flag = True
                else:
                    continue
            if(flag==True):
                return 1
            else:
                return 0
    def positionsLeft(self):
        positionLeft = []
        for i in range(len(self.boardValues)):
            if self.boardValues[i] == " ":
                positionLeft.append(int(i))
        return positionLeft

    def minimax(self, memory, currentAgent):
        '''
        Minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Minimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.minimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.minimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                return maxValue

    def alphabeta(self, memory, currentAgent, alpha, beta):
        '''
        Alphabeta pruning minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Alphabeta_Minimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.alphabeta(memory, getOpponent(currentAgent), alpha, beta)
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                    if (maxValue > beta):
                        return maxValue
                    else:
                        alpha = max(alpha, maxValue)
                return maxValue
            else:
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.alphabeta(memory, getOpponent(currentAgent), alpha, beta)
                    memory.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                    if (maxValue < alpha):
                        return maxValue
                    else:
                        beta = min(beta, maxValue)
                return maxValue

    def expectimax(self, memory, currentAgent):
        '''
        Expectimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Expectimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.expectimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                nodes = len(memory.positionsLeft())
                probability = 1/nodes
                expectiValue = 0
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.expectimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    expectiValue = expectiValue + (newValue * probability)
                return expectiValue

    def qLearning(self, board, QKey):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        diagLeft = [self.boardValues[0], self.boardValues[4], self.boardValues[8]]
        diagRight = [self.boardValues[2], self.boardValues[4], self.boardValues[6]]
        if diagLeft.count(" ") == 1 and diagLeft.count(QKey) == 2:
            idx = diagLeft.index(" ")
            if idx == 0:
                return 0
            elif idx == 1:
                return 4
            else:
                return 8
        elif diagRight.count(" ") == 1 and diagRight.count(QKey) == 2:
            idx = diagRight.index(" ")
            if idx == 0:
                return 2
            elif idx == 1:
                return 4
            else:
                return 6
        for i in range(3):
            count = 0
            rows = [self.boardValues[count], self.boardValues[count+1], self.boardValues[count+2]]
            if rows.count(" ") == 1 and rows.count(QKey) == 2:
                idx = rows.index(" ")
                if idx == 0:
                    return count
                elif idx == 1:
                    return count+1
                else:
                    return count+2
            count = count + 3

        for j in range(3):
            count = 0
            cols = [self.boardValues[count], self.boardValues[count+3], self.boardValues[count+6]]
            if cols.count(" ") == 1 and cols.count(QKey) == 2:
                idx = cols.index(" ")
                if idx == 0:
                    return count
                elif idx == 1:
                    return count+3
                else:
                    return count+6
            count = count + 1
        return None

    def counterMove(self, board, enemyKey):
        """ Block the opponent if it has a win available. """
        return self.qLearning(board, enemyKey)



    def pickcenter(self, board):
        """ Pick the center if it is available. """
        if self.boardValues[4] == " ":
            return 4
        return None

    def pickcorner(self, board, enemyKey):

        corner = [self.boardValues[0],self.boardValues[2],self.boardValues[6],self.boardValues[8]]
        if corner.count(" ") == 4:
            return random.choice(corner)
        else:
            if self.boardValues[0] == enemyKey and self.boardValues[8] == " ":
                return 8
            elif self.boardValues[2] == enemyKey and self.boardValues[6] == " ":
                return 6
            elif self.boardValues[8] == enemyKey and self.boardValues[0] == " ":
                return 0
            elif self.boardValues[6] == enemyKey and self.boardValues[2] == " ":
                return 2
        return None

    def diamondSide(self, board):
        """ Pick an empty side. """
        diamond = [self.boardValues[1], self.boardValues[3], self.boardValues[5], self.boardValues[7]]
        if diamond.count(" ") == 4:
            return random.choice(diamond)
        else:
            count = 1
            for i in range(0,3):
                if(diamond[i] == " "):
                    return count
                count = count + 2
        return None


    def QLMove(self, board):
        """
        trained move for Q-Learning Agent
        """
        if(agent1 == "QLearning"):
            QKey = 'X'
            enemyKey = 'O'
        elif(agent2 == "QLearning"):
            QKey = 'O'
            enemyKey = 'X'
        # Chose randomly with some probability so that the teacher does not always win
        if random.random() > 0.9:
            return random.choice(game.positionsLeft())
        # Follow optimal strategy
        if(self.qLearning(board,QKey) != None and self.qLearning(board,QKey) != ' '):
            return self.qLearning(board,QKey)
        elif(self.counterMove(board, enemyKey) != None and self.counterMove(board, enemyKey) != ' '):
            return self.counterMove(board, enemyKey)
        elif(self.pickcenter(board) != None and self.pickcenter(board) != ' '):
            return self.pickcenter(board)
        elif(self.pickcorner(board, enemyKey) != None and self.pickcorner(board, enemyKey) != ' '):
            return self.pickcorner(board, enemyKey)
        elif(self.diamondSide(board) != None and self.diamondSide(board) != ' '):
            return self.diamondSide(board)
        else:
            return random.choice(game.positionsLeft())

def getOpponent(selectedAgent):
    if selectedAgent == agent1:
        return agent2
    else:
        return agent1

def finalMove(game, selectedAgent):
    bestValue = 0
    bestMove = []
    for move in game.positionsLeft():
        game.placeAgent(move, selectedAgent)
        if(selectedAgent == "Minimax"):
            newValue = game.minimax(game, getOpponent(selectedAgent))
        elif(selectedAgent == "Alphabeta_Minimax"):
            newValue = game.alphabeta(game, getOpponent(selectedAgent), -1000, 1000)
        elif(selectedAgent == "Expectimax"):
            newValue = game.expectimax(game, getOpponent(selectedAgent))
        game.placeAgent(move, " ")
        if newValue >= bestValue:
            bestValue = newValue
            bestMove.append(move)
    print("Move",bestMove)
    if(len(bestMove) == 0):
        return random.choice(game.positionsLeft())
    else:
        return random.choice(bestMove)


if __name__ == "__main__":
    import random
    import math
    game = Game()
    game.board()
    print("Please Select Agent1 & Agent2 from following:")
    agentSelection = {1: 'Minimax', 2:'Alphabeta_Minimax', 3:'Expectimax', 4:'QLearning'}
    print(agentSelection)
    val1 = int(input("Please Enter your choice of Agent1:"))
    agent1 = agentSelection.get(val1)
    print(agent1)
    del agentSelection[val1]
    print(agentSelection)
    val2 = int(input("Please Enter your choice of Agent2:"))
    agent2 = agentSelection.get(val2)
    print(agent2)
    game.gameState()