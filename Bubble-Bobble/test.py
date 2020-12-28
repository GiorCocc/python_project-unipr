import unittest
from bubble_bobble import Bubble, Dragon, Enemy, Platform, Arena

class DragonTest (unittest.TestCase):

    def dragon_move_left(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        dragon.go_left()
        dragon.move()
        self.assertTrue(dragon.position() == (47, 0, 20, 20))

    def dragon_move_right(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        dragon.go_right()
        dragon.move()
        self.assertTrue(dragon.position() == (53, 0, 20, 20))

    def dragon_move_up(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        dragon.go_up()
        dragon.move()
        self.assertTrue(dragon.position() == (50, 0, 20, 20))

    def dragon_collide_platform(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (0,0))
        platform = Platform(arena, (30,0), 2, 1)
        dragon.move()
        dragon.collide(platform)
        self.assertTrue(dragon.position() == (10, 0, 20, 20))

    def dragon_collide_bubble(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        bubble = Bubble(arena, (47,0), 0)
        dragon.go_left()
        dragon.move()
        dragon.collide(bubble)
        self.assertTrue(len(arena.actors()) == 1)

    def dragon_collide_enemy(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        enemy = Enemy((47,0), arena)
        dragon.go_left()
        dragon.move()
        dragon.collide(enemy)
        self.assertTrue(len(arena.actors()) == 1)

    def dragon_collide_enemy(self):
        arena = Arena ((100,100))
        dragon = Dragon(arena, (50,0))
        enemy = Enemy((47,0), arena)
        dragon.go_left()
        dragon.move()
        dragon.collide(enemy)
        self.assertTrue(dragon.lives() == 2)

class EnemyTest(unittest.TestCase):

    def enemy_moves_left(self):
        arena = Arena ((100,100))
        enemy = Enemy((50,50), arena)
        enemy.go_up()
        enemy.move()       
        self.assertTrue(enemy.position() == (47, 0, 20, 20))

    def enemy_moves_right(self):
        arena = Arena ((100,100))
        enemy = Enemy((50,50), arena)
        enemy.go_up()
        enemy.move()       
        self.assertTrue(enemy.position() == (53, 0, 20, 20))

    def enemy_move_up(self):
        arena = Arena ((100,100))
        enemy = Enemy((50,50), arena)
        enemy.go_up()
        enemy.move()       
        self.assertTrue(enemy.position() == (50, 0, 20, 20))

    def enemy_collide_bubble(self):
        arena = Arena ((100,100))
        bubble = Bubble(arena, (47,0), 0)
        enemy = Enemy((50,0), arena)
        enemy.go_left()
        enemy.move()
        enemy.collide(bubble)
        bubble.go_left()
        bubble.move()
        self.assertTrue(enemy.position() == bubble.position())

    def enemy_lives(self):
        arena = Arena ((100,100))
        bubble = Bubble(arena, (47,0), 0)
        enemy = Enemy((50,0), arena)
        lives0 = enemy.lives()
        enemy.go_left()
        enemy.move()
        enemy.collide(bubble)
        self.assertTrue(enemy.lives() == lives0())

if __name__ == "__main__":
    unittest.main()