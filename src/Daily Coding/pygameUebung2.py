import pygame
import sys

pygame.init()

# Farben
weiß = (255, 255, 255)
schwarz = (0, 0, 0)

# Bildschirm initialisieren
breite, höhe = 400, 200
bildschirm = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Pygame Textfeld Beispiel")

# Schriftart initialisieren
pygame.font.init()
schrift = pygame.font.SysFont('Arial', 24)


class TextInput:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.aktiv = False
        self.blink_interval = 500  # Millisekunden
        self.last_blink_time = pygame.time.get_ticks()
        self.show_cursor = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.aktiv = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.aktiv:
            if event.key == pygame.K_RETURN:
                print("Eingegebener Text:", self.text)
                ausgabe_textfeld.text = self.text
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_blink_time >= self.blink_interval:
            self.show_cursor = not self.show_cursor
            self.last_blink_time = current_time

    def draw(self, surface):
        # Umrandung des Textfelds entsprechend der Aktivierung zeichnen
        pygame.draw.rect(surface, schwarz, self.rect, 2)

        # Text mit oder ohne Cursor zeichnen
        eingabe_text = self.text + ("|" if self.show_cursor else "")
        eingabe_surface = schrift.render(eingabe_text, True, schwarz)

        # Text positionieren, sodass er im Textfeld zentriert ist
        text_x = self.rect.x + 5
        text_y = self.rect.y + (self.rect.height - eingabe_surface.get_height()) // 2
        surface.blit(eingabe_surface, (text_x, text_y))


# Klasse für das Ausgabefeld
class OutputText:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""

    def draw(self, surface):
        pygame.draw.rect(surface, schwarz, self.rect, 2)
        ausgabe_surface = schrift.render(self.text, True, schwarz)
        text_x = self.rect.x + 5
        text_y = self.rect.y + (self.rect.height - ausgabe_surface.get_height()) // 2
        surface.blit(ausgabe_surface, (text_x, text_y))


# Textfelder erstellen
text_input = TextInput(50, 50, 300, 30)
ausgabe_textfeld = OutputText(50, 100, 300, 30)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        text_input.handle_event(event)

    text_input.update()

    # Hintergrund löschen
    bildschirm.fill(weiß)

    # Textfelder zeichnen
    text_input.draw(bildschirm)
    ausgabe_textfeld.draw(bildschirm)

    pygame.display.flip()
    clock.tick(30)
