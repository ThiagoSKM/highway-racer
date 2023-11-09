import pygame

# Create a variable for color white
WHITE = (255, 255, 255)


# Define class Car, which represents a car. It derives from the "Sprite" class in Pygame.
class Car(pygame.sprite.Sprite):
    """A class representing a car in the game.

    A car is a rectangular object that has a specified dimension and is showed as an image in the game. It can move
    in four different directions and collide with other objects in the game.

    Attributes
    ----------
    image : pygame.image
        A pygame module to represent the image of the car.
    speed : int
        An integer that represents the speed in which the car (NPC car) moves towards the bottom of the screen.
    rect : pygame.rect
        A Pygame object for storing the rectangular coordinates of the car.

    Methods
    -------
    moveRight(self, pixels)
        Moves the player's car to the right, by a specified number of pixels. Used for singleplayer mode.
    moveRight2(self, pixels)
        Moves the player's car to the right, by a specified number of pixels. Used for multiplayer mode.
    moveRight3(self, pixels)
        Moves the player's car to the right, by a specified number of pixels. Used for multiplayer mode.
    moveLeft(self, pixels)
        Moves the player's car to the left, by a specified number of pixels. Used for singleplayer mode.
    moveLeft2(self, pixels)
        Moves the player's car to the left, by a specified number of pixels. Used for multiplayer mode.
    moveLeft3(self, pixels)
        Moves the player's car to the left, by a specified number of pixels. Used for multiplayer mode.
    moveForward(self, pixels)
        Moves the player's car upwards, by a specified number of pixels.
    moveBackward(self, pixels)
        Moves the player's car downwards, by a specified number of pixels.
    moveNPC(self, speed)
        Moves the car (NPC car) downwards, based on the speed specified.
    changeSpeed(self, speed)
        Updates the speed attribute of the car, based on the new speed.
    repaint(self, base_image, width, height)
        Updates the image attribute of the car, based on the new base_image, width and height.
    """

    def __init__(self, speed, base_image, image_width, image_height):
        """Initialize the Car class.

        Parameters
        ----------
        speed : int
            The speed in which the car (NPC car) moves towards the bottom of the screen.
        base_image: PNG image file
            The image that will be converted into a new Surface object by Pygame.
        image_width : int
            The width that the Surface (image) will be resized to.
        image_height : int
            The height that the Surface (image) will be resized to.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the image of the car
        image = pygame.image.load(base_image).convert_alpha()
        new_image = pygame.transform.scale(image, (image_width, image_height))
        self.image = new_image

        # Set speed of the car
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        """Moves the car to the right, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the right.

        Returns
        -------
        None
        """

        self.rect.x += pixels

        # Ensure that player can't go too far off the screen to the right
        if self.rect.x > 877:
            self.rect.x = 877

    def moveRight2(self, pixels):
        """Moves the car to the right, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the right.

        Returns
        -------
        None
        """

        self.rect.x += pixels

        # Ensure that player 1 (in multiplayer) can't go too far off the screen to the right
        if self.rect.x > 525:
            self.rect.x = 525

    def moveRight3(self, pixels):
        """Moves the car to the right, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the right.

        Returns
        -------
        None
        """

        self.rect.x += pixels

        # Ensure that player 2 (in multiplayer) can't go too far off the screen to the right
        if self.rect.x > 1145:
            self.rect.x = 1145

    def moveLeft(self, pixels):
        """Moves the car to the left, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the left.

        Returns
        -------
        None
        """

        self.rect.x -= pixels

        # Ensure that player can't go too far off the screen
        if self.rect.x < 340:
            self.rect.x = 340

    def moveLeft2(self, pixels):
        """Moves the car to the left, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the left.

        Returns
        -------
        None
        """

        self.rect.x -= pixels

        # Ensure that player 1 (in multiplayer) can't go too far off the screen to the left
        if self.rect.x < 55:
            self.rect.x = 55

    def moveLeft3(self, pixels):
        """Moves the car to the left, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move to the left.

        Returns
        -------
        None
        """

        self.rect.x -= pixels

        # Ensure that player 2 (in multiplayer) can't go too far off the screen to the left
        if self.rect.x < 675:
            self.rect.x = 675

    def moveForward(self, pixels):
        """Moves the car upwards, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move upwards.

        Returns
        -------
        None
        """

        self.rect.y -= pixels

        # Ensure that player can't go too far off the screen to the top
        if self.rect.y < 0:
            self.rect.y = 0

    def moveBackward(self, pixels):
        """Moves the car downwards, by a specified number of pixels.

        Parameters
        ----------
        pixels : int
            The number of pixels that the car will move downwards.

        Returns
        -------
        None
        """

        self.rect.y += pixels

        # Ensure that player can't go too far off the screen to the bottom
        if self.rect.y > 610:
            self.rect.y = 610

    def moveNPC(self, speed):
        """Moves the car downwards, according to the speed specified.

        Parameters
        ----------
        speed : int
            The speed rate in which that the car will move downwards.

        Returns
        -------
        None
        """

        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        """Updates the speed attribute of the car, based on the new speed value.

        Parameters
        ----------
        speed : int
            The speed rate in which that the car will move downwards.

        Returns
        -------
        None
        """

        self.speed = speed

    def repaint(self, base_image, width, height):
        """Updates the image attribute of the car, based on the new base_image, width and height.

        Parameters
        ----------
        base_image : PNG image file
            The image that will be converted into a new Surface object by Pygame.
        width : int
            The width that the Surface (image) will be resized to.
        height : int
            The height that the Surface (image) will be resized to.

        Returns
        -------
        None
        """

        # Update the image of the car
        image = pygame.image.load(base_image).convert_alpha()
        new_image = pygame.transform.scale(image, (width, height))
        self.image = new_image
