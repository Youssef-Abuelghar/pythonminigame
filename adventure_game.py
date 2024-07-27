import time

import random


# the function thats uses the module time to make the game more exciting

def print_pause(string):
    print(string)
    time.sleep(3)


class game:

    def __init__(
        self,
        stoneqnt=0,
        ironqnt=0,
        goldqnt=0,
        diamondqnt=0,
        inventory=[],
        score=0,
        numberOfWins=0
    ):
        self.stoneqnt = stoneqnt
        self.ironqnt = ironqnt
        self.goldqnt = goldqnt
        self.diamondqnt = diamondqnt
        self.inventory = inventory
        self.score = score
        self.numberOfWins = numberOfWins

# in this function i used the random module , here the player enters the
# cave and gets an ore randomly from the following ores
# the ore he gets is added to his inventory where he can see it
    # #later on with another function

    def cave(self):
        # i repeated some words more than one time
        # in order to make some probabilties

        ores = [
            'stone',
            'stone',
            'stone',
            'stone',
            'iron',
            'iron',
            'gold',
            'gold',
            'diamond',
            ]
        TmpOre = random.choice(ores)
        if TmpOre in self.inventory:
            pass
        else:
            self.inventory.append(TmpOre)
        if TmpOre == 'stone':
            self.stoneqnt += 1
        elif TmpOre == 'iron':
            self.ironqnt += 1
        elif TmpOre == 'gold':
            self.goldqnt += 1
        elif TmpOre == 'diamond':
            self.diamondqnt += 1
        print_pause('You found ' + TmpOre)
        if TmpOre == 'diamond':
            sell = \
                input('you can sell this diamond for 4 gold'
                      '(1 to sell/2 to keep the diamond)'
                      )
            if sell == '1':
                self.diamondqnt -= 1
                self.goldqnt += 4
                if 'gold' in self.inventory:
                    pass
                else:
                    self.inventory.append('gold')
            elif sell == '2':
                print('you chose to keep the diamond')
            else:
                pass

# this is the function where the player can see his inventory

    def ShowInv(self):
        if self.inventory == []:
            print_pause('you dont have any items')
        for items in self.inventory:
            if items == 'stone':
                print('you have ', self.stoneqnt, items)
            elif items == 'iron':
                print('you have ', self.ironqnt, items)
            elif items == 'gold':
                print('you have ', self.goldqnt, items)
            elif items == 'diamond':
                print('you have ', self.diamondqnt, items)

    # this is the main function of the game

    def fight_ring(self):

        # i repeated some words here too to make random probabilties

        listOfLuck = [
            'correct',
            'correct',
            'correct',
            'correct',
            'wrong',
            'wrong',
            'wrong',
            'wrong',
            'ultimate',
            ]
        enemiesActions = ['hit', 'block']
        playerHP = 100
        enemyHP = 100
        print_pause('in order to enter the fight ring you have to pay 1 '
                    'gold do you want to continue'
                    )
        while True:

            # the game asks the player if he has enough
            # gold to enter the game and he
            # can go back if he doesnt have enough gold

            decision1 = \
                input('enter 1 if you want to continue or 2 if '
                      'you want to leave'
                      )
            if decision1 == '1' or decision1 == '2':
                break
            else:
                print('please enter a valid input')

# the game checks if the player has enough gold if not it
# tells him that he doesnt and brings him the the menu

        if decision1 == '1':
            if self.goldqnt < 1:
                print_pause('you dont have enough gold')
            elif self.goldqnt >= 1:
                self.goldqnt -= 1
                print_pause('you have entered the fighting ring')
                print_pause('the fighting ring consists of a fist '
                            'fight game with another contester'
                            )
                print_pause('if you win you gain a title and earn score'
                            )
                print_pause('if you lose the fight you lose score')
                print_pause('the fight will begin now')

                # this is the beginning of the fighting

                while playerHP > 0 and enemyHP > 0:
                    print('your hp:', playerHP)
                    print('enemies hp', enemyHP)
                    print('do you want to strike first or wait for'
                          ' your opponent to strike?')
                    firstHit = \
                        input('enter 1 to strike first or'
                              ' 2 to wait for opponent to strike'
                              )
                    playersLuck = random.choice(listOfLuck)
                    enemiesAction = random.choice(enemiesActions)
                    if firstHit != '1' and firstHit != '2':
                        print('please enter a valid input')

# these are the fight cases if the enemy is going to hit

                    if enemiesAction == 'hit':

                        # these are the cases if the player
                        # decided to hit back

                        if firstHit == '1':
                            if playersLuck == 'correct':
                                print_pause('both of you hit each other')

                                playerHP -= 20
                                enemyHP -= 20
                            elif playersLuck == 'wrong':
                                print_pause('both of you hit each other '
                                            'but the opponents hit '
                                            'was stronger')

                                playerHP -= 30
                                enemyHP -= 15
                            elif playersLuck == 'ultimate':
                                print_pause('both of you hit each other '
                                            'but your hit was stronger')

                                enemyHP -= 30
                                playerHP -= 15

