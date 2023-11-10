import pygame
from game import singleplayer, multiplayer


# Creating an interface function, that creates the GUI
def interface():
    """Creates the GUI of the game.

    The interface displays a menu page, which will take the user's input and direct them to their desired destination.
    It defines and displays a background image, as well as texts and rectangles (which represent buttons), and provides
    feedback to certain types of input/interaction from the user.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Initiating pygame
    pygame.init()

    # Creating the screen 1280x720 pixels
    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    # Creating some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)

    # Saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()

    # Creating some text labels
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    font2 = pygame.font.Font('fonts/evil_empire.ttf', 120)
    singleplayer_text = font1.render('Singleplayer', True, white)
    multiplayer_text = font1.render('Multiplayer', True, white)
    rules_text = font1.render('Rules', True, white)
    credits_text = font1.render('Credits', True, white)
    quit_text = font1.render('Quit', True, white)
    title_text = font2.render('Highway Racer', True, yellow)

    # Creating image variable
    menu_background = pygame.image.load('images/menu_img.jpg')

    # Loading menu music into pygame.mixer
    pygame.mixer.music.load('music/rock_it.mp3')

    # Play background music
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Interface loop
    while True:
        # Getting the input of the user
        for ev in pygame.event.get():

            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(width)
                print(height)
                if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
                    pygame.quit()

            # Press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 520 <= mouse[1] <= 570:
                    credits_()

            # Press the rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 420 <= mouse[1] <= 470:
                    rules()

            # Press the singleplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 220 <= mouse[1] <= 270:
                    singleplayer()

            # Press the multiplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 320 <= mouse[1] <= 370:
                    multiplayer()

        # Setting the background color as black
        screen.fill(black)

        # Set background image
        screen.blit(menu_background, (0, 0))

        # Create mouse variable, which fetches position of the mouse
        mouse = pygame.mouse.get_pos()

        # Print the buttons text and the box(color changing)

        # Singleplayer text
        # When the mouse is on the box it changes color
        if 280 <= mouse[0] <= 560 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, green, [280, 220, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 220, 280, 50])
        screen.blit(singleplayer_text, (288, 226))

        # Multiplayer text
        if 280 <= mouse[0] <= 560 and 320 <= mouse[1] <= 370:
            pygame.draw.rect(screen, green, [280, 320, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 320, 280, 50])
        screen.blit(multiplayer_text, (299, 326))

        # Rules text
        if 280 <= mouse[0] <= 560 and 420 <= mouse[1] <= 470:
            pygame.draw.rect(screen, green, [280, 420, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 420, 280, 50])
        screen.blit(rules_text, (362, 426))

        # Credits text
        if 280 <= mouse[0] <= 560 and 520 <= mouse[1] <= 570:
            pygame.draw.rect(screen, yellow, [280, 520, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 520, 280, 50])
        screen.blit(credits_text, (340, 526))

        # Quit text
        if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
            pygame.draw.rect(screen, red, [280, 620, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 620, 280, 50])
        screen.blit(quit_text, (374, 626))

        # TITLE TEXT
        screen.blit(title_text, (100, 20))

        # Pygame built-in function that updates the screen at every iteration of the loop
        pygame.display.update()


def credits_():
    """Displays the credits interface.

    The credits interface displays a page that shows who the developers of this project are.
    It displays a background image, texts and a rectangle that works as a back button for the user to return to the
    main menu interface.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Define resolution
    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    # Define some colors (RGB)
    white = (255, 255, 255)
    red = (255, 0, 0)
    color_dark = (100, 100, 100)

    # Define text labels
    creditsfont = pygame.font.Font('fonts/quaaykop.ttf', 40)
    backfont = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    titlefont = pygame.font.Font('fonts/quaaykop.ttf', 70)
    title_text = titlefont.render('Project developed by:', True, white)
    back_text = backfont.render('Back', True, white)
    member1_text = creditsfont.render('Thiago Sakamoto - 20211556@novaims.unl.pt', True, white)
    member2_text = creditsfont.render('Miguel Estêvão - 20211559@novaims.unl.pt', True, white)
    professors_text = creditsfont.render('(Base code developed by our professors at NOVA IMS)', True, white)

    # Creating image variable
    credits_background = pygame.image.load('images/credits_img.jpg')

    # Interface loop
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Press on back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
                    interface()

        # Fill screen with black
        screen.fill((0, 0, 0))

        # Show background
        screen.blit(credits_background, (0, 0))

        # Credits text
        screen.blit(title_text, (60, 40))
        screen.blit(member1_text, (20, 300))
        screen.blit(member2_text, (20, 200))
        screen.blit(professors_text, (20, 400))

        # Back button text
        if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
            pygame.draw.rect(screen, red, [280, 620, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 620, 280, 50])
        screen.blit(back_text, (374, 626))

        # Update display
        pygame.display.update()


def rules():
    """Displays the rules interface.

    The rules interface displays a page with the rules of the game. It displays a background image, texts and a
    rectangle that works as a back button for the user to return to the main menu interface.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Define resolution
    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    # Create some color variables
    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 153)
    color_dark = (100, 100, 100)

    # Create some text labels
    textfont = pygame.font.Font('fonts/quaaykop.ttf', 40)
    powerupfont = pygame.font.Font('fonts/quaaykop.ttf', 25)
    backfont = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    titlefont = pygame.font.Font('fonts/quaaykop.ttf', 70)
    title_text = titlefont.render('Game Rules:', True, white)
    back_text = backfont.render('Back', True, white)
    rule1_text = textfont.render('- Use arrow keys to move car (left/right/up/down) (or w/a/s/d for multiplayer)',
                                 True, white)
    rule2_text = textfont.render('- Avoid crashing with other cars in order to survive', True, white)
    rule3_text = textfont.render('- Collect powerups to enhance your gameplay experience:', True, white)
    rule4_text = powerupfont.render('BLUE - Gain temporary invincibility |   GREEN - Slows down cars |   '
                                    'RED - Shrinks your car |   PINK - Clears all cars around you', True, yellow)
    rule5_text = textfont.render('- OBS: Only 1 powerup can be active at a time', True, white)

    # Define image variable
    credits_background = pygame.image.load('images/credits_img.jpg')

    # Interface loop
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # Press on back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
                    interface()

        # Fill screen with black
        screen.fill((0, 0, 0))

        # Show background
        screen.blit(credits_background, (0, 0))

        # Credits text
        screen.blit(title_text, (60, 40))
        screen.blit(rule1_text, (20, 140))
        screen.blit(rule2_text, (20, 240))
        screen.blit(rule3_text, (20, 340))
        screen.blit(rule4_text, (20, 420))
        screen.blit(rule5_text, (20, 500))

        # Back button text
        if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
            pygame.draw.rect(screen, red, [280, 620, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 620, 280, 50])
        screen.blit(back_text, (374, 626))

        # Update display
        pygame.display.update()
