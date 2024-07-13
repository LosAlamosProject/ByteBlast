import pygame
import webbrowser
import typing


pygame.init()
window = pygame.display.set_mode((800, 600), pygame.RESIZABLE, pygame.SRCALPHA)
pygame.display.set_caption("ByteBlast")
pygame.display.set_icon(pygame.image.load("glmrenderer\\ByteBlast\\Main Menu\\assets\\icon.png").convert_alpha())
xbold = pygame.font.Font("glmrenderer\\ByteBlast\\Main Menu\\fonts\\Orbitron-ExtraBold.ttf", 90)
med = pygame.font.Font("glmrenderer\\ByteBlast\\Main Menu\\fonts\\Orbitron-Medium.ttf", 17)
med1 = pygame.font.Font("glmrenderer\\ByteBlast\\Main Menu\\fonts\\Orbitron-Medium.ttf", 30)
bg = pygame.image.load("glmrenderer\\ByteBlast\\Main Menu\\assets\\bg.png")
global credits
credits = False
global mapPicker
mapPicker = False
mapa = 0


class Button:
    def __init__(
        self,
        text: str,
        font: pygame.font.Font,
        pos: tuple[int, int],
        action: typing.Callable,
    ) -> None:
        self.text = text
        self.font = font
        self.action = action
        self.pos = pos
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.rendered_text.get_rect(topleft=self.pos)

    def draw(self, window: pygame.display):
        window.blit(self.rendered_text, self.rect)
        pygame.draw.rect(window, (255, 255, 255), self.rect.inflate(20, 10), 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.inflate(20, 10).collidepoint(event.pos):
                self.action()


def map1():
    global mapa
    mapa = 1


def map2():
    global mapa
    mapa = 2


def otvorikofi():
    webbrowser.open("https://ko-fi.com/markonije")


def openSP():
    global mapPicker
    mapPicker = True


def openCredits():
    print("Credits")
    global credits
    credits = True


def backToMenu():
    global credits
    credits = False
    global mapPicker
    mapPicker = False
    global mapa
    mapa = 0


back = Button(
    "Back",
    med1,
    (window.get_width() // 2 - med1.size("Back")[0] // 2, 500),
    backToMenu,
)
support = Button(
    "Support us at: ko-fi.com/markonije",
    med,
    (
        window.get_width() // 2
        - (med.size("Support us at: ko-fi.com/markonije")[0] // 2),
        350,
    ),
    otvorikofi,
)

map1 = Button(
    text="Map 1",
    font=med1,
    pos=(window.get_width() // 2 - med1.size("Map 1")[0] // 2, 250),
    action=map1,
)
map2 = Button(
    text="Map 2",
    font=med1,
    pos=(window.get_width() // 2 - med1.size("Map 2")[0] // 2, 325),
    action=map2,
)


def drawCredits(window):
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))
    titlec = xbold.render("Credits", True, (255, 255, 255))
    project = med.render("Project manager: Marko Popović", True, (255, 255, 255))
    devs = med.render(
        "Developers: Marko Popović, Mladen Gavrilović", True, (255, 255, 255)
    )
    graphics = med.render(
        "Graphics: Marko Jovanović, Mladen Gavrilović", True, (255, 255, 255)
    )

    window.blit(titlec, (window.get_width() // 2 - xbold.size("Credits")[0] // 2, 50))
    window.blit(
        project,
        (
            window.get_width() // 2
            - med.size("Project manager: Marko Popović")[0] // 2,
            200,
        ),
    )
    window.blit(
        devs,
        (
            window.get_width() // 2
            - med.size("Developers: Marko Popović, Mladen Gavrilović")[0] // 2,
            250,
        ),
    )
    window.blit(
        graphics,
        (
            window.get_width() // 2
            - med.size("Graphics: Marko Jovanović, Mladen Gavrilović")[0] // 2,
            300,
        ),
    )
    support.draw(window)
    back.draw(window)


def drawMapPicker(window):
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))
    titlec = xbold.render("Map Picker", True, (255, 255, 255))
    map1.draw(window)
    map2.draw(window)
    window.blit(
        titlec, (window.get_width() // 2 - xbold.size("Map Picker")[0] // 2, 50)
    )
    back.draw(window)


while True:
    w, h = window.get_size()
    bg = pygame.transform.scale(bg, (w, h))
    window.blit(bg, (0, 0))
    title = xbold.render("ByteBlast", True, (255, 255, 255))
    authors = med.render(
        "A game by Marko Popović and Mladen Gavrilović", True, (255, 255, 255)
    )
    singleplayer = Button(
        "Singleplayer",
        med1,
        (window.get_width() // 2 - med1.size("Singleplayer")[0] // 2, 250),
        openSP,
    )
    credits_button = Button(
        "Credits",
        med1,
        (window.get_width() // 2 - med1.size("Credits")[0] // 2, 325),
        openCredits,
    )
    singleplayer.draw(window)
    credits_button.draw(window)
    window.blit(title, (window.get_width() // 2 - xbold.size("ByteBlast")[0] // 2, 50))
    window.blit(
        authors,
        (
            window.get_width() // 2
            - med.size("A game by Marko Popović and Mladen Gavrilović")[0] // 2,
            175,
        ),
    )
    if credits:
        drawCredits(window)
    if mapPicker:
        drawMapPicker(window)
    if mapa != 0:
        print(mapa)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if credits:
            support.handle_event(event)
            back.handle_event(event)
        elif mapPicker:
            map1.handle_event(event)
            map2.handle_event(event)
            back.handle_event(event)
        else:
            singleplayer.handle_event(event)
            credits_button.handle_event(event)