# these are the cases if the player decided to block

                        if firstHit == '2':
                            if playersLuck == 'correct':
                                print_pause('you blocked his hit!')
                            elif playersLuck == 'wrong':
                                print_pause('you failed to block his attack')

                                playerHP -= 50
                            elif playersLuck == 'ultimate':
                                print_pause('you blocked his attack'
                                            ' and countered it!!')

                                enemyHP -= 20
                    elif enemiesAction == 'block':

                        # these are the cases if the enemy is going to block
                        # these are the cases if the player decided to hit

                        if firstHit == '1':
                            if playersLuck == 'correct':
                                print_pause('you landed a hit!')
                                enemyHP -= 25
                            elif playersLuck == 'wrong':
                                print_pause('the enemy blocked your hit')

                            elif playersLuck == 'ultimate':
                                print_pause('you landed a direct hit in '
                                            'the middle of his face!!')

                                enemyHP -= 50

# this is the case if the player decided to block

                        if firstHit == '2':
                            print_pause('both of you hesitated to engage')


# in this part the game checks if either the player won or lost
# i added the following case because sometimes both the player and the
# enemies hp might be in the negative at the same time

                if playerHP < 0 and enemyHP < 0:
                    if playerHP > enemyHP:
                        self.numberOfWins += 1
                        self.score += 25
                        if self.numberOfWins == 1:
                            print_pause('you have earned a title newbie')

                        elif self.numberOfWins == 2:
                            print_pause('you have earned a title rookie')

                        elif self.numberOfWins == 3:
                            print_pause('you have earned a title hero')
                        elif self.numberOfWins == 4:
                            print_pause('you have earned a title champion')
                        print('your score: ' + str(self.score))
                        return self.score
                    elif playerHP < enemyHP:
                        print_pause('you lost this fight but you'
                                    ' can try again'
                                    )
                        self.score -= 10
                        print('your score: ' + str(self.score))
                        return self.score

                # the following if is check if the player lost

                if playerHP <= 0:
                    print_pause('you lost this fight but you can try again'
                                )
                    self.score -= 10
                    print('your score: ' + str(self.score))
                    return self.score
                elif enemyHP <= 0:

                    # the following if checks if the player won

                    print_pause('you won this fight')
                    self.numberOfWins += 1
                    self.score += 25
                    if self.numberOfWins == 1:
                        print_pause('you have earned a title newbie')
                    elif self.numberOfWins == 2:
                        print_pause('you have earned a title rookie')
                    elif self.numberOfWins == 3:
                        print_pause('you have earned a title hero')
                    elif self.numberOfWins == 4:
                        print_pause('you have earned a title champion')
                    print('your score: ' + str(self.score))
                    return self.score
        elif decision1 == '2':
            pass
        else:
            print_pause('enter a valid input')

# the following function checks if the game ended or not

    def checkifwin(self):
        if self.score >= 100:
            print_pause('you earned your freedom back')
            print_pause('you lived the rest of your life peacefully'
                        ' in the woods with your dog'
                        )
            print_pause('you live a happy long life')
            return True
        else:
            return False

    def playAgain(self):
        while True:
            playagain = input('do you want to play again(yes/no)')
            playagain = playagain.lower()
            if playagain == 'yes':
                return True
            elif playagain == 'no':
                return False
            else:
                print('please enter a valid input')

    def leaveGame(self):
        confirmation = input('ARE YOU SURE YOU WANT TO LEAVE THE GAME?'
                             '(yes/no)')
        confirmation = confirmation.lower()
        if confirmation == 'yes':
            return True


# this is the main part of the game

while True:
    while True:
        player1 = game()
        print_pause('welcome to the fight club')
        print_pause('in this game you are locked in a city '
                    'where your freedom is taken from you'
                    )
        print_pause('in order to earn your freedom back'
                    ' you have to get out of the city'
                    )
        print_pause('to get out of the city you have to get'
                    ' score 100 in the fight ring'
                    )
        print_pause('in order to enter the fight ring you must have 1'
                    ' gold to pay as entry fee, you can find gold in caves'
                    )
        while True:
            playersaction = \
                input('do you want to cave or fight or see your inventory(1'
                      ' to cave,2 to fight,3 to check inv,4 leave the game)'
                      )
            if playersaction == '1':
                player1.cave()
            elif playersaction == '2':
                score = player1.fight_ring()
            elif playersaction == '3':
                player1.ShowInv()
            elif playersaction == '4':
                leaveGame = player1.leaveGame()
                if leaveGame is True:
                    exit()

            else:
                print('please enter a valid input')
            gamestate = player1.checkifwin()
            if gamestate is True:
                break

        gameagain = player1.playAgain()
        while True:
            if gameagain is False:
                break
            elif gameagain is True:
                break
            else:
                print('please enter a valid input')
        if gameagain is False:
            print('thank you for playing the game i hope you '
                  'enjoyed playing it')
            break
        else:
            pass
    if gameagain is False:
        break
