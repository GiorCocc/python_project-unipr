import g2d_pyg as g2d
from random import randint, choice
from boardgame_bubble_bobble import BubbleGame, Bubble

# variabili globali
CONT_STEP = 0                           # contatore per i passi che deve compiere il nemico prima di cambiare direzione
DECISION = randint(1,3)                 # scelte per i possibili movimenti del nemico
DIRECTION = 0                           # stabilisce la direzione della bolla in base alla direzione assunta dal drago
SPEED = 5
STEP_DIR_FRAME = 15                     # numero di frame prima che il nemico cambi la sua direzione (fatto per avere un movimento più semplice e lineare)

class BubbleGui:
    def __init__(self):
        self._game = BubbleGame()
        g2d.init_canvas(self._game.arena().size())
        self._sprites = g2d.load_image("bubble_bobble.png")
        # self._sprites = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")
        g2d.main_loop(self.tick)


    def tick(self):
        global CONT_STEP, DECISION, DIRECTION

        # controlli da tastiera separati per ogni giocatore e con gestione della direzione per la bolla. A destra ←→↑↓ ; a sinistra WASD
        if g2d.key_pressed("ArrowUp"):
            self._game.hero1().go_up()
        elif g2d.key_pressed("ArrowRight"):
            self._game.hero1().go_right()
            DIRECTION = 1
        elif g2d.key_pressed("ArrowLeft"):
            self._game.hero1().go_left()
            DIRECTION = 0
        elif (g2d.key_released("ArrowLeft") or g2d.key_released("ArrowRight")):
            self._game.hero1().stay()
        elif g2d.key_pressed("ArrowDown"):
            dragon_x, dragon_y, dragon_w, dragon_h = self._game.hero1().position()
            if DIRECTION == 0:
                dragon_dimension = dragon_x - dragon_w
                speed = -SPEED
            elif DIRECTION == 1:
                dragon_dimension = dragon_x + dragon_w
                speed = SPEED
            self._game.bubble().append(Bubble(self._game.arena(), (dragon_dimension, dragon_y), speed))

        if g2d.key_pressed('w'):
            self._game.hero().go_up()
        elif g2d.key_pressed("d"):
            self._game.hero().go_right()
            DIRECTION = 1
        elif g2d.key_pressed("a"):
            self._game.hero().go_left()
            DIRECTION = 0
        elif (g2d.key_released("a") or g2d.key_released("d")):
            self._game.hero().stay()
        elif g2d.key_pressed("s"):
            dragon_x, dragon_y, dragon_w, dragon_h = self._game.hero().position()
            if DIRECTION == 0:
                dragon_dimension = dragon_x - dragon_w
                speed = -SPEED
            elif DIRECTION == 1:
                dragon_dimension = dragon_x + dragon_w
                speed = SPEED
            self._game.bubble().append(Bubble(self._game.arena(), (dragon_dimension, dragon_y), speed))
        
        # decisione del movimento per il nemico aggiornando il numero di passi con il tick
        CONT_STEP += 1
        if CONT_STEP == STEP_DIR_FRAME:
            for enemy in self._game.enemy():
                DECISION = randint(1,3)
                enemy.decision(DECISION)
            CONT_STEP = 0
        else:
            for enemy in self._game.enemy():
                enemy.decision(DECISION)

        # controllo se il giocatore è vivo e nel caso lo rimuov0 e lo riaggiungo nel punto di origine
        if self._game.hero().lives() == 0:
            self._game.arena().remove(self._game.hero())
            g2d.alert("Sei stato eliminato!")
            self._game.hero().restore()

        if self._game.hero1().lives() == 0:
            self._game.arena().remove(self._game.hero1())
            g2d.alert("Sei stato eliminato!")
            self._game.hero1().restore()
            
        self._game.arena().move_all()  # Game logic
        
        # disegno degli elementi grafici
        g2d.clear_canvas()

        for i in self._game.platform():
            i.fill()

        for a in self._game.arena().actors():
            if a.symbol() != (0, 0, 0, 0):
                g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
            else:
                g2d.fill_rect(a.position())

        # gestione delle vite, dei punti e del tempo nell'interfaccia
        lives_player = "Player1 Lives: " + str(self._game.hero().lives())
        lives_player1 = "Player2 Lives: " + str(self._game.hero1().lives())
        points = "Points: " + str(self._game.hero().points() + self._game.hero1().points())
        toplay = "Time: " + str(self._game.remaining_time())

        g2d.draw_text(lives_player + "    " + toplay + "    " + points, (0, 0), 24)
        g2d.draw_text(lives_player1, (0,24), 24)

        # creazione degli alert per il termine del gioco
        if self._game.game_over():
            g2d.alert("Game over")
            g2d.close_canvas()

        elif self._game.game_won():
            g2d.alert("Game won")
            g2d.close_canvas()

gui = BubbleGui()