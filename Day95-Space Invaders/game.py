import pygame
import random
from aliens import Alien, MysteryShip
from player import Spaceship, Bullet, Barrier


class Game:
    def __init__(self):
        # Initialize PyGame
        pygame.init()

        self.VEL = 5
        self.BULLET_VEL = 7
        self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT = 55, 40
        self.ALIEN_WIDTH, self.ALIEN_HEIGHT = 40, 25
        self.ALIEN_VEL = 1

        # Screen dimensions
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Title and Icon
        pygame.display.set_caption("Space Invaders")

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # Fonts
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

        # Load images
        self.heart_img = pygame.image.load("./assets/heart.png")
        self.heart_img = pygame.transform.scale(self.heart_img, (40, 40))
        self.explosion_img = pygame.image.load("./assets/explosion.png")
        self.explosion_img = pygame.transform.scale(
            self.explosion_img, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)
        )

        # Constants
        self.FPS = 60

        # Game objects
        self.spaceship = Spaceship(self.screen_width, self.screen_height)
        self.aliens = [
            Alien(50 + j * 60, 50 + i * 60) for i in range(5) for j in range(11)
        ]
        self.bullets = []
        self.alien_bullets = []
        self.barriers = [
            Barrier(150, self.screen_height - 200),
            Barrier(350, self.screen_height - 200),
            Barrier(550, self.screen_height - 200),
            Barrier(750, self.screen_height - 200),
            Barrier(950, self.screen_height - 200),
        ]
        self.mystery_ship = MysteryShip(self.screen_width)

        # Game states
        self.running = True
        self.game_active = False
        self.game_over = False
        self.score = 0
        self.wave = 1
        self.player_hit_time = None

        # Clock
        self.clock = pygame.time.Clock()
        self.speed_multiplier = 1

    def start_screen(self):
        self.screen.fill(self.black)
        title_text = self.font.render("Space Invaders", True, self.white)
        start_text = self.small_font.render("Press ENTER to Start", True, self.white)
        self.screen.blit(
            title_text,
            (
                self.screen_width // 2 - title_text.get_width() // 2,
                self.screen_height // 2 - title_text.get_height() // 2 - 50,
            ),
        )
        self.screen.blit(
            start_text,
            (
                self.screen_width // 2 - start_text.get_width() // 2,
                self.screen_height // 2 - start_text.get_height() // 2 + 50,
            ),
        )
        pygame.display.update()

    def game_over_screen(self):
        self.screen.fill(self.black)
        game_over_text = self.font.render("Game Over", True, self.white)
        play_again_text = self.small_font.render(
            "Press ENTER to Play Again", True, self.white
        )
        self.screen.blit(
            game_over_text,
            (
                self.screen_width // 2 - game_over_text.get_width() // 2,
                self.screen_height // 2 - game_over_text.get_height() // 2 - 50,
            ),
        )
        self.screen.blit(
            play_again_text,
            (
                self.screen_width // 2 - play_again_text.get_width() // 2,
                self.screen_height // 2 - play_again_text.get_height() // 2 + 50,
            ),
        )
        pygame.display.update()

    def check_collision(self, rect1, rect2):
        return rect1.colliderect(rect2)

    def draw_lives(self):
        for i in range(self.spaceship.lives):
            self.screen.blit(self.heart_img, (10 + i * 50, 10))

    def draw_score(self):
        score_text = self.small_font.render(f"Score: {self.score}", True, self.white)
        self.screen.blit(
            score_text, (self.screen_width - score_text.get_width() - 10, 10)
        )

    def draw_wave(self):
        wave_text = self.small_font.render(f"Wave: {self.wave}", True, self.white)
        self.screen.blit(
            wave_text, (self.screen_width // 2 - wave_text.get_width() // 2, 10)
        )

    def generate_aliens(self, speed_multiplier):
        return [
            Alien(50 + j * 60, 50 + i * 60, speed_multiplier)
            for i in range(5)
            for j in range(11)
        ]

    def reset_barriers(self):
        return [
            Barrier(150, self.screen_height - 200),
            Barrier(350, self.screen_height - 200),
            Barrier(550, self.screen_height - 200),
            Barrier(750, self.screen_height - 200),
            Barrier(950, self.screen_height - 200),
        ]

    def run(self):
        alien_direction = 1

        while self.running:
            self.clock.tick(self.FPS)
            if not self.game_active and not self.game_over:
                self.start_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.game_active = True
                            self.game_over = False
                            self.score = 0
                            self.wave = 1
                            self.spaceship.lives = 3
                            self.spaceship.reset_position()
                            self.aliens = self.generate_aliens(self.speed_multiplier)
                            self.barriers = self.reset_barriers()
            elif self.game_over:
                self.game_over_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.game_active = True
                            self.game_over = False
                            self.score = 0
                            self.wave = 1
                            self.spaceship.lives = 3
                            self.spaceship.reset_position()
                            self.aliens = self.generate_aliens(self.speed_multiplier)
                            self.barriers = self.reset_barriers()
            else:
                self.screen.fill(self.black)  # Fill the screen with black

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    # Keydown events
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.spaceship.x_change = -self.VEL
                        if event.key == pygame.K_RIGHT:
                            self.spaceship.x_change = self.VEL
                        if event.key == pygame.K_SPACE:
                            if len(self.bullets) < 3:
                                bullet = Bullet(self.spaceship.rect.centerx, self.spaceship.rect.top, -1)
                                self.bullets.append(bullet)

                    # Keyup events
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            self.spaceship.x_change = 0

                # Move and draw spaceship
                if self.player_hit_time is None:
                    self.spaceship.move()
                    self.spaceship.draw(self.screen)
                else:
                    # Display explosion and pause for 0.5 seconds
                    self.screen.blit(self.explosion_img, self.spaceship.rect.topleft)
                    if pygame.time.get_ticks() - self.player_hit_time > 500:
                        self.player_hit_time = None
                        self.spaceship.reset_position()

                # Move and draw aliens
                shift_down = False
                for alien in self.aliens:
                    alien.move()
                    if (
                        alien.rect.x <= 0
                        or alien.rect.x >= self.screen_width - self.ALIEN_WIDTH
                    ):
                        shift_down = True
                    alien.draw(self.screen)
                    if alien.rect.y > self.screen_height - 100:
                        self.game_over = True  # Game over

                if shift_down:
                    for alien in self.aliens:
                        alien.shift_down()

                # Move and draw bullets
                for bullet in self.bullets[:]:
                    bullet.move(self.screen)
                    if bullet.state == "ready":
                        self.bullets.remove(bullet)
                    else:
                        # Check collision with aliens
                        for alien in self.aliens[:]:
                            if self.check_collision(bullet.rect, alien.rect):
                                self.aliens.remove(alien)
                                self.bullets.remove(bullet)
                                self.score += 10
                                break
                        # Check collision with barriers
                        for barrier in self.barriers[:]:
                            if self.check_collision(bullet.rect, barrier.rect):
                                self.bullets.remove(bullet)
                                self.barriers.remove(barrier)
                                break
                        # Check collision with mystery ship
                        if self.mystery_ship.active and self.check_collision(
                            bullet.rect, self.mystery_ship.rect
                        ):
                            self.mystery_ship.active = False
                            self.bullets.remove(bullet)
                            self.score += 50

                # Move and draw alien bullets
                for bullet in self.alien_bullets[:]:
                    bullet.move(self.screen)
                    if bullet.state == "ready":
                        self.alien_bullets.remove(bullet)
                    else:
                        if self.check_collision(bullet.rect, self.spaceship.rect):
                            self.alien_bullets.remove(bullet)
                            if self.spaceship.hit():
                                self.game_over = True
                            else:
                                self.player_hit_time = pygame.time.get_ticks()

                        # Check collision with barriers
                        for barrier in self.barriers[:]:
                            if self.check_collision(bullet.rect, barrier.rect):
                                self.alien_bullets.remove(bullet)
                                self.barriers.remove(barrier)
                                break

                # Alien shooting
                if random.randint(0, 100) < 2:
                    shooting_alien = random.choice(self.aliens)
                    bullet = Bullet(
                        shooting_alien.rect.centerx, shooting_alien.rect.bottom, 1
                    )
                    self.alien_bullets.append(bullet)

                # Draw barriers
                for barrier in self.barriers:
                    barrier.draw(self.screen)

                # Move and draw mystery ship
                if random.randint(0, 1000) < 5 and not self.mystery_ship.active:
                    self.mystery_ship.activate()
                self.mystery_ship.move(self.screen)

                # Draw lives, score, and wave
                self.draw_lives()
                self.draw_score()
                self.draw_wave()

                # Check if all aliens are destroyed
                if not self.aliens:
                    self.speed_multiplier += 0.5
                    self.wave += 1
                    self.aliens = self.generate_aliens(self.speed_multiplier)
                    self.barriers = self.reset_barriers()

                pygame.display.update()

        pygame.quit()
