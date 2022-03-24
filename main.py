@namespace
class SpriteKind:
    End = SpriteKind.create()
    object2 = SpriteKind.create()
    EnemyProjectile = SpriteKind.create()
    Coin = SpriteKind.create()
    flyingenemy = SpriteKind.create()
    bossmovementtype = SpriteKind.create()

def on_overlap_tile(sprite3, location):
    global level
    level += 1
    info.change_score_by(1)
    createLevel()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile)

def on_up_pressed():
    global attack, attackcooldown, projectile, projectile2
    if attack == 0:
        attack = 1
        attackcooldown = 10
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . b b . . . . . . . 
                            . . . . . . b c c b . . . . . . 
                            . . . . . . f c c f . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            200,
            0)
        projectile2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . b b . . . . . . . 
                            . . . . . . b c c b . . . . . . 
                            . . . . . . f c c f . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -200,
            0)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy(effects.hearts, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.EnemyProjectile, SpriteKind.player, on_on_overlap)

def on_b_pressed():
    global dash_cooldown, dash
    if dash == 0:
        dash_cooldown = 2
        dash = 1
        controller.move_sprite(mySprite, 300, 0)
        mySprite.vy = 0
        pause(200)
        controller.move_sprite(mySprite, 100, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def createLevel():
    for value in sprites.all_of_kind(SpriteKind.Coin):
        value.destroy()
    if level == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        makecoins()
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        makecoins()
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 3:
        tiles.set_current_tilemap(tilemap("""
            level3
        """))
        makecoins()
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 4:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        makecoins()
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 5:
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        makecoins()
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 6:
        game.show_long_text("good job getting this far, but the king has sent his strongest child to kill you, defeat her and continue your journey by leaving your home through the cave entrance",
            DialogLayout.FULL)
        tiles.set_current_tilemap(tilemap("""
            Boss Fight
        """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        Make_boss()
    elif level == 7:
        tiles.set_current_tilemap(tilemap("""
            secretlevel
        """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level == 8:
        game.show_long_text("you have achieved the true ending of world 1, good job!",
            DialogLayout.FULL)
    elif level == 9:
        scene.set_background_image(img("""
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
                        7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
                        7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
                        6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
                        6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
                        6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
                        6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
                        6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
                        66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
                        66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
                        66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
                        66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
                        66b66666699dbb666666dd9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
                        6bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb666666666666
                        6bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb66666666666
                        6bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb66666666666
                        bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666
                        bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666
                        bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666
                        bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966
                        bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996
                        bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999
                        bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999
                        bb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999b
                        bb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999b
                        bb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999b
                        b9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99b
                        b9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99b
                        b9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bb
                        b9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbb
                        dd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbb
                        9d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb9
                        9d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb99
                        9d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb999
                        9dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd99
                        99dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd99
                        99ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd9
                        9999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d9
                        9999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d9
                        999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd
                        d9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999d
                        dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999
                        dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999
                        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
                        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
                        ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999
                        dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999
                        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
                        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
                        dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999
                        d99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999d
                        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
                        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
                        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
                        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
                        999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9
                        9999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd9
                        d999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbdddddddd
                        ddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbddddddd
                        dddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddd
                        ddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbddddddd
                        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
                        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
                        dddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddd
                        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                        ddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbddddd
                        dddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddd
                        ddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777dddd
                        dddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dd
                        ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        """))
        tiles.set_current_tilemap(tilemap("""
            level24
        """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        create_enemy()
    else:
        pass

def on_overlap_tile2(sprite5, location3):
    global spawninvulnerability
    if spawninvulnerability == 0:
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        info.change_life_by(-1)
        spawninvulnerability = 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile2)

def on_hit_wall(sprite6, location4):
    sprite6.destroy(effects.hearts, 100)
scene.on_hit_wall(SpriteKind.EnemyProjectile, on_hit_wall)

def makecoins():
    global dark_coin
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        Coinblock1
    """)):
        dark_coin = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . f f f f f f . f f f f f f . 
                            . f f c c c c f f f c c c c f f 
                            . f c c c c c c f c c c c c c f 
                            . f c c c c c c c c b b b c c f 
                            . f c c c c c c c c b b b c c f 
                            . f c c c c c a a a b b b c c f 
                            . f c c c c a a a a a c c c c f 
                            . f f c c a a a a a a a c c f f 
                            . . f f c a a a a a a a c f f . 
                            . . . f f a a a a a a a f f . . 
                            . . . . f f a a a a a f f . . . 
                            . . . . . f f a a a f f . . . . 
                            . . . . . . f f a f f . . . . . 
                            . . . . . . . f f f . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Coin)
        tiles.place_on_tile(dark_coin, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))

def on_a_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -200
        pause(500)
        mySprite.vy = 200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f1111111dbf......
                        ......fd1111111ddf......
                        ......fd111111dddf......
                        ......fd111ddddddf......
                        ......fd111ddddddf......
                        ......fd1dddddddbf......
                        ......fd1dfbddbbff......
                        ......fbddfcdbbcf.......
                        .....ffffccddbfff.......
                        ....fcb1bbbfcffff.......
                        ....f1b1dcffffffff......
                        ....fdfdf..ffffffff.....
                        .....f.f.....fffff......
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f1111111dbf......
                        ......fd1111111ddf......
                        ......fd111111dddf......
                        ......fd111ddddddf......
                        ......fd111ddddddf......
                        ......fd1dddddddbf......
                        ......fd1dfbddbbff......
                        ......fbddfcdbbcf.......
                        ......ffffcddbfff.......
                        .....fcb1bbfcffff.......
                        .....f1b1dffffffff......
                        .....fdfdf.ffffffff.....
                        ......f.f....fffff......
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f1111111dbf......
                        ......fd1111111ddf......
                        ......fd111111dddf......
                        ......fd111ddddddf......
                        ......fd111ddddddf......
                        ......fd1dddddddbf......
                        ......fd1dfbddbbff......
                        ......fbddfcdbbcf.......
                        ......ffffcddbfff.......
                        .....fcb1bbfcffff.......
                        .....f1b1dfffffff.......
                        .....fdfdf.fffffff......
                        ......f.f....ffffff.....
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_hit_wall2(sprite4, location2):
    sprite4.destroy(effects.ashes, 100)
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall2)

def on_hit_wall3(sprite2, location5):
    sprite2.vy = 0 - sprite2.vy
scene.on_hit_wall(SpriteKind.bossmovementtype, on_hit_wall3)

def on_right_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim0
    """), 200, True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite22, otherSprite2):
    info.player2.change_score_by(1)
    otherSprite2.destroy(effects.fire, 200)
    if info.player2.score() == 1:
        game.show_long_text("this is a coin there are 3 hidden in each level",
            DialogLayout.FULL)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap2)

def create_enemy():
    global lightenemy
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        enemy_spawn
    """)):
        lightenemy = sprites.create(assets.image("""
            enemy_bat
        """), SpriteKind.flyingenemy)
        tiles.place_on_tile(lightenemy, value3)
        tiles.set_tile_at(value3, assets.tile("""
            transparency16
        """))
        lightenemy.vy = -75

def on_life_zero():
    global level
    if level < 7:
        game.over(False, effects.blizzard)
    elif level == 7:
        info.set_life(5)
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    elif level > 8:
        game.show_long_text("you have lost, luckily you will spawn at the start of world 2",
            DialogLayout.FULL)
        level = 9
        info.set_life(5)
        info.player2.change_score_by(15)
    else:
        pass
info.on_life_zero(on_life_zero)

def on_hit_wall4(sprite7, location6):
    sprite7.vy = 0 - sprite7.vy
scene.on_hit_wall(SpriteKind.flyingenemy, on_hit_wall4)

def Make_boss():
    global Boss, Boss_health
    Boss = sprites.create(img("""
            . . . . . . 5 . 5 . . . . . . . 
                    . . . . . f 5 5 5 f f . . . . . 
                    . . . . f 1 5 2 5 1 6 f . . . . 
                    . . . f 1 6 6 6 6 6 1 6 f . . . 
                    . . . f 6 6 f f f f 6 1 f . . . 
                    . . . f 6 f f d d f f 6 f . . . 
                    . . f 6 f d f d d f d f 6 f . . 
                    . . f 6 f d 3 d d 3 d f 6 f . . 
                    . . f 6 6 f d d d d f 6 6 f . . 
                    . f 6 6 f 3 f f f f 3 f 6 6 f . 
                    . . f f d 3 5 3 3 5 3 d f f . . 
                    . . f d d f 3 5 5 3 f d d f . . 
                    . . . f f 3 3 3 3 3 3 f f . . . 
                    . . . f 3 3 5 3 3 5 3 3 f . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.bossmovementtype)
    tiles.place_on_random_tile(Boss, assets.tile("""
        myTile2
    """))
    Boss_health = 10
    Boss.change_scale(2, ScaleAnchor.MIDDLE)
    Boss.vy = -25

def on_on_overlap3(sprite72, otherSprite3):
    global Boss_health, level
    Boss_health += -1
    sprite72.destroy(effects.disintegrate, 100)
    if Boss_health == 0:
        Boss.destroy(effects.hearts, 1000)
        if info.player2.score() == 15:
            game.show_long_text("you have collected all coins and unlocked the bonus level",
                DialogLayout.FULL)
            level += 1
            createLevel()
        elif info.player2.score() < 15:
            game.show_long_text("you have beaten world 1, world 2 is harder",
                DialogLayout.FULL)
            level += 3
            createLevel()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite8, otherSprite4):
    tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

Boss_Projectile: Sprite = None
Boss_health = 0
Boss: Sprite = None
lightenemy: Sprite = None
dark_coin: Sprite = None
spawninvulnerability = 0
dash_cooldown = 0
dash = 0
projectile2: Sprite = None
projectile: Sprite = None
attackcooldown = 0
attack = 0
mySprite: Sprite = None
level = 0
level = 1
info.set_score(1)
info.player2.set_score(0)
scene.set_background_color(12)
mySprite = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f1111111df.......
            ......fd1111111ddf......
            ......fd111111dddf......
            ......fd111ddddddf......
            ......fd1dfbddddbf......
            ......fbddfcdbbbcf......
            .......f11111bbcf.......
            .......f1b1fffff........
            .......fbfc111bf........
            ........ff1b1bff........
            .........fbfbfff.f......
            ..........ffffffff......
            ............fffff.......
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
createLevel()
info.set_life(5)
controller.move_sprite(mySprite, 100, 0)
scene.camera_follow_sprite(mySprite)
mySprite.ay += 200
game.show_long_text("you are a lonely ghost, living peacefully in your dungeon, but the king thinks your evil, your quest is to set out and prove him wrong",
    DialogLayout.FULL)

def on_update_interval():
    global Boss_Projectile
    if Boss_health > 0:
        Boss_Projectile = sprites.create_projectile_from_sprite(img("""
                . f f f . f f f . 
                            f 3 3 3 f 3 3 3 f 
                            f 3 3 3 3 3 1 3 f 
                            f 3 3 3 3 3 3 3 f 
                            . f 3 b b b 3 f . 
                            . f f b b b f f . 
                            . . f f b f f . . 
                            . . . f f f . . .
            """),
            Boss,
            50,
            0)
        Boss_Projectile.set_kind(SpriteKind.EnemyProjectile)
        Boss_Projectile.follow(mySprite, 50)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    for value4 in sprites.all_of_kind(SpriteKind.flyingenemy):
        value4.vy = 0 - value4.vy
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    for value5 in sprites.all_of_kind(SpriteKind.bossmovementtype):
        value5.vy = 0 - value5.vy
game.on_update_interval(2000, on_update_interval3)

def on_update_interval4():
    global spawninvulnerability
    spawninvulnerability = 0
game.on_update_interval(500, on_update_interval4)

def on_update_interval5():
    global attack, attackcooldown
    if attackcooldown == 0:
        attack = 0
    elif attackcooldown > 0:
        attackcooldown += -1
game.on_update_interval(100, on_update_interval5)

def on_update_interval6():
    global dash, dash_cooldown
    if dash_cooldown == 0:
        dash = 0
    elif dash_cooldown > 0:
        dash_cooldown += -1
game.on_update_interval(100, on_update_interval6)
