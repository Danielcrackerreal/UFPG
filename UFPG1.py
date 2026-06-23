#welcome to the games code. um, nothing to look here but....
import time

level = 0

#the talking stuff
def say(stentence): 
    for i in stentence :
        print(i,end='')
        time.sleep(0.05)
    print()
#first part
def tutorial():
    global level
    say('Docking. complete.')
    say('*Ring.. Ring...')
    say('HELLO? IS ANYBODY THERE? OH WAIT FRICK THE VOLUme\nyeah sorry about that\nit\'s me! Jonas parker from the newspaper!')
    say('with my guide, you may find secrets apon my factory, \nthe gaurded license!')
    say('say, what brings you here?')
    input('Game     You     silence')
    say('oh thats a good reason.\nlet me tell about me.\ni was CEO of this place until some person got jelous and took my spot. he trapped me in this cage.\nand thats why i put this in case someone comes to our strange little factory in space!')
    say('wait whats that noise')
    say('hmm.. seems like ya found a GOLDEN TOOTH')
    say('don\'t panic you could um.. oh! uh.. check\nTHE DICTIONARY')
    say('*dictionary equiped')
    say('*you open the dictionary.\n*dusty.')
    say('what you need to do my friend, is to search \'Golden tooth\'')
    say('*you go to page 6.')
    print('Golden Tooth\n')
    print('strong points        hearing\nweak points        seeing')
    say('okay then! now should prolly sneak in? i guess')
    print('(saved..)(if rejoined, not saved.)')
    level += 1
    input('sneak in         don\'t')
    say('ah no one cares what ya say ')
    say('                            ')
    print('memorize the right path to not make a sound.')
    print('not 5 but not 6 its greater then them but smaller then 8')
    fq = input('4       8       7')
    if fq == 7:
        say('                                                   safe.')
        print('when clock hits nine, i go to a place. its called seven [].\nwhat might be []?')
        q2 = input('11          13          7')
        if q2 == 11:
            say('                                                   safe.')
        else:
            say('                                                       NOT SAFE')
    else:
        say('                                                       NOT SAFE')
        print('========================================================================')
        say('hey, you there? i heard some death sounds there\nHello? Hello?')
#intro part
def intro():
    say('\'ello!(british ahh)\n')
    say('U  N   T   I   T   L   E   D       F   R   E   A   K   Y       \nP   U   Z   Z   L   E       G   A   M   E')
    say('made by Daniel Cracker')
    print('Play         Exit')
    st = input('')
    if st == 'Exit':
        say('\n\'ye!(british ahh)')
    elif st == 'Play':
        print('loading',end="")
        say('................')
        tutorial()
    else:
        say('say whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat?')












#the bottemFULL pit













#almost there..











#we here!
intro()
