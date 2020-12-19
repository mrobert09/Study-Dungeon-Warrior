from random import randint

def add_question():
    """
    Takes in question from user and adds to txt file. This method should not be a part of the question class since the
    questions need to be added to the txt file before creating an instance of the class.
    :return: No return
    """
    file = open('test_questions.txt', 'w')

    # makes counter so user inputs correct amount of answers
    counter = 0
    q_list = []
    while counter < 5:
        if counter == 0:
            q = input('What question would you like to add?\n')
            q_list.append(q)
            counter += 1
        elif counter == 1:
            a = input('What is the actual answer to the question?\n')
            q_list.append(a)
            counter += 1
        else:
            option = input("What other options would you like to add? Try to trick yourself!\n")
            q_list.append(option)
            counter += 1
    add_string = ', '.join(q_list)
    file.write(add_string + '\n')
    add_more = input('Would you like to add another question? Y/N\n')
    if add_more.upper() == 'Y':
        add_question()
    else:
        file.close()

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
        # generates the random question to use
        question = self.generate_question()

        # prints out the question
        self.display_question(question)

        # gathers user input as answer to the question
        user_answer = input('The answer is:\n')

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
        return False
