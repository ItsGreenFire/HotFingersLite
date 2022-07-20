import pyautogui as pag
import keyboard
import pygame
import pygame as pg

pag.PAUSE = .02  # Sets speed
pygame.init()


def main():
    speed = 0
    hotkey = 'r'
    toggleActive = False
    clock = pg.time.Clock()
    pg.display.set_icon(pygame.image.load('wiiCursor.png'))
    pg.display.set_caption("HF Lite")
    screen = pg.display.set_mode((225, 207))

    color_inactive = pg.Color((100, 100, 100))
    color_active = pg.Color('silver')
    color = color_inactive
    subfont = pg.font.Font(None, 16)
    font = pg.font.Font(None, 32)
    headerFont = pg.font.Font(None, 48)

    speed_input_box = pg.Rect(10, 65, 50, 32)
    hotkey_input_box = pg.Rect(10, 135, 50, 32)
    done_button_box = pg.Rect(10, 175, 65, 32)
    window_border = pg.Rect(screen.get_rect())

    speedBoxActive = False
    speedInputText = '0'
    hotkeyBoxActive = False
    hotkeyInputText = 'r'
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN and not toggleActive:
                if speed_input_box.collidepoint(event.pos):
                    speedBoxActive = not speedBoxActive
                else:
                    speedBoxActive = False
                if hotkey_input_box.collidepoint(event.pos):
                    hotkeyBoxActive = not hotkeyBoxActive
                else:
                    hotkeyBoxActive = False
                color = color_active if speedBoxActive or hotkeyBoxActive else color_inactive
            if event.type == pg.KEYDOWN:
                if speedBoxActive and len(str(speedInputText)) < 6:
                    if event.key == pg.K_BACKSPACE:
                        if len(str(speedInputText)) == 1:
                            speedInputText = 0
                        else:
                            speedInputText = speedInputText[:-1]
                    elif pg.key.name(event.key).isdigit():
                        if speedInputText == 0:
                            speedInputText = event.unicode
                        else:
                            speedInputText += event.unicode
                    speed = int(speedInputText)
                if hotkeyBoxActive:
                    hotkeyInputText = event.unicode
                    hotkey = hotkeyInputText
        while keyboard.is_pressed(hotkey):
            pag.click(pag.position())
            clock.tick(speed)

        screen.fill((60, 60, 60))

        # Text Surfaces
        sp_txt_surface = font.render(str(speedInputText), True, color)
        hk_txt_surface = font.render(str(hotkeyInputText), True, color)
        done_txt_surface = font.render("Done", True, "silver")

        # Adaptive Resizing
        sp_width = max(50, sp_txt_surface.get_width() + 10)
        speed_input_box.w = sp_width
        hk_width = max(50, hk_txt_surface.get_width() + 10)
        hotkey_input_box.w = hk_width

        # Blits
        screen.blit(pg.image.load("wiiCursorLarge.png"), (105, 30))
        screen.blit(headerFont.render('Hot Fingers L', False, "silver"), (6, 10))
        screen.blit(font.render('Interval', False, "silver"), (speed_input_box.x, speed_input_box.y - 25))
        screen.blit(font.render('Hot Key', False, "silver"), (hotkey_input_box.x, hotkey_input_box.y - 25))
        screen.blit(subfont.render('V1.0', False, "silver"), (200, 3))
        screen.blit(subfont.render('Made By ItsGreenFire', False, "silver"), (110, 195))
        screen.blit(sp_txt_surface, (speed_input_box.x + 5, speed_input_box.y + 5))
        screen.blit(hk_txt_surface, (hotkey_input_box.x + 5, hotkey_input_box.y + 5))
        screen.blit(done_txt_surface, (done_button_box.x + 5, done_button_box.y + 5))

        # PyGame Drawing
        pg.draw.rect(screen, color, speed_input_box, 2)
        pg.draw.rect(screen, color, hotkey_input_box, 2)
        pg.draw.rect(screen, "silver", done_button_box, 2)
        pg.draw.rect(screen, "silver", window_border, 2)

        pg.display.flip()


main()  # Calling Main Function
