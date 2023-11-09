from powerups import *

# Create a pause variable to monitor if the game is paused or not
pause = False


def singleplayer():
    """The game itself, in singleplayer mode.

    This function defines and displays the game's interface for the singleplayer mode, and also defines the general
    rules and functionalities that determine how the game should work.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Initiate pygame
    pygame.init()

    # Loading menu music into pygame.mixer
    pygame.mixer.music.load('music/rock_it.mp3')

    # Play background music
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Retrieve global variable pause
    global pause

    # Define some color variables
    grey = (128, 128, 128)
    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (100, 100, 255)
    pink = (255, 174, 240)
    green = (142, 235, 145)

    # Define a font style
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 50)

    # Create a list with the images that will be used for the NPC cars
    image_list = ['images/car1.png', 'images/car2.png', 'images/car3.png', 'images/car4.png', 'images/car5.png']

    # Creating sound effect variable
    crash_sound = pygame.mixer.Sound('music/crash.wav')
    pygame.mixer.Sound.set_volume(crash_sound, 0.3)

    # Create variable for grass background image
    grass = pygame.image.load('images/grass.jpg')

    # Set default speed to 1
    speed = 1

    # Define screen resolution
    screenwidth = 1280
    screenheight = 720
    size = (screenwidth, screenheight)
    screen = pygame.display.set_mode(size)

    # Set caption
    pygame.display.set_caption("Highway Racer")

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Create all car objects
    playerCar = Car(70, 'images/player_car.png', 60, 110)
    playerCar.rect.x = 607
    playerCar.rect.y = screenheight - 100

    playerCar_copy = Car(70, 'images/player_car.png', 60, 110)

    smallCar = Car(70, 'images/player_car.png', 30, 50)

    car1 = Car(random.randint(40, 100), 'images/car1.png', 60, 110)
    car1.rect.x = 358
    car1.rect.y = -50

    car2 = Car(random.randint(40, 100), 'images/car2.png', 60, 110)
    car2.rect.x = 455
    car2.rect.y = -600

    car3 = Car(random.randint(40, 100), 'images/car3.png', 60, 110)
    car3.rect.x = 555
    car3.rect.y = -350

    car4 = Car(random.randint(40, 100), 'images/car4.png', 60, 110)
    car4.rect.x = 655
    car4.rect.y = -900

    car5 = Car(random.randint(40, 100), 'images/car5.png', 60, 110)
    car5.rect.x = 755
    car5.rect.y = -800

    car6 = Car(random.randint(40, 100), 'images/car6.png', 60, 110)
    car6.rect.x = 855
    car6.rect.y = -1000

    # Create all powerup objects
    invincibility = InvincibilityPower(30, 30, 75, blue)
    slowing = SlowingPower(30, 30, 75, green)
    shrinking = ShrinkingPower(30, 30, 75, red)
    kill = KillPower(30, 30, 75, pink)

    # Spawn powerups (set their rectangular coordinates)
    invincibility.spawn()
    slowing.spawn()
    shrinking.spawn()
    kill.spawn()

    # Add the cars and powerups to the list of all sprites
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(car5)
    all_sprites_list.add(car6)
    all_sprites_list.add(invincibility)
    all_sprites_list.add(slowing)
    all_sprites_list.add(shrinking)
    all_sprites_list.add(kill)

    # Add the NPC cars to the list of all coming cars
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)
    all_coming_cars.add(car5)
    all_coming_cars.add(car6)

    # Add the powerups to the list of all spawned powerups
    all_spawned_powerups = pygame.sprite.Group()
    all_spawned_powerups.add(invincibility)
    all_spawned_powerups.add(slowing)
    all_spawned_powerups.add(shrinking)
    all_spawned_powerups.add(kill)

    # Allowing the user to close the window...
    carryOn = True

    # Initiate pygame time clock and fetch the start time
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Set initial collision time to 1000000 (a random high value to ensure that the collision effects aren't applied
    # early in the game)
    collision_time = 1000000

    # Define invincible variable to reflect the invincibility status
    invincible = False

    # Define powerup_active variable to reflect whether a powerup is active or not
    powerup_active = False

    # Interface loop
    while carryOn:
        # Getting the input of the user
        for event in pygame.event.get():
            # Press on exit button
            if event.type == pygame.QUIT:
                carryOn = False

            elif event.type == pygame.KEYDOWN:
                # Press the 'x' key
                if event.key == pygame.K_x:
                    carryOn = False

                # Press the 'esc' key (to access pause menu)
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

        # Define current time and elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 100

        # Check if movement keys are being pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            playerCar.moveForward(5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            playerCar.moveBackward(5)

        # Game Logic
        for car in all_coming_cars:
            # Make car move downwards
            car.moveNPC(speed)

            # If car leaves the screen
            if car.rect.y > screenheight:
                # Update car speed, image and y position
                car.changeSpeed(random.randint(50, 120))
                car.repaint(random.choice(image_list), 60, 120)
                car.rect.y = random.randint(-500, -200)

            # Check if there is a car collision (if invincibility is not active)
            if not invincible:
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    print("Car crash!")
                    # Play crash sound
                    crash_sound.play()
                    # Stop background music
                    pygame.mixer.music.pause()
                    # End Of Game. Send player to game over screen
                    game_over()

        for powerup in all_spawned_powerups:
            # Make powerup move downwards
            powerup.move(speed)
            # If powerup leaves the screen and is not active, spawn it again
            if powerup.rect.y > screenheight and not powerup_active:
                powerup.spawn()

            # Check if player collides with a powerup
            powerup_collision_list = pygame.sprite.spritecollide(playerCar, all_spawned_powerups, False)
            for powerup in powerup_collision_list:
                # Check if there isn't any powerups active
                if not powerup_active:
                    # Create variable to check the last powerup collision
                    last_powerup = ''
                    # Respawn the powerup
                    powerup.spawn()
                    # Fetch the time in which the collision happened
                    collision_time = pygame.time.get_ticks()

                    if powerup == invincibility:
                        # If powerup collected was invincibility, then update the status variables and apply effects.
                        invincible = True
                        powerup_active = True
                        last_powerup = 'invincibility'
                        powerup.affect_player(playerCar)

                    elif powerup == slowing:
                        # If powerup collected was slowing, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'slowing'
                        playerCar.repaint('images/slowed_car.png', 60, 110)
                        powerup.affect_traffic(car1)
                        powerup.affect_traffic(car2)
                        powerup.affect_traffic(car3)
                        powerup.affect_traffic(car4)
                        powerup.affect_traffic(car5)
                        powerup.affect_traffic(car6)

                    elif powerup == shrinking:
                        # If powerup collected was shrinking, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'shrinking'
                        powerup.affect_player(playerCar)
                        # Substitute the playerCar with the smallCar, and then update the playerCar
                        smallCar.rect.x = playerCar.rect.x
                        smallCar.rect.y = playerCar.rect.y
                        all_sprites_list.remove(playerCar)
                        all_sprites_list.add(smallCar)
                        playerCar = smallCar
                        playerCar.update()

                    elif powerup == kill:
                        # If powerup collected was kill, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'kill'
                        playerCar.repaint('images/kill_car.png', 60, 110)
                        powerup.affect_traffic(car1)
                        powerup.affect_traffic(car2)
                        powerup.affect_traffic(car3)
                        powerup.affect_traffic(car4)
                        powerup.affect_traffic(car5)
                        powerup.affect_traffic(car6)

        # Define for how long the powerups will be active, then determine what will happen after they become inactive
        if current_time - collision_time > 6000:
            # Set collision time to 1000000 again
            collision_time = 1000000

            if last_powerup == 'invincibility':
                # If the last active powerup was invincibility, then update status variables and revert the effects.
                invincible = False
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)

            elif last_powerup == 'slowing':
                # If the last active powerup was slowing, then update status variables and revert the effects.
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)
                car1.changeSpeed(random.randint(50, 100))
                car2.changeSpeed(random.randint(50, 100))
                car3.changeSpeed(random.randint(50, 100))
                car4.changeSpeed(random.randint(50, 100))
                car5.changeSpeed(random.randint(50, 100))
                car6.changeSpeed(random.randint(50, 100))

            elif last_powerup == 'shrinking':
                # If the last active powerup was shrinking, then update status variables and revert the effects.
                powerup_active = False
                # Substitute the playerCar with a copy of it, then update playerCar
                playerCar_copy.rect.x = playerCar.rect.x
                playerCar_copy.rect.y = playerCar.rect.y
                all_sprites_list.remove(playerCar)
                all_sprites_list.add(playerCar_copy)
                playerCar = playerCar_copy
                playerCar.update()

            elif last_powerup == 'kill':
                # If the last active powerup was kill, then update status variables and revert the effects.
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)
                car1.rect.y = random.randint(-300, -100)
                car2.rect.y = random.randint(-300, -100)
                car3.rect.y = random.randint(-300, -100)
                car4.rect.y = random.randint(-300, -100)
                car5.rect.y = random.randint(-300, -100)
                car6.rect.y = random.randint(-300, -100)
                all_sprites_list.add(car1)
                all_sprites_list.add(car2)
                all_sprites_list.add(car3)
                all_sprites_list.add(car4)
                all_sprites_list.add(car5)
                all_sprites_list.add(car6)
                all_coming_cars.add(car1)
                all_coming_cars.add(car2)
                all_coming_cars.add(car3)
                all_coming_cars.add(car4)
                all_coming_cars.add(car5)
                all_coming_cars.add(car6)

            # Create a playerCar_copy variable here, in order for it to be reset after each change related to it.
            playerCar_copy = Car(70, 'images/player_car.png', 60, 110)

        # Update all sprites list
        all_sprites_list.update()

        # Drawing on Screen
        screen.blit(grass, (0, 0))

        # Draw The Road
        pygame.draw.rect(screen, grey, [325, 0, 610, screenheight])

        # Draw Line paintings on the road
        pygame.draw.line(screen, yellow, [435, 0], [435, screenheight], 5)
        pygame.draw.line(screen, yellow, [535, 0], [535, screenheight], 5)
        pygame.draw.line(screen, yellow, [635, 0], [635, screenheight], 5)
        pygame.draw.line(screen, yellow, [735, 0], [735, screenheight], 5)
        pygame.draw.line(screen, yellow, [835, 0], [835, screenheight], 5)

        # Marker size and edge markers
        marker_width = 15
        left_edge_marker = (325, 0, marker_width, screenheight)
        right_edge_marker = (935, 0, marker_width, screenheight)

        # Draw the edge markers
        pygame.draw.rect(screen, white, left_edge_marker)
        pygame.draw.rect(screen, white, right_edge_marker)

        # Draw all the sprites in one go
        all_sprites_list.draw(screen)

        # Create and display score texts in game
        text = font1.render(f"Score:", True, blue)
        text2 = font1.render(f"{int(elapsed_time)}", True, blue)
        screen.blit(text, (15, 20))
        screen.blit(text2, (70, 80))

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(60)

    pygame.quit()


def multiplayer():
    """The game itself, in multiplayer mode.

    This function defines and displays the game's interface for the multiplayer mode, and also defines the general
    rules and functionalities that determine how the game should work.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Initiate pygame
    pygame.init()

    # Loading menu music into pygame.mixer
    pygame.mixer.music.load('music/rock_it.mp3')

    # Play background music
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # Retrieve global variable pause
    global pause

    # Define some color variables
    grey = (128, 128, 128)
    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (100, 100, 255)
    pink = (255, 174, 240)
    green = (142, 235, 145)

    # Define a font style
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 50)

    # Create a list with the images that will be used for the NPC cars
    image_list = ['images/car1.png', 'images/car2.png', 'images/car3.png', 'images/car4.png', 'images/car5.png']

    # Creating sound effect variable
    crash_sound = pygame.mixer.Sound('music/crash.wav')
    pygame.mixer.Sound.set_volume(crash_sound, 0.3)

    # Create variable for grass background image
    grass = pygame.image.load('images/grass.jpg')

    # Set default speed to 1
    speed = 1

    # Define screen resolution
    screenwidth = 1280
    screenheight = 720
    size = (screenwidth, screenheight)
    screen = pygame.display.set_mode(size)

    # Set caption
    pygame.display.set_caption("Car Racing")

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Create all car objects
    playerCar = Car(70, 'images/player_car.png', 60, 110)
    playerCar.rect.x = 300
    playerCar.rect.y = screenheight - 100

    player2Car = Car(70, 'images/player2_car.png', 60, 110)
    player2Car.rect.x = 900
    player2Car.rect.y = screenheight - 100

    playerCar_copy = Car(70, 'images/player_car.png', 60, 110)

    player2Car_copy = Car(70, 'images/player2_car.png', 60, 110)

    smallCar = Car(70, 'images/player_car.png', 30, 50)

    smallCar2 = Car(70, 'images/player2_car.png', 30, 50)

    car1 = Car(random.randint(30, 110), 'images/car1.png', 60, 110)
    car1.rect.x = 67
    car1.rect.y = -50

    car2 = Car(random.randint(30, 110), 'images/car2.png', 60, 110)
    car2.rect.x = 155
    car2.rect.y = -600

    car3 = Car(random.randint(30, 110), 'images/car3.png', 60, 110)
    car3.rect.x = 244
    car3.rect.y = -350

    car4 = Car(random.randint(30, 110), 'images/car4.png', 60, 110)
    car4.rect.x = 334
    car4.rect.y = -900

    car5 = Car(random.randint(30, 110), 'images/car5.png', 60, 110)
    car5.rect.x = 424
    car5.rect.y = -800

    car6 = Car(random.randint(30, 110), 'images/car6.png', 60, 110)
    car6.rect.x = 513
    car6.rect.y = -1000

    car5 = Car(random.randint(30, 110), 'images/car5.png', 60, 110)
    car5.rect.x = 424
    car5.rect.y = -800

    car6 = Car(random.randint(30, 110), 'images/car6.png', 60, 110)
    car6.rect.x = 513
    car6.rect.y = -1000

    car7 = Car(random.randint(30, 110), 'images/car1.png', 60, 110)
    car7.rect.x = 687
    car7.rect.y = -50

    car8 = Car(random.randint(30, 110), 'images/car2.png', 60, 110)
    car8.rect.x = 775
    car8.rect.y = -600

    car9 = Car(random.randint(30, 110), 'images/car3.png', 60, 110)
    car9.rect.x = 865
    car9.rect.y = -350

    car10 = Car(random.randint(30, 110), 'images/car4.png', 60, 110)
    car10.rect.x = 955
    car10.rect.y = -900

    car11 = Car(random.randint(30, 110), 'images/car5.png', 60, 110)
    car11.rect.x = 1045
    car11.rect.y = -800

    car12 = Car(random.randint(30, 110), 'images/car6.png', 60, 110)
    car12.rect.x = 1133
    car12.rect.y = -1000

    # Create all powerup objects
    invincibility = InvincibilityPower(30, 30, 75, blue)
    slowing = SlowingPower(30, 30, 75, green)
    shrinking = ShrinkingPower(30, 30, 75, red)
    kill = KillPower(30, 30, 75, pink)
    invincibility2 = InvincibilityPower(30, 30, 75, blue)
    slowing2 = SlowingPower(30, 30, 75, green)
    shrinking2 = ShrinkingPower(30, 30, 75, red)
    kill2 = KillPower(30, 30, 75, pink)

    # Spawn powerups (set their rectangular coordinates)
    invincibility.spawn2()
    slowing.spawn2()
    shrinking.spawn2()
    kill.spawn2()
    invincibility2.spawn3()
    slowing2.spawn3()
    shrinking2.spawn3()
    kill2.spawn3()

    # Add the cars and the powerups to the list of objects
    all_sprites_list.add(playerCar)
    all_sprites_list.add(player2Car)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(car5)
    all_sprites_list.add(car6)
    all_sprites_list.add(car7)
    all_sprites_list.add(car8)
    all_sprites_list.add(car9)
    all_sprites_list.add(car10)
    all_sprites_list.add(car11)
    all_sprites_list.add(car12)
    all_sprites_list.add(invincibility)
    all_sprites_list.add(slowing)
    all_sprites_list.add(shrinking)
    all_sprites_list.add(kill)
    all_sprites_list.add(invincibility2)
    all_sprites_list.add(slowing2)
    all_sprites_list.add(shrinking2)
    all_sprites_list.add(kill2)

    # Add the NPC cars to the list of all coming cars
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)
    all_coming_cars.add(car5)
    all_coming_cars.add(car6)
    all_coming_cars.add(car7)
    all_coming_cars.add(car8)
    all_coming_cars.add(car9)
    all_coming_cars.add(car10)
    all_coming_cars.add(car11)
    all_coming_cars.add(car12)

    # Add the powerups to the list of all spawned powerups
    all_spawned_powerups = pygame.sprite.Group()
    all_spawned_powerups.add(invincibility)
    all_spawned_powerups.add(slowing)
    all_spawned_powerups.add(shrinking)
    all_spawned_powerups.add(kill)
    all_spawned_powerups.add(invincibility2)
    all_spawned_powerups.add(slowing2)
    all_spawned_powerups.add(shrinking2)
    all_spawned_powerups.add(kill2)

    # Create list to check which players crashed
    dead_players = []

    # Allowing the user to close the window...
    carryOn = True

    # Initiate pygame time clock and fetch the start time
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Set initial collision times to 1000000 (a random high value to ensure that the collision effects aren't applied
    # early in the game). (There are two, one for each player)
    collision_time = 1000000
    collision_time2 = 1000000

    # Define invincible variable to reflect the invincibility status. (There are two, one for each player)
    invincible = False
    invincible2 = False

    # Define powerup_active variable to reflect whether a powerup is active or not. (There are two, one for each player)
    powerup_active = False
    powerup_active2 = False

    # Interface loop
    while carryOn:
        # Getting the input of the user
        for event in pygame.event.get():
            # Press on exit button
            if event.type == pygame.QUIT:
                carryOn = False
                
            elif event.type == pygame.KEYDOWN:
                # Press the 'x' key
                if event.key == pygame.K_x:
                    carryOn = False

                # Press the 'esc' key (to access pause menu)
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

        # Define current time and elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 100

        # Check if movement keys are being pressed
        keys = pygame.key.get_pressed()
        
        # Define actions of movement for player 2
        if keys[pygame.K_LEFT]:
            player2Car.moveLeft3(5)
        if keys[pygame.K_RIGHT]:
            player2Car.moveRight3(5)
        if keys[pygame.K_UP]:
            player2Car.moveForward(5)
        if keys[pygame.K_DOWN]:
            player2Car.moveBackward(5)

        # Define actions of movement for player 1
        if keys[pygame.K_a]:
            playerCar.moveLeft2(5)
        if keys[pygame.K_d]:
            playerCar.moveRight2(5)
        if keys[pygame.K_w]:
            playerCar.moveForward(5)
        if keys[pygame.K_s]:
            playerCar.moveBackward(5)

        # Game Logic
        for car in all_coming_cars:
            # Make car move downwards
            car.moveNPC(speed)

            # If car leaves the screen
            if car.rect.y > screenheight:
                # Update car speed, image and y position
                car.changeSpeed(random.randint(50, 120))
                car.repaint(random.choice(image_list), 60, 120)
                car.rect.y = random.randint(-500, -200)

            # Check if there is a car collision for player 1 (if invincibility is not active)
            if not invincible:
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    print("Car crash!")
                    # Play crash sound
                    crash_sound.play()
                    # Remove cars from left road
                    all_sprites_list.remove(playerCar)
                    all_sprites_list.remove(car1)
                    all_sprites_list.remove(car2)
                    all_sprites_list.remove(car3)
                    all_sprites_list.remove(car4)
                    all_sprites_list.remove(car5)
                    all_sprites_list.remove(car6)
                    all_coming_cars.remove(car1)
                    all_coming_cars.remove(car2)
                    all_coming_cars.remove(car3)
                    all_coming_cars.remove(car4)
                    all_coming_cars.remove(car5)
                    all_coming_cars.remove(car6)
                    # Add player 1 to dead players list
                    dead_players.append('Player 1')

            # Check if there is a car collision for player 2 (if invincibility is not active)  
            if not invincible2:
                car_collision_list2 = pygame.sprite.spritecollide(player2Car, all_coming_cars, False)
                for car in car_collision_list2:
                    print("Car crash!")
                    # Play crash sound
                    crash_sound.play()
                    # Remove cars from left road
                    all_sprites_list.remove(player2Car)
                    all_sprites_list.remove(car7)
                    all_sprites_list.remove(car8)
                    all_sprites_list.remove(car9)
                    all_sprites_list.remove(car10)
                    all_sprites_list.remove(car11)
                    all_sprites_list.remove(car12)
                    all_coming_cars.remove(car7)
                    all_coming_cars.remove(car8)
                    all_coming_cars.remove(car9)
                    all_coming_cars.remove(car10)
                    all_coming_cars.remove(car11)
                    all_coming_cars.remove(car12)
                    # Add player 2 to dead players list
                    dead_players.append('Player 2')

        for powerup in all_spawned_powerups:
            # Make powerup move downwards
            powerup.move(speed)
            # If powerup leaves the screen and is not active, spawn it again (for player 1)
            if powerup.rect.y > screenheight and not powerup_active and powerup in [invincibility, slowing, shrinking, kill]:
                powerup.spawn2()
            # If powerup leaves the screen and is not active, spawn it again (for player 2)
            elif powerup.rect.y > screenheight and not powerup_active2 and powerup in [invincibility2, slowing2, shrinking2, kill2]:
                powerup.spawn3()

            # Check if player 1 collides with a powerup
            powerup_collision_list = pygame.sprite.spritecollide(playerCar, all_spawned_powerups, False)
            for powerup in powerup_collision_list:
                # Check if there isn't any powerups active (for player 1)
                if not powerup_active:
                    # Create variable to check the last powerup collision
                    last_powerup = ''
                    # Respawn the powerup
                    powerup.spawn2()
                    # Fetch the time in which the collision happened
                    collision_time = pygame.time.get_ticks()
                    
                    if powerup == invincibility:
                        # If powerup collected was invincibility, then update the status variables and apply effects.
                        invincible = True
                        powerup_active = True
                        last_powerup = 'invincibility'
                        powerup.affect_player(playerCar)
                        
                    elif powerup == slowing:
                        # If powerup collected was slowing, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'slowing'
                        playerCar.repaint('images/slowed_car.png', 60, 110)
                        powerup.affect_traffic(car1)
                        powerup.affect_traffic(car2)
                        powerup.affect_traffic(car3)
                        powerup.affect_traffic(car4)
                        powerup.affect_traffic(car5)
                        powerup.affect_traffic(car6)
                        
                    elif powerup == shrinking:
                        # If powerup collected was shrinking, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'shrinking'
                        powerup.affect_player(playerCar)
                        # Substitute the playerCar with the smallCar, and then update the playerCar
                        smallCar.rect.x = playerCar.rect.x
                        smallCar.rect.y = playerCar.rect.y
                        all_sprites_list.remove(playerCar)
                        all_sprites_list.add(smallCar)
                        playerCar = smallCar
                        playerCar.update()
                        
                    elif powerup == kill:
                        # If powerup collected was kill, then update the status variables and apply effects.
                        powerup_active = True
                        last_powerup = 'kill'
                        playerCar.repaint('images/kill_car.png', 60, 110)
                        powerup.affect_traffic(car1)
                        powerup.affect_traffic(car2)
                        powerup.affect_traffic(car3)
                        powerup.affect_traffic(car4)
                        powerup.affect_traffic(car5)
                        powerup.affect_traffic(car6)

            # Check if player 2 collides with a powerup
            powerup_collision_list2 = pygame.sprite.spritecollide(player2Car, all_spawned_powerups, False)
            for powerup in powerup_collision_list2:
                # Check if there isn't any powerups active (for player 2)
                if not powerup_active2:
                    # Create variable to check the last powerup collision
                    last_powerup2 = ''
                    # Respawn the powerup
                    powerup.spawn3()
                    # Fetch the time in which the collision happened
                    collision_time2 = pygame.time.get_ticks()
                    
                    if powerup == invincibility2:
                        # If powerup collected was invincibility, then update the status variables and apply effects.
                        invincible2 = True
                        powerup_active2 = True
                        last_powerup2 = 'invincibility'
                        powerup.affect_player2(player2Car)
                        
                    elif powerup == slowing2:
                        # If powerup collected was slowing, then update the status variables and apply effects.
                        powerup_active2 = True
                        last_powerup2 = 'slowing'
                        player2Car.repaint('images/slowed_car2.png', 60, 110)
                        powerup.affect_traffic(car7)
                        powerup.affect_traffic(car8)
                        powerup.affect_traffic(car9)
                        powerup.affect_traffic(car10)
                        powerup.affect_traffic(car11)
                        powerup.affect_traffic(car12)
                        
                    elif powerup == shrinking2:
                        # If powerup collected was shrinking, then update the status variables and apply effects.
                        powerup_active2 = True
                        last_powerup2 = 'shrinking'
                        powerup.affect_player2(player2Car)
                        # Substitute the player2Car with the smallCar2, and then update the player2Car
                        smallCar2.rect.x = player2Car.rect.x
                        smallCar2.rect.y = player2Car.rect.y
                        all_sprites_list.remove(player2Car)
                        all_sprites_list.add(smallCar2)
                        player2Car = smallCar2
                        player2Car.update()
                        
                    elif powerup == kill2:
                        # If powerup collected was kill, then update the status variables and apply effects.
                        powerup_active2 = True
                        last_powerup2 = 'kill'
                        player2Car.repaint('images/kill_car2.png', 60, 110)
                        powerup.affect_traffic(car7)
                        powerup.affect_traffic(car8)
                        powerup.affect_traffic(car9)
                        powerup.affect_traffic(car10)
                        powerup.affect_traffic(car11)
                        powerup.affect_traffic(car12)

        # Define for how long the powerups will be active, then determine what will happen after they become inactive
        # (For player 1)
        if current_time - collision_time > 6000:
            # Set collision time to 1000000 again
            collision_time = 1000000
            
            if last_powerup == 'invincibility':
                # If the last active powerup was invincibility, then update status variables and revert the effects.
                invincible = False
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)

            elif last_powerup == 'slowing':
                # If the last active powerup was slowing, then update status variables and revert the effects.
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)
                car1.changeSpeed(random.randint(50, 100))
                car2.changeSpeed(random.randint(50, 100))
                car3.changeSpeed(random.randint(50, 100))
                car4.changeSpeed(random.randint(50, 100))
                car5.changeSpeed(random.randint(50, 100))
                car6.changeSpeed(random.randint(50, 100))

            elif last_powerup == 'shrinking':
                # If the last active powerup was shrinking, then update status variables and revert the effects.
                powerup_active = False
                # Substitute the playerCar with a copy of it, then update playerCar
                playerCar_copy.rect.x = playerCar.rect.x
                playerCar_copy.rect.y = playerCar.rect.y
                all_sprites_list.remove(playerCar)
                all_sprites_list.add(playerCar_copy)
                playerCar = playerCar_copy
                playerCar.update()

            elif last_powerup == 'kill':
                # If the last active powerup was kill, then update status variables and revert the effects.
                powerup_active = False
                playerCar.repaint('images/player_car.png', 60, 110)
                car1.rect.y = random.randint(-300, -100)
                car2.rect.y = random.randint(-300, -100)
                car3.rect.y = random.randint(-300, -100)
                car4.rect.y = random.randint(-300, -100)
                car5.rect.y = random.randint(-300, -100)
                car6.rect.y = random.randint(-300, -100)
                all_sprites_list.add(car1)
                all_sprites_list.add(car2)
                all_sprites_list.add(car3)
                all_sprites_list.add(car4)
                all_sprites_list.add(car5)
                all_sprites_list.add(car6)
                all_coming_cars.add(car1)
                all_coming_cars.add(car2)
                all_coming_cars.add(car3)
                all_coming_cars.add(car4)
                all_coming_cars.add(car5)
                all_coming_cars.add(car6)

            # Create a playerCar_copy variable here, in order for it to be reset after each change related to it.
            playerCar_copy = Car(70, 'images/player_car.png', 60, 110)

        # Define for how long the powerups will be active, then determine what will happen after they become inactive
        # (For player 2)
        if current_time - collision_time2 > 6000:
            collision_time2 = 1000000
            if last_powerup2 == 'invincibility':
                # If the last active powerup was invincibility, then update status variables and revert the effects.
                invincible2 = False
                powerup_active2 = False
                player2Car.repaint('images/player2_car.png', 60, 110)

            elif last_powerup2 == 'slowing':
                # If the last active powerup was slowing, then update status variables and revert the effects.
                powerup_active2 = False
                player2Car.repaint('images/player2_car.png', 60, 110)
                car7.changeSpeed(random.randint(50, 100))
                car8.changeSpeed(random.randint(50, 100))
                car9.changeSpeed(random.randint(50, 100))
                car10.changeSpeed(random.randint(50, 100))
                car11.changeSpeed(random.randint(50, 100))
                car12.changeSpeed(random.randint(50, 100))

            elif last_powerup2 == 'shrinking':
                # If the last active powerup was shrinking, then update status variables and revert the effects.
                powerup_active2 = False
                # Substitute the player2Car with a copy of it, then update player2Car
                player2Car_copy.rect.x = player2Car.rect.x
                player2Car_copy.rect.y = player2Car.rect.y
                all_sprites_list.remove(player2Car)
                all_sprites_list.add(player2Car_copy)
                player2Car = player2Car_copy
                player2Car.update()

            elif last_powerup2 == 'kill':
                # If the last active powerup was kill, then update status variables and revert the effects.
                powerup_active2 = False
                player2Car.repaint('images/player2_car.png', 60, 110)
                car7.rect.y = random.randint(-300, -100)
                car8.rect.y = random.randint(-300, -100)
                car9.rect.y = random.randint(-300, -100)
                car10.rect.y = random.randint(-300, -100)
                car11.rect.y = random.randint(-300, -100)
                car12.rect.y = random.randint(-300, -100)
                all_sprites_list.add(car7)
                all_sprites_list.add(car8)
                all_sprites_list.add(car9)
                all_sprites_list.add(car10)
                all_sprites_list.add(car11)
                all_sprites_list.add(car12)
                all_coming_cars.add(car7)
                all_coming_cars.add(car8)
                all_coming_cars.add(car9)
                all_coming_cars.add(car10)
                all_coming_cars.add(car11)
                all_coming_cars.add(car12)

            # Create a player2Car_copy variable here, in order for it to be reset after each change related to it.
            player2Car_copy = Car(70, 'images/player2_car.png', 60, 110)

        # Check if both players are dead, and if so, then display the game over screen
        if dead_players == ['Player 1', 'Player 2'] or dead_players == ['Player 2', 'Player 1']:
            game_over2()

        # Update the all sprites list
        all_sprites_list.update()

        # Drawing on Screen
        screen.blit(grass, (0, 0))

        # Draw The Road
        pygame.draw.rect(screen, grey, [50, 0, 550, screenheight])
        pygame.draw.rect(screen, grey, [670, 0, 550, screenheight])

        # Draw Line paintings on the road
        pygame.draw.line(screen, yellow, [140, 0], [140, screenheight], 5)
        pygame.draw.line(screen, yellow, [230, 0], [230, screenheight], 5)
        pygame.draw.line(screen, yellow, [320, 0], [320, screenheight], 5)
        pygame.draw.line(screen, yellow, [410, 0], [410, screenheight], 5)
        pygame.draw.line(screen, yellow, [500, 0], [500, screenheight], 5)
        pygame.draw.line(screen, yellow, [760, 0], [760, screenheight], 5)
        pygame.draw.line(screen, yellow, [850, 0], [850, screenheight], 5)
        pygame.draw.line(screen, yellow, [940, 0], [940, screenheight], 5)
        pygame.draw.line(screen, yellow, [1030, 0], [1030, screenheight], 5)
        pygame.draw.line(screen, yellow, [1120, 0], [1120, screenheight], 5)

        # Marker size and edge markers
        marker_width = 15
        left_edge_marker1 = (40, 0, marker_width, screenheight)
        right_edge_marker1 = (585, 0, marker_width, screenheight)
        left_edge_marker2 = (660, 0, marker_width, screenheight)
        right_edge_marker2 = (1205, 0, marker_width, screenheight)

        # Draw the edge markers
        pygame.draw.rect(screen, white, left_edge_marker1)
        pygame.draw.rect(screen, white, right_edge_marker1)
        pygame.draw.rect(screen, white, left_edge_marker2)
        pygame.draw.rect(screen, white, right_edge_marker2)

        # Now let's draw all the sprites in one go
        all_sprites_list.draw(screen)

        # Create and display score texts in game
        text = font1.render(f"Score:", True, blue)
        text2 = font1.render(f"{int(elapsed_time)}", True, blue)
        screen.blit(text, (15, 20))
        screen.blit(text2, (70, 80))

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(60)

    pygame.quit()


