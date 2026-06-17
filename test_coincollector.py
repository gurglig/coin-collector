import pytest
from random import randint
import pygame
import os

try:
    from pgzero.actor import Actor
except ImportError:
    pytest.skip("Pygame Zero (pgzrun) not installed or Actor not found, skipping all tests in this file.",
                allow_module_level=True)

WIDTH_TEST = 400
HEIGHT_TEST = 400


class GameTestContext:
    def __init__(self, width, height):
        self.score = 0
        self.high_score = 0
        self.lives = 1
        self.width = width
        self.height = height
        self.time_left = 30
        self.game_over = False
        self.game_started = False

        self.fox = Actor("fox")
        self.fox.pos = 100, 100

        self.coin = Actor("coin")
        self.coin.pos = 200, 200

        # Placeholder actors — in the real game these use their own images.
        # For tests we reuse "coin" so no extra image files are needed.
        self.obstacle = Actor("coin")
        self.obstacle.pos = 300, 150

        self.life_pickup = Actor("coin")
        self.life_pickup.pos = 50, 300

        self.powerup = Actor("coin")
        self.powerup.pos = 200, 350

    def update(self, dt):
        if not self.game_over:
            self.time_left -= dt
            if self.time_left <= 0:
                self.game_over = True
                self.time_left = 0
                # TODO: Update high_score if score is greater than the current high_score.
            self.update_score_logic()
            self.check_obstacle_collision()
            self.check_life_pickup_collision()
            self.check_powerup_collision()

    def place_coin(self):
        # TODO: Place coin at a random position, keeping it at least 20px from each edge.
        # Hint: use randint(20, self.width - 20) for x, and randint(20, self.height - 20) for y.
        pass

    def place_life_pickup(self):
        # TODO: Move life_pickup to a new random position with a 20px margin.
        pass

    def place_powerup(self):
        # TODO: Move powerup to a new random position with a 20px margin.
        pass

    def update_score_logic(self):
        # TODO: Check if fox and coin are colliding using fox.colliderect(coin).
        #       If they are, add 10 to score and call place_coin().
        pass

    def lose_life(self):
        # TODO: Subtract 1 from lives. If lives reach 0, set game_over to True.
        pass

    def check_obstacle_collision(self):
        # TODO: If fox collides with obstacle, call lose_life().
        pass

    def check_life_pickup_collision(self):
        # TODO: If fox collides with life_pickup, add 1 to lives and call place_life_pickup().
        pass

    def check_powerup_collision(self):
        # TODO: If fox collides with powerup, add 5 to time_left and call place_powerup().
        pass

    def clamp_fox(self):
        # TODO: Prevent the fox from moving off any edge of the screen.
        #       Keep fox.x between 0 and self.width.
        #       Keep fox.y between 0 and self.height.
        pass

    def restart(self):
        # TODO: Reset score, lives, time_left, game_over, and game_started to their starting values.
        pass


@pytest.fixture
def game_context():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

    try:
        pygame.init()
        pygame.display.set_mode((WIDTH_TEST, HEIGHT_TEST))
    except pygame.error as e:
        pytest.skip(f"Pygame initialization or display setup failed: {e}.")
        return

    try:
        context = GameTestContext(WIDTH_TEST, HEIGHT_TEST)
    except Exception as e:
        pygame.quit()
        pytest.skip(f"Could not initialize GameTestContext. "
                    f"Ensure 'images/fox.png' and 'images/coin.png' exist. Error: {e}")
        return

    yield context

    pygame.quit()


# ---------------------------------------------------------------------------
# Part 1 — Core game logic
# Implement place_coin(), update_score_logic(), and update() in GameTestContext.
# ---------------------------------------------------------------------------

def test_initial_score_is_zero(game_context):
    # TODO: Assert that game_context.score starts at 0.
    pass

def test_initial_time_is_thirty(game_context):
    # TODO: Assert that game_context.time_left starts at 30.
    pass

def test_place_coin_within_bounds(game_context):
    # TODO: Call place_coin() 100 times.
    #       Each time assert coin.x is between 20 and WIDTH_TEST - 20,
    #       and coin.y is between 20 and HEIGHT_TEST - 20.
    pass

def test_score_increases_on_collision(game_context):
    # TODO: Place fox and coin at the same position.
    #       Call update_score_logic().
    #       Assert score == 10 and the coin has moved to a new position.
    pass

def test_score_does_not_increase_if_no_collision(game_context):
    # TODO: Place fox at (50, 50) and coin at (300, 300).
    #       Call update_score_logic().
    #       Assert score is still 0.
    pass

def test_score_accumulates_over_multiple_collections(game_context):
    # TODO: Collect the coin 3 times in a row, moving fox to the coin's new position each time.
    #       Assert score goes 10 -> 20 -> 30.
    pass

def test_game_over_when_time_runs_out(game_context):
    # TODO: Call update(dt=31) to simulate 31 seconds passing.
    #       Assert game_over is True and time_left == 0.
    pass

def test_no_score_increase_after_game_over(game_context):
    # TODO: End the game by calling update(dt=31).
    #       Then move fox to coin's position and call update(dt=1) again.
    #       Assert score did not increase after the game ended.
    pass


