import pygame

# Initialize game
pygame.init()

# Create Game Window (pixels x-axis, pixels y-axis)
screen = pygame.display.set_mode((800, 600))

#Text Stuff
oswfont32 = pygame.font.Font("Fonts/Oswald-VariableFont_wght.ttf", 32)

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)

class Button:
    """Creation and methods for handling buttons"""

    def __init__(self, color, x, y, width, height, text='', font = oswfont32, text_color = BLACK):
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

    # def set_text_color(self, color):
    #     """Changes the color of the text. RGB"""
    #     self.text_color = color

    def draw_button(self, surface):
        """Call this method to draw the button onto the given surface"""
        pygame.draw.rect(surface, self.color, self.rectangle)

        if self.text != '':
            text = self.font.render(self.text, True, self.text_color)
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_hover_color(self, hover_color):
        """Changes the color of the button when the mouse is hovering over it"""
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] > self.x and mouse_position[0] < (self.x + self.width) and mouse_position[1] > self.y and mouse_position[1] < (self.y + self.height):
                self.color = hover_color
        else:
            self.color = self.original_color

class TextBox:
    """Creates a TextBox object (add better docstring)"""

    def __init__(self, box_color, border_color, x, y, width, height, surface, text_font):
        """
        Initializes a Textbox 
        upper left corner at coordinates x, y
        width = # of pixels wide
        height = # of pixels tall
        box_color = color of the box
        border_color =  color of the border
        surface = on which surface the textbox should appear
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
        self.button_A = Button(BLACK, self.x + 10, self.y + 120, self.width -20, height = 50, text = self.response_A, text_color = WHITE)
        self.button_B = Button(BLACK, self.x + 10, self.y + 180, self.width -20, height = 50, text = self.response_B, text_color = WHITE)
        self.button_C = Button(BLACK, self.x + 10, self.y + 240, self.width -20, height = 50, text = self.response_C, text_color = WHITE)
        self.button_D = Button(BLACK, self.x + 10, self.y + 300, self.width -20, height = 50, text = self.response_D, text_color = WHITE)
        self.button_E = Button(BLACK, self.x + 10, self.y + 360, self.width -20, height = 50, text = self.response_D, text_color = WHITE)
        self.buttons_list = [self.button_A, self.button_B, self.button_C, self.button_D]

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

    def set_response_A(self, text):
        """Sets the text which will appear in button A"""
        self.response_A = f'A) {text}'
        self.button_A = Button(BLACK, self.x + 10, self.y + 120, self.width -20, 50, text = self.response_A, text_color = WHITE)

    def set_response_B(self, text):
        """Sets the text which will appear in button B"""
        self.response_B = f'B) {text}'
        self.button_B = Button(BLACK, self.x + 10, self.y + 180, self.width -20, 50, text = self.response_B, text_color = WHITE)

    def set_response_C(self, text):
        """Sets the text which will appear in button C"""
        self.response_C = f'C) {text}'
        self.button_C = Button(BLACK, self.x + 10, self.y + 240, self.width -20, 50, text = self.response_C, text_color = WHITE)

    def set_response_D(self, text):
        """Sets the text which will appear in button D"""
        self.response_D = f'D) {text}'
        self.button_D = Button(BLACK, self.x + 10, self.y + 300, self.width -20, 50, text = self.response_D, text_color = WHITE)

    def set_response_E(self, text):
        """Sets the text which will apper in button E"""
        self.response_E = text
        self.button_E = Button(BLACK, self.x + 10, self.y + 360, self.width -20, 50, text = self.response_E, text_color = WHITE)

    def draw_read_text(self):
        """Draws the read text at the top of the Textbox"""
        text_boundary = pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height)
        self.draw_text(self.surface, self.read_text, BLACK, text_boundary, self.font)
    
    def display_textbox(self):
        """A function to display the textbox and all of its contents"""
        self.draw_background()
        self.draw_read_text()
        self.button_A.draw_button(screen)
        self.button_B.draw_button(screen)
        self.button_C.draw_button(screen)
        self.button_D.draw_button(screen)
        self.button_E.draw_button(screen)

question = TextBox(WHITE, BLACK, 100, 70, 400, 420, screen, oswfont32)
question.set_read_text("What is the atomic number for Helium?")
question.set_response_A("2")
question.set_response_B("4")
question.set_response_C("3")
question.set_response_D("10")
question.set_response_E("Use a powerup")

# Game Loop
running = True
while running:

    screen.fill(WHITE)

    question.display_textbox()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            question.button_A.mouse_hover_color(GREY)
            question.button_B.mouse_hover_color(GREY)
            question.button_C.mouse_hover_color(GREY)
            question.button_D.mouse_hover_color(GREY)
            question.button_E.mouse_hover_color(GREY)
    
    pygame.display.update()
