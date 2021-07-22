import play
from random import randint

#instructions
manual_text = play.new_text(
        words="Hello! Click the button to test your luck",
        x=0,y=240,
        font=None,
        font_size=50,
        color="green"
    )
    
#button to randomize number
spin_button = play.new_box(
        color="yellow",
        x=0, y=130,
        width=105,
        height=45,
    )

#text to randomize number
spin_text = play.new_text(
        words="SPIN!",
        x=0, y=130,
        font=None,
        font_size=35,
        color="purple"
    )

#win
win_text = play.new_text(
        words="Yøü Wiñ!",
        x=0, y=-245,
        font=None,
        font_size=40,
        color="green"
    )

#lose
lose_text = play.new_text(
        words="Yøü Łøșě! T®¥ āgàiñ!",
        x=0, y=-245,
        font=None,
        font_size=40,
        color="green"
    )

numbered_box_1 = play.new_box(
        border_color="green", color="light green",
        border_width=5,
        x=-190, y=-40,
        width=80,
        height=150,
    )

numbered_box_2 = play.new_box(
        border_color="green", color="light green",
        border_width=5,
        x=0, y=-40,
        width=80,
        height=150,
    )

numbered_box_3 = play.new_box(
        border_color="green", color="light green",
        border_width=5,
        x=190, y=-40,
        width=80,
        height=150,
    )

times_box = play.new_box(
        border_color="orange", color="yellow",
        border_width=2,
        x=210, y=-190,
        width=150,
        height=40
    )

times_text = play.new_text(
        words="0",
        x=250, y=-190,
        font=None,
        font_size=50,
        color="red"
)
times_text2 = play.new_text(
        words="Time:",
        x=190, y=-190,
        font=None,
        font_size=50,
        color="red"
)

number_no1 = play.new_text(
        words="0",
        x=-190, y=-40,
        font=None,
        font_size=90,
        color="purple",
)
        
number_no2 = play.new_text(
        words="0",
        x=0, y=-40,
        font=None,
        font_size=90,
        color="purple"
)

number_no3 = play.new_text(
        words="0",
        x=190, y=-40,
        font=None,
        font_size=90,
        color="purple"
)

warning_text = play.new_text(
        words="[ONLY click after 1 SECONDS]",
        x=0, y=190,
        font=None,
        font_size=30,
        color="red"
)

#when program starts
@play.when_program_starts
def start():
    #hide win and lose
    win_text.hide()
    lose_text.hide()

#when spin button is clicked
@spin_button.when_clicked
async def clicked():
    number_no1.words = randint(0, 9)
    number_no2.words = randint(0, 9)
    number_no3.words = randint(0, 9)

    #if the numbers are the same win
    if int(number_no1.words) == int(number_no2.words) == int(number_no3.words):
        win_text.show()
        times_text.words = int(times_text.words) + 1
    else:
        lose_text.show()
        times_text.words = int(times_text.words) + 1

    #reset after a second
    await play.timer(seconds = 1)
    number_no1.words = "0"
    number_no2.words = "0"
    number_no3.words = "0"
    win_text.hide()
    lose_text.hide()

play.start_program()