# ---------------------------------------------------------------------------
# Part 2 — Boundary clamping (fixing clipping)
# Implement clamp_fox() in GameTestContext, then add the same logic to
# coincollector.py where the TODO comment is.
# ---------------------------------------------------------------------------

def test_fox_cannot_go_off_left_edge(game_context):
    # TODO: Set fox.x to -50, call clamp_fox(), assert fox.x >= 0.
    pass

def test_fox_cannot_go_off_right_edge(game_context):
    # TODO: Set fox.x to WIDTH_TEST + 50, call clamp_fox(), assert fox.x <= WIDTH_TEST.
    pass

def test_fox_cannot_go_off_top_edge(game_context):
    # TODO: Set fox.y to -50, call clamp_fox(), assert fox.y >= 0.
    pass

def test_fox_cannot_go_off_bottom_edge(game_context):
    # TODO: Set fox.y to HEIGHT_TEST + 50, call clamp_fox(), assert fox.y <= HEIGHT_TEST.
    pass


# ---------------------------------------------------------------------------
# Part 3 — Lives and dangerous obstacles
# Implement lose_life() and check_obstacle_collision() in GameTestContext,
# then add the same logic to coincollector.py where the TODO comment is.
# ---------------------------------------------------------------------------

def test_initial_lives_is_one(game_context):
    # TODO: Assert that game_context.lives starts at 1.
    pass

def test_lose_life_decrements_lives(game_context):
    # TODO: Set lives to 3, call lose_life(), assert lives == 2.
    pass

def test_game_over_when_lives_reach_zero(game_context):
    # TODO: Set lives to 1, call lose_life(), assert game_over is True.
    pass

def test_obstacle_collision_loses_a_life(game_context):
    # TODO: Set lives to 3.
    #       Place fox and obstacle at the same position.
    #       Call check_obstacle_collision().
    #       Assert lives == 2.
    pass

def test_obstacle_collision_ends_game_on_last_life(game_context):
    # TODO: Set lives to 1.
    #       Place fox and obstacle at the same position.
    #       Call check_obstacle_collision().
    #       Assert game_over is True.
    pass


# ---------------------------------------------------------------------------
# Part 4 — Life pickup
# Implement check_life_pickup_collision() and place_life_pickup() in
# GameTestContext, then add the same logic to coincollector.py.
# ---------------------------------------------------------------------------

def test_life_pickup_increases_lives(game_context):
    # TODO: Place fox and life_pickup at the same position.
    #       Call check_life_pickup_collision().
    #       Assert lives == 2.
    pass

def test_life_pickup_repositions_after_collection(game_context):
    # TODO: Record life_pickup position, trigger a collision, then
    #       assert the life_pickup has moved to a new position.
    pass

def test_place_life_pickup_within_bounds(game_context):
    # TODO: Call place_life_pickup() 100 times and assert that life_pickup.x
    #       and life_pickup.y stay within the 20px margin each time.
    pass


# ---------------------------------------------------------------------------
# Part 5 — Time extension powerup
# Implement check_powerup_collision() and place_powerup() in GameTestContext,
# then add the same logic to coincollector.py.
# ---------------------------------------------------------------------------

def test_powerup_extends_time(game_context):
    # TODO: Set time_left to 10.
    #       Place fox and powerup at the same position.
    #       Call check_powerup_collision().
    #       Assert time_left == 15.
    pass

def test_powerup_repositions_after_collection(game_context):
    # TODO: Record powerup position, trigger a collision, then
    #       assert the powerup has moved to a new position.
    pass

def test_place_powerup_within_bounds(game_context):
    # TODO: Call place_powerup() 100 times and assert that powerup.x
    #       and powerup.y stay within the 20px margin each time.
    pass


# ---------------------------------------------------------------------------
# Part 6 — Restart
# Implement restart() in GameTestContext, then add the same logic to
# coincollector.py where the TODO comment is (keyboard.r check in else block).
# ---------------------------------------------------------------------------

def test_restart_resets_score(game_context):
    # TODO: Set score to 50, call restart(), assert score == 0.
    pass

def test_restart_resets_time(game_context):
    # TODO: Set time_left to 0, call restart(), assert time_left == 30.
    pass

def test_restart_resets_lives(game_context):
    # TODO: Set lives to 0, call restart(), assert lives == 1.
    pass

def test_restart_clears_game_over(game_context):
    # TODO: Set game_over to True, call restart(), assert game_over is False.
    pass


# ---------------------------------------------------------------------------
# Part 7 — High score
# Update update() in GameTestContext to set high_score when the game ends,
# then add the same logic to coincollector.py where the TODO comment is.
# ---------------------------------------------------------------------------

def test_high_score_updates_after_game_over(game_context):
    # TODO: Set score to 50, call update(dt=31) to end the game.
    #       Assert that high_score == 50.
    pass

def test_high_score_not_overwritten_by_lower_score(game_context):
    # TODO: Set high_score to 100 and score to 30, then end the game.
    #       Assert that high_score is still 100.
    pass
