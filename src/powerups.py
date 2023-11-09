import pygame
from abc import ABC, abstractmethod
import random
from car import Car

# Create some color variables
black = (0, 0, 0)
white = (255, 255, 255)


# Define an abstract class PowerUp, which will be the mother class
class PowerUp(ABC):
    """An abstract class that represents a powerup.

    This abstract class represents the concept of a "Power-Up" inside the game. In simple words, a powerup is an object
    that a player can "catch" by hitting it with the car. The class contains three abstract methods with
    self-explanatory names: affect_player, affect_traffic and spawn. Each of the four child powerup classes will have a
    different look, as well as their own methods better specified and defined.

    Attributes
    ----------
    None

    Methods
    -------
    affect_player(self, player)
        Abstract method that represents the effects of the powerup on the player.
    affect_traffic(self, NPC)
        Abstract method that represents the effects of the powerup on the traffic.
    spawn(self)
        Abstract method that represents the rectangular coordinates of the powerup's spawn location.
    move(self, speed)
        Abstract method that represents the speed in which the car is moved downwards.
    """

    @abstractmethod
    def affect_player(self, player: Car):
        """Abstract method to apply the powerup effect on the player.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        pass

    @abstractmethod
    def affect_traffic(self, NPC: Car):
        """Abstract method to apply the powerup effect on the NPC.

        Parameters
        ----------
        NPC : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        pass

    @abstractmethod
    def spawn(self):
        """Abstract method to "spawn" the powerup by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        pass

    @abstractmethod
    def move(self, speed):
        """Abstract method to "move" the powerup by updating its Y coordinate.

        Parameters
        ----------
        speed : int
            The speed/rate in which the powerup moves towards the bottom of the screen.

        Returns
        -------
        None
        """

        pass


# Define a class for the invincibility powerup, which will be a child of the PowerUp class
class InvincibilityPower(PowerUp, pygame.sprite.Sprite):
    """The invincibility powerup class.

    This class inherits from the PowerUp mother class. It defines the attributes of the invincibility powerup, as well
    as the methods that define its appearance and functionalities.

    Attributes
    ----------
    width : int
        Represents the width that the powerup image (Pygame Surface) will have.
    height: int
        Represents the height that the powerup image (Pygame Surface) will have.
    speed : int
        Represents the speed/rate in which the powerup will move towards the bottom of the screen.
    image : pygame.image
        A pygame module to represent the image of the powerup.
    rect : pygame.rect
        A Pygame object for storing the rectangular coordinates of the powerup.

    Methods
    -------
    affect_player(self, player)
        Method that defines the effects of the powerup on the player 1, in both singleplayer and multiplayer mode.
    affect_player2(self, player)
        Method that defines the effects of the powerup on the player 2, in multiplayer mode.
    affect_traffic(self, NPC)
        Method that defines the effects of the powerup on the traffic.
    spawn(self)
        Method that defines the rectangular coordinates of the powerup's spawn location, in singleplayer mode.
    spawn2(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the left road, in
        multiplayer mode.
    spawn3(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the right road, in
        multiplayer mode.
    move(self, speed)
        Method that defines the speed in which the powerup is moved downwards.
    """

    def __init__(self, width, height, speed, color):
        """Initialize the powerup class.

        Parameters
        ----------
        width : int
            Represents the width that the powerup image (Pygame Surface) will have.
        height: int
            Represents the height that the powerup image (Pygame Surface) will have.
        speed : int
            Represents the speed/rate in which the powerup will move towards the bottom of the screen.
        color : RGB color
            Represents the color that the powerup image (Pygame Surface) will have.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the dimensions of the powerup
        self.width = width
        self.height = height

        # Set the speed of the powerup
        self.speed = speed

        # Set the image of the powerup
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the powerup on the image surface, considering its color and dimensions
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def spawn(self):
        """Method to "spawn" the powerup, in singleplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(350, 900)
        self.rect.y = random.randint(-10000, -6000)

    def spawn2(self):
        """Method to "spawn" the powerup, on the left road in multiplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(60, 560)
        self.rect.y = random.randint(-10000, -6000)

    def spawn3(self):
        """Method to "spawn" the powerup, on the right road in multiplayer mode, by updating its rectangular
         coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(680, 1190)
        self.rect.y = random.randint(-10000, -6000)

    def move(self, speed):
        """Method to "move" the powerup by updating its Y coordinate.

        Parameters
        ----------
        speed : int
            The speed/rate in which the powerup moves towards the bottom of the screen.

        Returns
        -------
        None
        """

        # Update powerup's Y coordinate
        self.rect.y += self.speed * speed / 20

    def affect_player(self, player: Car):
        """Method to apply the powerup effect on the player 1, both in singleplayer and multiplayer mode.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        #Change the appearance of the player's car, to indicate that the powerup is active
        player.repaint('images/invincible_car.png', 60, 110)

    def affect_player2(self, player: Car):
        """Method to apply the powerup effect on the player 2, in multiplayer mode.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        # Change the appearance of the player's car, to indicate that the powerup is active
        player.repaint('images/invincible_car2.png', 60, 110)

    def affect_traffic(self, NPC: Car):
        """Abstract method to apply the powerup effect on the NPC.

        Parameters
        ----------
        NPC : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        pass


# Define a class for the slowing powerup, which will be a child of the PowerUp class
class SlowingPower(PowerUp, pygame.sprite.Sprite):
    """The slowing powerup class.

    This class inherits from the PowerUp mother class. It defines the attributes of the slowing powerup, as well
    as the methods that define its appearance and functionalities.

    Attributes
    ----------
    width : int
        Represents the width that the powerup image (Pygame Surface) will have.
    height: int
        Represents the height that the powerup image (Pygame Surface) will have.
    speed : int
        Represents the speed/rate in which the powerup will move towards the bottom of the screen.
    image : pygame.image
        A pygame module to represent the image of the powerup.
    rect : pygame.rect
        A Pygame object for storing the rectangular coordinates of the powerup.

    Methods
    -------
    affect_player(self, player)
        Method that defines the effects of the powerup on the player.
    affect_traffic(self, NPC)
        Method that defines the effects of the powerup on the traffic.
    spawn(self)
        Method that defines the rectangular coordinates of the powerup's spawn location, in singleplayer mode.
    spawn2(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the left road, in
        multiplayer mode.
    spawn3(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the right road, in
        multiplayer mode.
    move(self, speed)
        Method that defines the speed in which the powerup is moved downwards.
    """

    def __init__(self, width, height, speed, color):
        """Initialize the powerup class.

        Parameters
        ----------
        width : int
            Represents the width that the powerup image (Pygame Surface) will have.
        height: int
            Represents the height that the powerup image (Pygame Surface) will have.
        speed : int
            Represents the speed/rate in which the powerup will move towards the bottom of the screen.
        color : RGB color
            Represents the color that the powerup image (Pygame Surface) will have.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the dimensions of the powerup
        self.width = width
        self.height = height

        # Set the speed of the powerup
        self.speed = speed

        # Set the image of the powerup
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the powerup on the image surface, considering its color and dimensions
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def spawn(self):
        """Method to "spawn" the powerup, in singleplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(350, 900)
        self.rect.y = random.randint(-5000, -1000)

    def spawn2(self):
        """Method to "spawn" the powerup, on the left road in multiplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(60, 560)
        self.rect.y = random.randint(-5000, -1000)

    def spawn3(self):
        """Method to "spawn" the powerup, on the right road in multiplayer mode, by updating its rectangular
         coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(680, 1190)
        self.rect.y = random.randint(-5000, -1000)

    def move(self, speed):
        """Method to "move" the powerup by updating its Y coordinate.

        Parameters
        ----------
        speed : int
            The speed/rate in which the powerup moves towards the bottom of the screen.

        Returns
        -------
        None
        """

        # Update powerup's Y coordinate
        self.rect.y += self.speed * speed / 20

    def affect_player(self, player: Car):
        """Method to apply the powerup effect on the player.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        pass

    def affect_traffic(self, NPC: Car):
        """Abstract method to apply the powerup effect on the NPC.

        Parameters
        ----------
        NPC : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        # Update NPC car's speed
        NPC.speed = 30


# Define a class for the shrinking powerup, which will be a child of the PowerUp class
class ShrinkingPower(PowerUp, pygame.sprite.Sprite):
    """The shrinking powerup class.

    This class inherits from the PowerUp mother class. It defines the attributes of the shrinking powerup, as well
    as the methods that define its appearance and functionalities.

    Attributes
    ----------
    width : int
        Represents the width that the powerup image (Pygame Surface) will have.
    height: int
        Represents the height that the powerup image (Pygame Surface) will have.
    speed : int
        Represents the speed/rate in which the powerup will move towards the bottom of the screen.
    image : pygame.image
        A pygame module to represent the image of the powerup.
    rect : pygame.rect
        A Pygame object for storing the rectangular coordinates of the powerup.

    Methods
    -------
    affect_player(self, player)
        Method that defines the effects of the powerup on the player 1, in both singleplayer and multiplayer mode.
    affect_player2(self, player)
        Method that defines the effects of the powerup on the player 2, in multiplayer mode.
    affect_traffic(self, NPC)
        Method that defines the effects of the powerup on the traffic.
    spawn(self)
        Method that defines the rectangular coordinates of the powerup's spawn location, in singleplayer mode.
    spawn2(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the left road, in
        multiplayer mode.
    spawn3(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the right road, in
        multiplayer mode.
    move(self, speed)
        Method that defines the speed in which the powerup is moved downwards.
    """

    def __init__(self, width, height, speed, color):
        """Initialize the powerup class.

        Parameters
        ----------
        width : int
            Represents the width that the powerup image (Pygame Surface) will have.
        height: int
            Represents the height that the powerup image (Pygame Surface) will have.
        speed : int
            Represents the speed/rate in which the powerup will move towards the bottom of the screen.
        color : RGB color
            Represents the color that the powerup image (Pygame Surface) will have.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the dimensions of the powerup
        self.width = width
        self.height = height

        # Set the speed of the powerup
        self.speed = speed

        # Set the image of the powerup
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the powerup on the image surface, considering its color and dimensions
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def spawn(self):
        """Method to "spawn" the powerup, in singleplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(350, 900)
        self.rect.y = random.randint(-8000, -3000)

    def spawn2(self):
        """Method to "spawn" the powerup, on the left road in multiplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(60, 560)
        self.rect.y = random.randint(-8000, -3000)

    def spawn3(self):
        """Method to "spawn" the powerup, on the right road in multiplayer mode, by updating its rectangular
         coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(680, 1190)
        self.rect.y = random.randint(-8000, -3000)

    def move(self, speed):
        """Method to "move" the powerup by updating its Y coordinate.

        Parameters
        ----------
        speed : int
            The speed/rate in which the powerup moves towards the bottom of the screen.

        Returns
        -------
        None
        """

        # Update powerup's Y coordinate
        self.rect.y += self.speed * speed / 20

    def affect_player(self, player: Car):
        """Method to apply the powerup effect on the player 1, both in singleplayer and multiplayer mode.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        #Change the appearance of the player's car, to indicate that the powerup is active
        player.repaint('images/player_car.png', 30, 50)

    def affect_player2(self, player: Car):
        """Method to apply the powerup effect on the player 2, in multiplayer mode.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        # Change the appearance of the player's car, to indicate that the powerup is active
        player.repaint('images/player2_car.png', 30, 50)

    def affect_traffic(self, NPC: Car):
        """Abstract method to apply the powerup effect on the NPC.

        Parameters
        ----------
        NPC : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        pass


# Define a class for the kill powerup, which will be a child of the PowerUp class
class KillPower(PowerUp, pygame.sprite.Sprite):
    """The kill powerup class.

    This class inherits from the PowerUp mother class. It defines the attributes of the kill powerup, as well
    as the methods that define its appearance and functionalities.

    Attributes
    ----------
    width : int
        Represents the width that the powerup image (Pygame Surface) will have.
    height: int
        Represents the height that the powerup image (Pygame Surface) will have.
    speed : int
        Represents the speed/rate in which the powerup will move towards the bottom of the screen.
    image : pygame.image
        A pygame module to represent the image of the powerup.
    rect : pygame.rect
        A Pygame object for storing the rectangular coordinates of the powerup.

    Methods
    -------
    affect_player(self, player)
        Method that defines the effects of the powerup on the player.
    affect_traffic(self, NPC)
        Method that defines the effects of the powerup on the traffic.
    spawn(self)
        Method that defines the rectangular coordinates of the powerup's spawn location, in singleplayer mode.
    spawn2(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the left road, in
        multiplayer mode.
    spawn3(self)
        Method that defines the rectangular coordinates of the powerup's spawn location for the right road, in
        multiplayer mode.
    move(self, speed)
        Method that defines the speed in which the powerup is moved downwards.
    """

    def __init__(self, width, height, speed, color):
        """Initialize the powerup class.

        Parameters
        ----------
        width : int
            Represents the width that the powerup image (Pygame Surface) will have.
        height: int
            Represents the height that the powerup image (Pygame Surface) will have.
        speed : int
            Represents the speed/rate in which the powerup will move towards the bottom of the screen.
        color : RGB color
            Represents the color that the powerup image (Pygame Surface) will have.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the dimensions of the powerup
        self.width = width
        self.height = height

        # Set the speed of the powerup
        self.speed = speed

        # Set the image of the powerup
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the powerup on the image surface, considering its color and dimensions
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def spawn(self):
        """Method to "spawn" the powerup, in singleplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(350, 900)
        self.rect.y = random.randint(-10000, -4000)

    def spawn2(self):
        """Method to "spawn" the powerup, on the left road in multiplayer mode, by updating its rectangular coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(60, 560)
        self.rect.y = random.randint(-10000, -4000)

    def spawn3(self):
        """Method to "spawn" the powerup, on the right road in multiplayer mode, by updating its rectangular
         coordinates.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # Update powerup's rectangular coordinates
        self.rect.x = random.randint(680, 1190)
        self.rect.y = random.randint(-10000, -4000)

    def move(self, speed):
        """Method to "move" the powerup by updating its Y coordinate.

        Parameters
        ----------
        speed : int
            The speed/rate in which the powerup moves towards the bottom of the screen.

        Returns
        -------
        None
        """

        # Update powerup's Y coordinate
        self.rect.y += self.speed * speed / 20

    def affect_player(self, player: Car):
        """Method to apply the powerup effect on the player.

        Parameters
        ----------
        player : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """
        pass

    def affect_traffic(self, NPC: Car):
        """Abstract method to apply the powerup effect on the NPC.

        Parameters
        ----------
        NPC : Car
            Car object (an instance of the Car class) which will be affected by the powerup.

        Returns
        -------
        None
        """

        # Kill the NPC
        NPC.kill()
