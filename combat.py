import pygame
from settings import *
from random import randint
from gameover import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Button:
    """Creation and methods for handling buttons"""

    def __init__(self, color, x, y, width, height, label, text='', font = oswfont32, text_color = BLACK):
        """
        Initializes a button of 'color' color, with the upper left corner at x,y 
        width and height determine size of button
        text is what should be said inside the button
        """
        self.color = color
        self.original_color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_label = label

    def draw_button(self, surface):
        """Call this method to draw the button onto the given surface"""
        pygame.draw.rect(surface, self.color, self.rectangle)

        if self.text != '':
            text = self.font.render(self.text, True, self.text_color)
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    
    def is_hover(self):
        """Returns boolean if mouse is over the button"""
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] > self.x and mouse_position[0] < (self.x + self.width) and mouse_position[1] > self.y and mouse_position[1] < (self.y + self.height):
            return True
        else:
            return False

    def mouse_hover_color(self, hover_color):
        """Changes the color of the button when the mouse is hovering over it"""
        if self.is_hover():
            self.color = hover_color
        else:
            self.color = self.original_color

    def set_color(self, color):
        """Change the color of the button"""
        self.color = color

    def is_clicked_on(self):
        """Checks if the button has been clicked on and returns boolean"""
        if self.is_hover() == True:
            return True
        return False
    
    def get_label(self):
        """returns the button's label (A, B, C, etc)"""
        return self.button_label

