#PONG VERSION 2
#2 PLAYERS
#CLASSIC PONG

from superwires import games, color
import random, math
games.init(screen_width=640, screen_height=480, fps=50)

#RAKIETA 1
class Rocket(games.Sprite):
    """Rakieta do odbijania piłki"""
    SPEED = 5
    image = games.load_image("rocket.png")
    def __init__(self):
        """Inicjalizuje rakietę"""
        super(Rocket, self).__init__(image = Rocket.image,
                                     x = 3,
                                     bottom = games.screen.height - 240)


    def update(self):
        """Kieruj za pomocą klawiszy W i S"""
        #sterowanie góra / dół
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1*self.SPEED
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1*self.SPEED
        #żeby nie wyjechał za daleko
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
        if self.top < 0:
            self.top = 0

        self.check_catch_1()

    def check_catch_1(self):
        """Sprawdź czy gracz odbił piłkę"""
        for ball in self.overlapping_sprites:
            ball.handle_caught_1()

#RAKIETA 2
class Rocket_2(games.Sprite):
    """Rakieta do odbijania piłki"""
    SPEED = 5
    image = games.load_image("rocket.png")
    def __init__(self):
        """Inicjalizuje rakietę"""
        super(Rocket_2, self).__init__(image = Rocket_2.image,
                                       x = games.screen.width,
                                        bottom = games.screen.height - 240)

    def update(self):
        """Kieruj za pomocą klawiszy UP i DOWN"""
        # sterowanie góra / dó
        if games.keyboard.is_pressed(games.K_UP):
            self.y -= 1*self.SPEED
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y += 1*self.SPEED
        # żeby nie wyjechał za daleko
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
        if self.top < 0:
            self.top = 0

        self.check_catch_2()

    def check_catch_2(self):

        """Sprawdź czy gracz odbił piłkę"""
        for ball in self.overlapping_sprites:
            ball.handle_caught_2()

class Ball(games.Sprite):
    """Piłka do gry"""
    image = games.load_image("pilka_pong.png")
    speed = 3
    change = False
    def __init__(self):
        """Inicjaluzuję piłkę"""
        super(Ball, self).__init__(image=Ball.image,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    dy=Ball.speed,
                                    dx=Ball.speed)

        #utwórz wynik punktowy 1
        self.score_1 = games.Text(value=0,
                                  size=30,
                                  color=color.white,
                                  top=5,
                                  right=games.screen.width - 10,
                                  is_collideable=False)
        games.screen.add(self.score_1)

        #utwórz wynik punktowy 2
        self.score_2 = games.Text(value=0,
                                  size=30,
                                  color=color.white,
                                  top=5,
                                  right=games.screen.width - 630,
                                  is_collideable=False)
        games.screen.add(self.score_2)




    def update(self):
        """Sprawdź czy dolny brzeg piłki dotknął dołu ekranu"""
        if self.bottom > games.screen.height:
            self.dy =  -1 *random.randrange(7,10)
            self.change = False #jeśli odbił się od dolnej ścianki to change ma wartość True
        elif self.right > games.screen.width:
            self.end_game_1()
            self.destroy()
            self.score_2.value += 1

        elif self.left < 0:
            self.end_game_2()
            self.destroy()
            self.score_1.value += 1

        elif self.top < 0:
            self.dy =  random.randrange(7,10)
            self.change = True #jeśli odbił się od górnej ścianki to change ma wartość True




    def handle_caught_1(self):

        """Odbicie piłki jeśli dotknął pierwszy gracz"""
        if self.change == True and self.y > 240:
            self.dy = -random.randrange(8, 10) * math.cos(self.angle)
        elif self.change == True and self.y < 240:
            self.dy = random.randrange(8,10) * math.cos(self.angle)
        elif self.change == False and self.y > 240:
            self.dy = -random.randrange(8, 10) * math.cos(self.angle)
        elif self.change == False and self.y < 240:
            self.dy = random.randrange(8, 10) * math.cos(self.angle)
        self.dx = random.randrange(8,10)



    def handle_caught_2(self):
        """Odbicie piłki jeśli dotknął pierwszy gracz"""
        if self.change == True and self.y > 240:
            self.dy = -random.randrange(8, 10) * math.cos(self.angle)
        elif self.change == True and self.y < 240:
            self.dy = random.randrange(8, 10) * math.cos(self.angle)
        elif self.change == False and self.y > 240:
            self.dy = -random.randrange(8, 10) * math.cos(self.angle)
        elif self.change == False and self.y < 240:
            self.dy = random.randrange(8, 10) * math.cos(self.angle)
        self.dx = -random.randrange(8,10)



    def end_game_1(self):
        """Koniec gry"""
        end_message = games.Message(value="Wygrywa Gracz 1",
                                size=45,
                                color=color.white,
                                x=games.screen.width / 2,
                                y=games.screen.height / 2,
                                lifetime=5 * games.screen.fps,
                                after_death=games.screen.quit)
        games.screen.add(end_message)

    def end_game_2(self):
        """Koniec gry"""
        end_message = games.Message(value="Wygrywa Gracz 2",
                                    size=45,
                                    color=color.white,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)




def main():
    the_ball = Ball()
    games.screen.add(the_ball)

    the_rocket = Rocket()
    games.screen.add(the_rocket)

    the_rocket_2 = Rocket_2()
    games.screen.add(the_rocket_2)



    games.screen.event_grab = True
    games.screen.mainloop()


# start programu
main()