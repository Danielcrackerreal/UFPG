def say(speed, text=''):

    if isinstance(speed, str):
        text = speed
        speed = 0.05  
        #기본 출력속도 0.05. say('문장') 
        #속도 0으로 출력. 숫자를 바꾸면 출력속도 변경가능 say(0,'문장') 
def tutorial():
    global level
    say('Docking. complete.')
    say('*Ring.. Ring...')
    say('HELLO? IS ANYBODY THERE? OH WAIT FRICK THE VOLUme\nyeah sorry about that\nit\'s me! Jonas parker from the newspaper!')
    say('with my guide, you may find secrets apon my factory, \nthe gaurded license!')
    say('say, what brings you here?')
    choice = make_choices("Game", "You", "silence")

    say('oh thats a good reason.\nlet me tell about me.\ni was CEO of this place until some person got jelous and took my spot. he trapped me in this cage.\nand thats why i put this in case someone comes to our strange little factory in space!')
    say('wait whats that noise')
    say('hmm.. seems like ya found a GOLDEN TOOTH')
    say('don\'t panic you could um.. oh! uh.. check\nTHE DICTIONARY')
    say('*dictionary equiped')
    say('*you open the dictionary.\n*dusty.')
    say('what you need to do my friend, is to search \'Golden tooth\'')
    say('*you go to page 6.')
    say('Golden Tooth\n')

    choice = make_choices("strong points", "hearing", "weak points", "seeing")
    say('okay then! now should prolly sneak in? i guess')
    say(0,'(saved..)(if rejoined, not saved.)') #속도 0으로 출력
    level += 1

    choice = make_choices("sneak in", "don\'t")
    say('ah no one cares what ya say ')
    say('                            ')
    say(0,'memorize the right path to not make a sound.')
    say(0,'not 5 but not 6 its greater then them but smaller then 8')
    fq = make_choices("4", "8", '7')
    if fq == '7':
        say('                                                   safe.')
        say(0, 'when clock hits nine, i go to a place. its called seven [].\nwhat might be []?')
        q2 = make_choices("11", "13", '7')
        if q2 == '11':
            say('                                                   safe.')
        else:
            say('                                                       NOT SAFE')
            game_over()
    else:
        say('                                                       NOT SAFE')
        say('========================================================================')
        say('hey, you there? i heard some death sounds there\nHello? Hello?')
        game_over()


#intro part
def intro():
    say('\'ello!(british ahh)\n')
    say('U  N   T   I   T   L   E   D       F   R   E   A   K   Y       \nP   U   Z   Z   L   E       G   A   M   E')
    say('made by Daniel Cracker')
    st = make_choices("Play", "Exit")
    if st == 'Exit':
        say('\n\'ye!(british ahh)')
        game_over()
    elif st == 'Play':
        print('loading',end="")
        say('................')
        tutorial()
    else:
        say('say whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat?')


# 창이 뜬 다음 게임 시작
root.after(100, intro)

root.mainloop()
