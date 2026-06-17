# Original project from the DK book, "Coding Games in Python."

import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

score = 0
high_score = 0
lives = 1
game_over = False
game_started = False
time_left = 30

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

# TODO: Add obstacle.png to the images/ folder, then uncomment these two lines:
# obstacle = Actor("obstacle")
# obstacle.pos = 300, 150

# TODO: Add life_pickup.png to the images/ folder, then uncomment these two lines:
# life_pickup = Actor("life_pickup")
# life_pickup.pos = 50, 300

# TODO: Add powerup.png to the images/ folder, then uncomment these two lines:
# powerup = Actor("powerup")
# powerup.pos = 200, 350

def draw():
    screen.fill("chartreuse4")
    fox.draw()
    coin.draw()
    # TODO: Once the actors above are uncommented, draw them here:
    # obstacle.draw()
    # life_pickup.draw()
    # powerup.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    screen.draw.text("Best: " + str(high_score), color="black", topleft=(10, 30))
    screen.draw.text("Lives: " + str(lives), color="black", topleft=(10, 50))
    screen.draw.text("Time: " + str(int(time_left)), color="black", topright=(WIDTH - 10, 10))

    if game_over:
        screen.fill("orange")
        screen.draw.text("Final Score: " + str(score), center=(WIDTH/2, HEIGHT/2 - 40), fontsize=60, color="black")
        screen.draw.text("Best: " + str(high_score), center=(WIDTH/2, HEIGHT/2 + 20), fontsize=40, color="black")
        screen.draw.text("Press R to restart", center=(WIDTH/2, HEIGHT/2 + 70), fontsize=30, color="black")

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update(dt):
    global score, game_over, time_left, game_started, high_score, lives

    if not game_over:
        if keyboard.w or keyboard.a or keyboard.s or keyboard.d or keyboard.up or keyboard.down or keyboard.left or keyboard.right:
            game_started = True

        if keyboard.a or keyboard.left:
            fox.x = fox.x - 5
        elif keyboard.d or keyboard.right:
            fox.x = fox.x + 5
        elif keyboard.w or keyboard.up:
            fox.y = fox.y - 5
        elif keyboard.s or keyboard.down:
            fox.y = fox.y + 5

        # TODO: Clamp fox so it cannot move off the edges of the screen.
        # Hint: check fox.x against 0 and WIDTH, and fox.y against 0 and HEIGHT.

        coin_collected = fox.colliderect(coin)
        if coin_collected:
            score = score + 10
            place_coin()

        # TODO: Check if fox collides with obstacle. If so, subtract 1 from lives.
        #       If lives reach 0, set game_over to True.
        #       (Uncomment obstacle above and add obstacle.png first.)

        # TODO: Check if fox collides with life_pickup. If so, add 1 to lives
        #       and move the life_pickup to a new random position.
        #       (Uncomment life_pickup above and add life_pickup.png first.)

        # TODO: Check if fox collides with powerup. If so, add 5 seconds to time_left
        #       and move the powerup to a new random position.
        #       (Uncomment powerup above and add powerup.png first.)

        if game_started:
            time_left = time_left - dt
            if time_left <= 0:
                game_over = True
                time_left = 0
                # TODO: Update high_score here if score is greater than the current high_score.

    else:
        # TODO: If keyboard.r is pressed, reset score, lives, time_left, game_over,
        #       and game_started to their starting values so the game can be played again.
        pass

place_coin()

pgzrun.go()
