from random import randint

######################### Game Functions ##############################
# adding game functions to not clutter the Game class
# Not sure if this should be a class
def add_question():
    """
    Takes in question from user and adds to txt file. This method should not be a part of the question class since the
    questions need to be added to the txt file before creating an instance of the class.
    :return: No return
    """
    file = open('test_questions.txt', 'w')

    # makes counter so user inputs correct amount of answers
    q_counter = 0
    q_list = []

    # asks user to input question, correct answer, and 3 other MC options
    # user must input AT LEAST 10 questions, can add more
    # when they are done, exits function and closes file
    while q_counter < 10:
        c_counter = 0
        if q_counter == 0:
            print("Let's get your first question added. The dungeon is waiting...")
        elif 0 < q_counter < 9:
            print(f'You still need to enter in {10 - q_counter} questions. Pick up the pace.')
        else:
            print('After this question you can enter the dungeon at any time.')
        while c_counter < 5:
            if c_counter == 0:
                q = input('What question would you like to add?\n')
                q_list.append(q)
                c_counter += 1
            elif c_counter == 1:
                a = input('What is the actual answer to the question?\n')
                q_list.append(a)
                c_counter += 1
            else:
                option = input("What other options would you like to add? Try to trick yourself!\n")
                q_list.append(option)
                c_counter += 1
        q_counter += 1
        add_string = ', '.join(q_list)
        file.write(add_string + '\n')
        q_list[:] = []
        if q_counter == 10:
            add_more = input('Press Y to enter another question. Press any other button to enter the dungeon.\n')
            if add_more.upper() == 'Y':
                q_counter = 9
            else:
                file.close()


def game_intro():
    """
    Welcomes the player to the game and prompts them to add some trivia questions to begin.
    :return: Nothing
    """
    print('Welcome to Study Dungeon: The dungeon for studying!\n'
          'Before you enter the dungeon, we need some basic information to get started.\n'
          'Please enter at least 10 multiple choice questions that you want to study.\n'
          'First, enter the question. Second, enter the correct answer. Then, enter 3 other options.\n'
          "Make the extra options difficult, the dungeon monsters don't like when you aren't challenged\n"
          'Shall we begin?')

def enter_dungeon():
    """
    The text that plays when the dungeon is entered
    :return: Nothing
    """
    print('You awaken on a cold, stone floor. Still groggy, you stand up and notice the candles on the walls.\n'
          'This is not where you fell asleep. Suddenly, a massive silhouette emerges from the shadows.\n'
          'As it moves in to the light you begin to make out the grotesque features of this monster.\n'
          'It is unlike anything you have ever seen, but something about it is familiar. You realize that it\n'
          'looks very similar to the teacher of the class you were studying for the night before.\n'
          'The monster eventually reaches you and says, "You must answer my questions if you want to have any\n'
          'hope of escaping my dungeon"')

class Questions:
    """
    Stores questions in a list of dictionaries. Used questions are removed from list and added to a storage list.
    Questions are randomly generated and displayed.
    """
    def __init__(self):
        """
        Initializes list of questions and list for storing used questions.
        """
        file = open('test_questions.txt', 'r')
        self._used_questions = []
        self._questions = []
        self._answer_keys = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4
        }

        for line in file:
            line = line.strip()
            storage_dict = {}
            item_list = line.split(', ')
            storage_dict[item_list[0]] = item_list[1:]
            self._questions.append(storage_dict)

    def generate_question(self):
        """
        Uses random module to generate a random question. Prints the question in multiple choice format.
        :return: no return value
        """
        # set of possible choices to be used as list indices
        choices = [0, 1, 2, 3]

        # generates random integer as a list index
        full_question = self._questions[randint(0, len(self._questions) - 1)]

        # returns random number from choices set. Needs to be random so correct answer isn't always A
        choice1 = choices.pop(randint(0, len(choices) - 1))
        choice2 = choices.pop(randint(0, len(choices) - 1))
        choice3 = choices.pop(randint(0, len(choices) - 1))
        choice4 = choices.pop(randint(0, len(choices) - 1))

        question_list = []
        # appends question and answers to the list to be used by later method
        for question, answer in full_question.items():
            question_list.append(question)
            question_list.append(answer[choice1])
            question_list.append(answer[choice2])
            question_list.append(answer[choice3])
            question_list.append(answer[choice4])

        return question_list

    def display_question(self, question):
        """
        Prints out question in clean multiple choice format.
        :param question: list from generate_question
        :return: no return value
        """
        print(question[0] + "\n" + f'A. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}')

    def answer_question(self):
        """
        Gets the random question and uses helper method to print it out. Allows user to answer the question.
        Determines if answer is correct or not. If answer is correct, question is removed from the list of questions
        that can be generated and added to a list of used questions.
        :return: boolean (whether the question was answered correctly or not)
        """
        if self._questions:
            # generates the random question to use
            question = self.generate_question()

            # prints out the question
            self.display_question(question)

            # gathers user input as answer to the question
            user_answer = input('The answer is:\n')

            while user_answer:
                if 'A' <= user_answer.upper() <= 'D':
                    # maps the user input to a list index to be used
                    question_index = self._answer_keys[user_answer.upper()]

                    # finds the question that was asked
                    for dictionary in self._questions:
                        if question[0] in dictionary:
                            key_question = dictionary

                    correct_answer = key_question[question[0]][0] == question[question_index]
                    if correct_answer:
                        for index, dictionary in enumerate(self._questions):
                            if key_question == dictionary:
                                adder = self._questions.pop(index)
                                self._used_questions.append(adder)
                        return True
                    else:
                        print('WRONG!')
                        return False

                else:
                    user_answer = input('Not a valid answer. Try again.\n')
        else:
            print('No questions available yet. Please add some.')
            return False


class Character():
    """This is the class that defines player characters"""

    def __init__(self, hp=10, atk=1, lvl=1, exp=0):
        """this initializes the player character"""
        self.hp = hp
        self.atk = atk
        self.max_hp = hp
        self.lvl = lvl
        self.exp = exp

    def take_dmg(self, dmg):
        """takes an int amount of damage dealt to character, can take negative number for
        gaining health
        """
        self.hp -= dmg

    def gain_exp(self, amt):
        """gains the amount of experience inputted, if it goes over 10 times the level then levels up
        and resets exp appropriately"""
        self.exp += amt
        if self.exp >= (self.lvl * 10):
            self.lvl_up()

    def lvl_up(self):
        """levels up, assumes that experience is greater than or equal to 10 times level"""
        if self.exp < 10 * self.lvl:
            return
        self.exp -= 10*(self.lvl)
        self.lvl += 1

    def get_hp(self):
        """returns the current amount of health"""
        return self.hp

    def get_max_hp(self):
        """returns the max health of character"""
        return self.max_hp

    def get_atk_dmg(self):
        """returns the amount of damage character does when it gets correct answer"""
        return self.atk

class Game:
    """
    Where the game is played.
    """
    def __init__(self):
        game_intro()
        add_question()
        enter_dungeon()

g = Game()
