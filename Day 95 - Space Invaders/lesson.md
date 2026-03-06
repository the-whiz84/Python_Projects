# Day 95 - 2D Arcade Architecture with Pygame

Space Invaders is larger than the earlier arcade projects because it has multiple enemy types, player lives, bullets from both sides, destructible barriers, a mystery ship, start and game-over screens, and wave progression. That makes it a good lesson in organizing a 2D game into cooperating classes rather than one monolithic loop.

The project works because the game state lives in `Game`, while the moving actors live in their own modules.

## 1. Split the Game Into Focused Actor Classes

The project uses separate classes for the major pieces:

- `Spaceship`, `Bullet`, and `Barrier` in `player.py`
- `Alien` and `MysteryShip` in `aliens.py`
- `Game` in `game.py`

For example, the spaceship owns movement and life state:

```python
class Spaceship:
    def __init__(self, screen_width, screen_height):
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 100))
        self.x_change = 0
        self.lives = 3
        self.hit_status = False
```

That split is what keeps the game maintainable. The `Game` class can orchestrate actors without needing to store every behavior inline.

## 2. Let `Game` Own the Main State Machine

The `Game` constructor initializes:

- screen dimensions
- fonts and images
- lists of enemies, bullets, and barriers
- score, wave, and active/game-over flags

```python
self.running = True
self.game_active = False
self.game_over = False
self.score = 0
self.wave = 1
self.player_hit_time = None
```

That is the real architecture of the project. Every frame is interpreted through one of those states:

- start screen
- active game
- game over screen

The `run()` loop switches behavior depending on that state instead of trying to handle every case at once.

## 3. Use Collision Logic to Drive the Game

Once the game is active, the loop handles input, movement, drawing, and collisions.

The player fires bullets like this:

```python
if event.key == pygame.K_SPACE:
    if len(self.bullets) < 3:
        bullet = Bullet(self.spaceship.rect.centerx, self.spaceship.rect.top, -1)
        self.bullets.append(bullet)
```

That bullet cap is a small design choice, but it matters. It prevents the game from turning into a spam loop and keeps the pace closer to classic Space Invaders.

The bullets then interact with enemies, barriers, and the mystery ship through rectangle collisions:

```python
if self.check_collision(bullet.rect, alien.rect):
    self.aliens.remove(alien)
    self.bullets.remove(bullet)
    self.score += 10
```

That is the main arcade loop pattern again:

- move entities
- detect intersections
- update score or state
- remove objects that should no longer exist

## 4. Make Progression Part of the Architecture

The game does more than survive one screen. It also tracks:

- remaining lives
- wave number
- barrier resets
- alien regeneration

The helper methods such as `generate_aliens()` and `reset_barriers()` make those resets clean:

```python
def generate_aliens(self, speed_multiplier):
    return [
        Alien(50 + j * 60, 50 + i * 60, speed_multiplier)
        for i in range(5)
        for j in range(11)
    ]
```

The mystery ship adds another layer of variety without complicating the base alien logic:

```python
class MysteryShip:
    def activate(self):
        self.rect.x = 0
        self.active = True
```

This is what makes the project feel like a real game and not only a shooting demo. There are multiple interacting systems, but they remain understandable because each one has a clear owner.

## How to Run Space Invaders

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the game:
   ```bash
   python main.py
   ```
3. Verify the major behaviors:
   - `Enter` starts and restarts the game
   - left/right keys move the ship
   - `Space` fires bullets with a cap of three active shots
   - aliens, barriers, and the mystery ship all participate in collisions
   - score, lives, and wave indicators update during play

## Summary

Today, you worked with a fuller arcade architecture. The project separates actors into modules, uses `Game` as the orchestration layer, and drives progression through collisions, lives, and wave resets. The important lesson is not only how to use Pygame. It is how to keep a larger game readable by giving each moving piece a clear role.
