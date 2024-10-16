import pygame

# Load images
alien_img = pygame.image.load("./assets/alien.png")
mystery_ship_img = pygame.image.load("./assets/mystery_ship.gif")
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 25
ALIEN_VEL = 1
# Screen dimensions
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


# Alien class
class Alien:
    def __init__(self, x, y, speed_multiplier=1):
        self.image = pygame.transform.scale(alien_img, (ALIEN_WIDTH, ALIEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x_change = ALIEN_VEL * speed_multiplier

    def move(self):
        self.rect.x += self.x_change

    def shift_down(self):
        self.rect.y += 10
        self.x_change *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


# Mystery Ship class
class MysteryShip:
    def __init__(self, screen_width):
        self.image = pygame.transform.scale(mystery_ship_img, (60, 30))
        self.rect = self.image.get_rect(topleft=(0, 50))
        self.x_change = 2
        self.active = False
        self.screen_width = screen_width

    def move(self, screen):
        if self.active:
            self.rect.x += self.x_change
            screen.blit(self.image, self.rect.topleft)
            if self.rect.x > self.screen_width:
                self.active = False

    def activate(self):
        self.rect.x = 0
        self.active = True
