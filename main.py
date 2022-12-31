from config import *

while True:
    text3 = pygame.font.SysFont("Arial", 20, bold=True).render(f"Countries Destroyed: {countries}", False, (255, 255, 255))
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if 50 < mouse_pos_x < 150 and 50 < mouse_pos_y < 150:
            color = color_hover
            if i.type == pygame.MOUSEBUTTONDOWN:
                color = color_active
                countries += 1
        elif width - 150 < mouse_pos_x < width - 50 and 50 < mouse_pos_y < 150:
            color1 = color_hover
            if i.type == pygame.MOUSEBUTTONDOWN:
                color1 = color_active
                say_a_phrase()
        elif width // 2 - 75 < mouse_pos_x < width // 2 + 75 and 250 < mouse_pos_y < 300:
            color2 = color_hover
            if i.type == pygame.MOUSEBUTTONDOWN:
                color2 = color_active
                exit()
        else:
            color = color_passive
            color1 = color_passive
            color2 = color_passive

    sc.fill("black")
    sc.blit(image, (0, 0))
    pygame.draw.circle(sc, color, (100, 100), 60)
    pygame.draw.circle(sc, color1, (width-100, 100), 60)
    pygame.draw.rect(sc, color2, (width//2-75, height-55, 150, 50))
    sc.blit(text, (45, 90))
    sc.blit(text1, (width-150, 90))
    sc.blit(text2, (width//2-50, height-55))
    sc.blit(text3, (0, height-25))
    pygame.display.flip()
    clock.tick(fps)