def unpause():
    """Unpauses game by setting the global pause variable to False

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    global pause
    pause = False


def paused():
    """Pause screen of the game.

    Defines and displays the pause menu, which allows the user to either resume the game, go back to the main menu
    or quit the game.

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
    green = (0, 255, 0)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)

    # Creating some text labels
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    font2 = pygame.font.Font('fonts/evil_empire.ttf', 120)
    resume_text = font1.render('Resume Game', True, white)
    menu_text = font1.render('Main Menu', True, white)
    quit_text = font1.render('Quit', True, white)
    title_text = font2.render('Paused', True, yellow)

    # Creating image variable
    menu_background = pygame.image.load('images/credits_img.jpg')

    # Interface loop
    while pause:
        # Getting the input of the user
        for ev in pygame.event.get():
            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Press the quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
                    pygame.quit()

            # Press the resume button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
                    unpause()

            # Press the main menu button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
                    interface()

        # Setting the background color as black
        screen.fill(black)

        # Set background image
        screen.blit(menu_background, (0, 0))

        # Create variable to fetch position of the mouse
        mouse = pygame.mouse.get_pos()

        # Print the buttons text and the box(color changing)

        # Resume text
        # When the mouse is on the box it changes color
        if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, green, [500, 220, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 220, 280, 50])
        screen.blit(resume_text, (514, 226))

        # Main menu text
        if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
            pygame.draw.rect(screen, green, [500, 320, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 320, 280, 50])
        screen.blit(menu_text, (540, 326))

        # Quit text
        if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
            pygame.draw.rect(screen, green, [500, 420, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 420, 280, 50])
        screen.blit(quit_text, (595, 426))

        # TITLE TEXT
        screen.blit(title_text, (480, 50))

        # Pygame built-in function that updates the screen at every iteration of the loop
        pygame.display.update()