class MultipleChoiceBox:
    """Creates a MultipleChoiceBox object (add better docstring)"""

    def __init__(self, box_color, border_color, x, y, width, height, surface, text_font):
        """
        Initializes a MultipleChoiceBox
        upper left corner at coordinates x, y
        width = # of pixels wide
        height = # of pixels tall
        box_color = color of the box
        border_color =  color of the border
        surface = on which surface the MultipleChoiceBox should appear
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box_color = box_color
        self.border_color = border_color
        self.surface = surface
        self.font = text_font
        self.rectangle = pygame.Rect(x, y, width, height)
        self.rectangle_outline = pygame.Rect(x-2, y-2, width+4, height+4)
        self.response_A = ''
        self.response_B = ''
        self.response_C = ''
        self.response_D = ''
        self.response_E = ''
        self.correct_response = ''
        self.button_A = Button(BLACK, self.x + 10, self.y + 120, self.width -20, 50, "A", text = self.response_A, text_color = WHITE)
        self.button_B = Button(BLACK, self.x + 10, self.y + 180, self.width -20, 50, "B", text = self.response_B, text_color = WHITE)
        self.button_C = Button(BLACK, self.x + 10, self.y + 240, self.width -20, 50, "C", text = self.response_C, text_color = WHITE)
        self.button_D = Button(BLACK, self.x + 10, self.y + 300, self.width -20, 50, "D", text = self.response_D, text_color = WHITE)
        self.button_E = Button(BLACK, self.x + 10, self.y + 360, self.width -20, 50, "E", text = self.response_D, text_color = WHITE)
        self.buttons_list = [self.button_A, self.button_B, self.button_C, self.button_D, self.button_E]

    def draw_background(self):
        """Draws the background text box on top of given surface"""
        #pygame.draw.rect(<name of surface>, <color of fill>, <dimensions (x,y,width,height)>, <optional: rounded corner radius>)
        pygame.draw.rect(self.surface, self.border_color, self.rectangle_outline)
        pygame.draw.rect(self.surface, self.box_color, self.rectangle)

    def draw_text(self, surface, text, color, rectangle, font, aa = True, bkg = None): #https://www.pygame.org/wiki/TextWrap 
        """
        Will draw text and wrap it to following line if text is larger than container
        surface = surface for text to be drawn on
        text = a string of text to be displayed
        color = color of text
        rectangle = size of textbox as (x, y, width, height) with x, y marking upper left corner
        font = font style
        aa = antialiasing, determines if text is smoothed or not. Used for the font.render method
        bkg = background
        """
        rectangle = pygame.Rect(rectangle)
        y = rectangle.top
        line_spacing = -2

        #get the height of the font. 'font.size(<text>)' returns the height and width of the text as a tuple ('T' and 'g' are tall and deep letters)
        font_height = font.size("Tg")[1] 

        while text:
            i = 1

            #determine if the row of text will be outside the area
            if y + font_height > rectangle.bottom:
                break

            #determine maximum width of line
            while font.size(text[:i])[0] < rectangle.width and i < len(text):
                i += 1
            
            #if text is wrapped, adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1 #rfind is a string method. It finds the index of the last instance of a value string.rfind(<value>, <startindex>, <endindex>)

            #render the line and blit it to the surface
            text_render = font.render(text[:i], aa, color)

            surface.blit(text_render, (rectangle.left, y))
            y += font_height + line_spacing

            #remove the text we just blitted
            text = text[i:]

        return text

    def set_read_text(self, text):
        """Sets the text which will be displayed at the top of the box"""
        self.read_text = text

    def get_read_text(self):
        """Returns the question text"""
        return self.read_text

    def set_response_A(self, text):
        """Sets the text which will appear in button A"""
        self.response_A = text
        self.button_A = Button(BLACK, self.x + 10, self.y + 120, self.width -20, 50, "A", text = self.response_A, text_color = WHITE)

    def set_response_B(self, text):
        """Sets the text which will appear in button B"""
        self.response_B = text
        self.button_B = Button(BLACK, self.x + 10, self.y + 180, self.width -20, 50, "B", text = self.response_B, text_color = WHITE)

    def set_response_C(self, text):
        """Sets the text which will appear in button C"""
        self.response_C = text
        self.button_C = Button(BLACK, self.x + 10, self.y + 240, self.width -20, 50, "C", text = self.response_C, text_color = WHITE)

    def set_response_D(self, text):
        """Sets the text which will appear in button D"""
        self.response_D = text
        self.button_D = Button(BLACK, self.x + 10, self.y + 300, self.width -20, 50, "D", text = self.response_D, text_color = WHITE)

    def set_response_E(self, text):
        """Sets the text which will apper in button E"""
        self.response_E = text
        self.button_E = Button(BLACK, self.x + 10, self.y + 360, self.width -20, 50, "E", text = self.response_E, text_color = WHITE)

    def set_correct_response(self, response):
        """Stores the correct response"""
        self.correct_response = response

    def get_correct_response(self):
        """Returns correct response"""
        return self.correct_response

    def draw_read_text(self):
        """Draws the question text at the top of the MultipleChoiceBox"""
        text_boundary = pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height)
        self.draw_text(self.surface, self.read_text, BLACK, text_boundary, self.font)
    
    def display_MultipleChoiceBox(self):
        """A function to display the MultipleChoiceBox and all of its contents in the game loop"""
        self.draw_background()
        self.draw_read_text()
        self.button_A.draw_button(screen)
        self.button_B.draw_button(screen)
        self.button_C.draw_button(screen)
        self.button_D.draw_button(screen)
        self.button_E.draw_button(screen)
    
    def answer_clicked(self):
        for button in self.buttons_list:
            if button.is_clicked_on() == True:
               return button.get_label()
        return False

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
        self._single_question = None
        self._questions = []
        self._answer_keys = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5
        }
        self.mcbox = MultipleChoiceBox(WHITE, BLACK, 100, 70, 400, 420, screen, oswfont32) #coordinates to center MultipleChoiceBox on room

        for line in file:
            line = line.strip()
            item_list = line.split(', ')
            self._questions.append(item_list)
            # storage_dict[item_list[0]] = item_list[1:]
            # self._questions.append(storage_dict)

    def get_questions(self):
        """Returns list of questions"""
        return self._questions

    def generate_question(self):
        """
        Uses random module to generate a random question. Returns list with question at index 0 followed by 4 multiple choice answers
        """
        # set of possible choices to be used as list indices
        choices = [1, 2, 3, 4]

        # generates random integer as a list index
        if self._questions:
            full_question = self._questions[randint(0, len(self._questions) - 1)]
            self.mcbox.set_correct_response(full_question[1])
        else:
            print('NO MORE QUESTIONS')

        # returns random number from choices set. Needs to be random so correct answer isn't always A
        choice1 = choices.pop(randint(0, len(choices) - 1))
        choice2 = choices.pop(randint(0, len(choices) - 1))
        choice3 = choices.pop(randint(0, len(choices) - 1))
        choice4 = choices.pop(randint(0, len(choices) - 1))

        question_list = []
        self._single_question = question_list
        # appends question and answers to the list to be used by later method

        question_list.append(full_question[0])
        question_list.append(full_question[choice1])
        question_list.append(full_question[choice2])
        question_list.append(full_question[choice3])
        question_list.append(full_question[choice4])
        question_list.append('POWER UP IS OVER 9000')

        #Prepare the multiple choice box with the appropriate text
        self.mcbox.set_read_text(question_list[0])
        self.mcbox.set_response_A(question_list[1])
        self.mcbox.set_response_B(question_list[2])
        self.mcbox.set_response_C(question_list[3])
        self.mcbox.set_response_D(question_list[4])
        self.mcbox.set_response_E("Use a powerup")

    def display_question(self):
        """Draws question multiple choice box on screen"""
        self.mcbox.display_MultipleChoiceBox()

    def answer_question(self, answer):
        """
        Gets the random question and uses helper method to print it out. Allows user to answer the question.
        Determines if answer is correct or not. If answer is correct, question is removed from the list of questions
        that can be generated and added to a list of used questions.
        :return: boolean (whether the question was answered correctly or not)
        """

        # maps the user input to a list index to be used
        question_index = self._answer_keys[answer.upper()]

        correct_answer = self.mcbox.get_correct_response()

        if correct_answer == self._single_question[question_index]:
            for index, question in enumerate(self._questions):
                if question[0] == self._single_question[0]:
                    remove_q = self._questions.pop(index)
                    self._used_questions.append(remove_q)
                    return True
        return False

questions = Questions()

def ask_a_question():
    """Generates and displays an interactive multiple choice question box"""
    questions.generate_question()
    answered = False
    is_correct = False

    while answered == False:
        questions.display_question()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_combat = False
                running = False

            if event.type == pygame.MOUSEMOTION:
                questions.mcbox.button_A.mouse_hover_color(LIGHTGREY)
                questions.mcbox.button_B.mouse_hover_color(LIGHTGREY)
                questions.mcbox.button_C.mouse_hover_color(LIGHTGREY)
                questions.mcbox.button_D.mouse_hover_color(LIGHTGREY)
                questions.mcbox.button_E.mouse_hover_color(LIGHTGREY)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if questions.mcbox.answer_clicked() != False:
                    if questions.answer_question(questions.mcbox.answer_clicked()) == True:
                        print("Correct answer pressed")
                        pygame.mixer.Sound.play(hiyaa)
                        answered = True
                        correct = True
                        return is_correct
                    elif questions.mcbox.answer_clicked() == 'E':
                        answered = True
                        print('POWER UP OVER 9000')
                    else:
                        answered = True
                        pygame.mixer.Sound.play(oof)
                        game_over()
                        return is_correct
                        

        pygame.display.update()
