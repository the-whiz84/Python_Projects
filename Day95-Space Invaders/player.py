import pygame

VEL = 5
BULLET_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BARRIER_WIDTH, BARRIER_HEIGHT = 80, 40  # Double the size of barriers

# Load images
spaceship_img = pygame.image.load("./assets/spaceship.png")
bullet_img = pygame.image.load("./assets/bullet.png")
barrier_img = pygame.image.load("./assets/barrier.png")
explosion_img = pygame.image.load("./assets/explosion.png")

# Screen dimensions
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


# Spaceship class
class Spaceship:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.transform.scale(
            spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        )
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 100))
        self.explosion_image = pygame.transform.scale(
            explosion_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        )  # Add this for the explosion image
        self.x_change = 0
        self.lives = 3
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hit_time = None  # Add a variable to track hit time
        self.hit_status = False  # Track if player is hit

    def move(self):
        if not self.hit_status:  # Prevent movement during explosion
            self.rect.x += self.x_change
            if self.rect.x <= 0:
                self.rect.x = 0
            elif self.rect.x >= self.screen_width - SPACESHIP_WIDTH:
                self.rect.x = self.screen_width - SPACESHIP_WIDTH

    def draw(self, screen):
        if self.hit_status:
            screen.blit(self.explosion_image, self.rect.topleft)  # Show explosion
        else:
            screen.blit(self.image, self.rect.topleft)

    def hit(self):
        self.lives -= 1
        self.hit_status = True
        self.hit_time = pygame.time.get_ticks()  # Record the time of the hit
        if self.lives <= 0:
            return True  # Game over when lives are zero
        return False

    def reset_position(self):
        self.rect.center = (self.screen_width // 2, self.screen_height - 100)
        self.hit_status = False  # Reset hit status after respawn


# Bullet class
class Bullet:
    def __init__(self, x, y, direction):
        self.image = pygame.transform.scale(bullet_img, (8, 16))
        self.rect = self.image.get_rect(center=(x, y))
        self.y_change = BULLET_VEL * direction
        self.state = "fire"
        self.screen_height = screen_height

    def move(self, screen):
        self.rect.y += self.y_change
        screen.blit(self.image, self.rect.topleft)
        if self.rect.y <= 0 or self.rect.y >= self.screen_height:
            self.state = "ready"


# Barrier class
class Barrier:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            barrier_img, (BARRIER_WIDTH, BARRIER_HEIGHT)
        )
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