def interface():
    """Creates the GUI of the game.

    The interface displays a menu page, which will take the user's input and direct them to their desired destination.
    It defines and displays a background image, as well as texts and rectangles (which represent buttons), and provides
    feedback to certain types of inputs from the user.

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

            # Press on credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 520 <= mouse[1] <= 570:
                    credits_()

            # Press on rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 420 <= mouse[1] <= 470:
                    rules()

            # Press on singleplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 220 <= mouse[1] <= 270:
                    singleplayer()

            # Press on multiplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 560 and 320 <= mouse[1] <= 370:
                    multiplayer()

        # Setting the background color as black
        screen.fill(black)

        # Set background image
        screen.blit(menu_background, (0, 0))

        # Create variable to fetch position of the mouse
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
        screen.blit(rules_text, (364, 426))

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
    It displays a background image, texts and a rectangle that works as a back button for the user to return to
    the main menu interface.

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

            # Press on quit button
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

        # Back text
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
    rule1_text = textfont.render('- Use arrow keys to move car (left/right/up/down) (or w/a/s/d for multiplayer)', True, white)
    rule2_text = textfont.render('- Avoid crashing with other cars in order to survive', True, white)
    rule3_text = textfont.render('- Collect powerups to enhance your gameplay experience:', True, white)
    rule4_text = powerupfont.render('BLUE - Gain temporary invincibility |   GREEN - Slows down cars |   RED - Shrinks your car |   PINK - Clears all cars around you', True, yellow)
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

        # Back text
        if 280 <= mouse[0] <= 560 and 620 <= mouse[1] <= 670:
            pygame.draw.rect(screen, red, [280, 620, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [280, 620, 280, 50])
        screen.blit(back_text, (374, 626))

        # Update display
        pygame.display.update()


def game_over():
    """Defines the game over screen for the singleplayer mode.

    Displays a game over screen, in which the player can opt to play again, go back to the main menu, or exit the
    game.

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
    green = (0, 255, 0)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)

    # Creating some text labels
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    font2 = pygame.font.Font('fonts/evil_empire.ttf', 120)
    playagain_text = font1.render('Play Again', True, white)
    menu_text = font1.render('Main Menu', True, white)
    quit_text = font1.render('Quit', True, white)
    title_text = font2.render('Game Over', True, yellow)

    # Creating image variable
    menu_background = pygame.image.load('images/credits_img.jpg')

    # Interface loop
    while True:
        # Getting the input of the user
        for ev in pygame.event.get():
            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
                    pygame.quit()

            # Press on play again button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
                    singleplayer()

            # Press on main menu button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
                    interface()

        # Setting the background color as black
        screen.fill(black)

        # Set background image
        screen.blit(menu_background, (0, 0))

        # Create variable to fetch position of the mouse
        mouse = pygame.mouse.get_pos()

        # Print the buttons text and the box(color changing)

        # Play again text
        # When the mouse is on the box it changes color
        if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, green, [500, 220, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 220, 280, 50])
        screen.blit(playagain_text, (525, 226))

        # Menu text
        if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
            pygame.draw.rect(screen, green, [500, 320, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 320, 280, 50])
        screen.blit(menu_text, (535, 326))

        # Quit text
        if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
            pygame.draw.rect(screen, green, [500, 420, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 420, 280, 50])
        screen.blit(quit_text, (595, 426))

        # TITLE TEXT
        screen.blit(title_text, (400, 50))

        # Pygame built-in function that updates the screen at every iteration of the loop
        pygame.display.update()


