import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    
    #画像サーフェイス
    bg_img = pg.image.load("ex01_2/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01_2/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, kk_img2]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x,0])
        screen.blit(kk_imgs[(tmr//50)%2],[300,200])
        if x==3200:
            x = 0
          
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()