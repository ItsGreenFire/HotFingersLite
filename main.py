import pyautogui as pag
import keyboard
import pygame
import pygame as pg

pag.PAUSE = .005  # TODO: MAKE SETTINGS
speed = 0
hotkey = 'r'
toggleActive = False

pygame.init()


def autoClick():
    pag.click(pag.position())


def main():
    global speed, hotkey, toggleActive
    clock = pg.time.Clock()
    pg.display.set_icon(pygame.image.load('wiiCursor.png'))
    pg.display.set_caption("Hot Fingers L")
    screen = pg.display.set_mode((300, 300))

    color_inactive = pg.Color('darkred')
    color_active = pg.Color('red')
    color = color_inactive
    font = pg.font.Font(None, 32)
    headerFont = pg.font.Font(None, 48)

    togold_button_box = pg.Rect(80, 100, 100, 32)
    speed_input_box = pg.Rect(10, 100, 50, 32)
    hotkey_input_box = pg.Rect(10, 170, 50, 32)
    window_border = pg.Rect(0, 0, 300, 300)

    speedBoxActive = False
    speedInputText = '0'
    hotkeyBoxActive = False
    hotkeyInputText = 'r'
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the speed_input_box rect.
                if speed_input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    speedBoxActive = not speedBoxActive
                    print(speedBoxActive)
                else:
                    speedBoxActive = False
                if hotkey_input_box.collidepoint(event.pos):
                    hotkeyBoxActive = not hotkeyBoxActive
                else:
                    hotkeyBoxActive = False
                if togold_button_box.collidepoint(event.pos):
                    toggleActive = not toggleActive
                # Change the current color of the input box.
                color = color_active if speedBoxActive or hotkeyBoxActive else color_inactive
            if event.type == pg.KEYDOWN:
                if speedBoxActive and pg.key.name(event.key).isdigit():
                    if event.key == pg.K_BACKSPACE:
                        speedInputText = speedInputText[:-1]
                    else:
                        speedInputText += event.unicode
                    speed = int(speedInputText)
                if hotkeyBoxActive:
                    hotkeyInputText = event.unicode
                    hotkey = hotkeyInputText
        while keyboard.is_pressed(hotkey) and not speedBoxActive and not hotkeyBoxActive:
            autoClick()
            clock.tick(speed)

        screen.fill((30, 30, 30))
        # Render the current speedInputText.
        sp_txt_surface = font.render(str(speedInputText), True, color)
        hk_txt_surface = font.render(str(hotkeyInputText), True, color)
        # Resize the box if the speedInputText is too long.
        sp_width = max(50, sp_txt_surface.get_width() + 10)
        speed_input_box.w = sp_width
        hk_width = max(50, hk_txt_surface.get_width() + 10)
        hotkey_input_box.w = hk_width
        # Blit the speedInputText.
        screen.blit(headerFont.render('Hot Fingers Lite', False, "#ff2146"), (10, 10))
        screen.blit(font.render('Interval', False, "red"), (speed_input_box.x, speed_input_box.y - 25))
        screen.blit(font.render('Hot Key', False, "red"), (hotkey_input_box.x, hotkey_input_box.y - 25))
        screen.blit(sp_txt_surface, (speed_input_box.x + 5, speed_input_box.y + 5))
        screen.blit(hk_txt_surface, (hotkey_input_box.x + 5, hotkey_input_box.y + 5))
        # Blit the speed_input_box rect.
        pg.draw.rect(screen, color, speed_input_box, 2)
        pg.draw.rect(screen, color, hotkey_input_box, 2)
        pg.draw.rect(screen, "red", window_border, 2)
        # TODO: DONE BUTTON, START AC BUTTON, END AC BUTTON

        pg.display.flip()


main()