def game_over2():
    """Defines the game over screen for multiplayer mode.

    Displays a game over screen, in which the player can opt to play again, go back to the main menu, or exit the
    game.

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
    green = (0, 255, 0)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)

    # Creating some text labels
    font1 = pygame.font.Font('fonts/pixel_emulator.ttf', 30)
    font2 = pygame.font.Font('fonts/evil_empire.ttf', 120)
    playagain_text = font1.render('Play Again', True, white)
    menu_text = font1.render('Main Menu', True, white)
    quit_text = font1.render('Quit', True, white)
    title_text = font2.render('Game Over', True, yellow)

    # Creating image variable
    menu_background = pygame.image.load('images/credits_img.jpg')

    # Interface loop
    while True:
        # Getting the input of the user
        for ev in pygame.event.get():
            # Press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # Press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
                    pygame.quit()

            # Press on play again button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
                    multiplayer()

            # Press on main menu button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
                    interface()

        # Setting the background color as black
        screen.fill(black)

        # Set background image
        screen.blit(menu_background, (0, 0))

        # Create variable to fetch position of the mouse
        mouse = pygame.mouse.get_pos()

        # Print the buttons text and the box(color changing)

        # Play again text
        # When the mouse is on the box it changes color
        if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 270:
            pygame.draw.rect(screen, green, [500, 220, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 220, 280, 50])
        screen.blit(playagain_text, (525, 226))

        # Menu text
        if 500 <= mouse[0] <= 780 and 320 <= mouse[1] <= 370:
            pygame.draw.rect(screen, green, [500, 320, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 320, 280, 50])
        screen.blit(menu_text, (535, 326))

        # Quit text
        if 500 <= mouse[0] <= 780 and 420 <= mouse[1] <= 470:
            pygame.draw.rect(screen, green, [500, 420, 280, 50])
        else:
            pygame.draw.rect(screen, color_dark, [500, 420, 280, 50])
        screen.blit(quit_text, (595, 426))

        # TITLE TEXT
        screen.blit(title_text, (400, 50))

        # Pygame built-in function that updates the screen at every iteration of the loop
        pygame.display.update()
