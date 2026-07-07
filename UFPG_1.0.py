import tkinter as tk
import time


root = tk.Tk()
root.title("this is untitled!")
root.geometry("800x700")
root.resizable(True, False)


# =========================
# 텍스트 박스 + 스크롤
# =========================

text_frame = tk.Frame(root)
text_frame.pack(padx=15, pady=15, fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(
    text_frame,
    font=("맑은 고딕", 12),
    wrap="word",
    state="disabled",
    yscrollcommand=scrollbar.set
)
text_box.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_box.yview)


# =========================
# 버튼 프레임
# =========================

button_frame = tk.Frame(root, height=170)
button_frame.pack(padx=10, pady=10, fill="x")
button_frame.pack_propagate(False)

choice_buttons = []
choice_var = tk.StringVar()


# =========================
# 버튼 숨기기 / 보이기
# =========================

def hide_buttons():
    for button in choice_buttons:
        button.grid_remove()


def clear_buttons():
    for button in choice_buttons:
        button.destroy()
    choice_buttons.clear()


# =========================
# 한 글자씩 출력
# =========================

def say(speed, text=''):

    if isinstance(speed, str):
        text = speed
        speed = 0.05  
        #기본 출력속도 0.05. say('문장') 
        #속도 0으로 출력. 숫자를 바꾸면 출력속도 변경가능 say(0,'문장') 

    hide_buttons()

    text_box.config(state="normal")

    if text_box.get("1.0", tk.END).strip() != "":
        text_box.insert(tk.END, "\n\n")

    for ch in text:
        text_box.insert(tk.END, ch)
        text_box.see(tk.END)
        root.update()
        time.sleep(speed)

    text_box.config(state="disabled")


# =========================
# 선택지 만들기
# =========================

def make_choices(*choices):
    clear_buttons()
    choice_var.set("")

    choices = choices[:15]

    for i, choice in enumerate(choices):
        row = i // 5
        col = i % 5

        button = tk.Button(
            button_frame,
            text=choice,
            width=20,
            height=2,
            font=("맑은 고딕", 10),
            command=lambda c=choice: choice_var.set(c)
        )

        button.grid(row=row, column=col, padx=5, pady=5)
        choice_buttons.append(button)

    root.wait_variable(choice_var)

    selected = choice_var.get()
    clear_buttons()

    return selected

def game_over(restart=None):
    button = tk.Button(
            button_frame,
            text='restart',
            width=20,
            height=2,
            font=("맑은 고딕", 10),
            command=tutorial
        )
    button.grid(row=0, column=0, padx=5, pady=5)
    choice_buttons.append(button)

    root.wait_variable(choice_var)

    selected = choice_var.get()
    clear_buttons()

    


# =========================
# 게임 내용
# =========================
level = 0

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
    say('strongness: hearing')
    say('weakness: seeing')
    say('okay then! now should prolly sneak in? i guess')

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
            say('hey didya make it?\nyes?\nok then')
            say('ok we escaped')
            say('OMG that must be!')
            say(0,'H.H.')
            say(0,'#will commit changes soon')
            game_over()
        else:
            say('                                                       NOT SAFE')
            say('========================================================================')
            say('hey, you there? i heard some death sounds there\nHello? Hello?')
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
