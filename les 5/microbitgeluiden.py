from microbit import *
import speech
rest = ["cookies", "an essay", "drawing"]

def SayTheWords1(word):
    print(word)
    speech.say(word, speed=100, pitch=100 , throat=100, mouth=100)
    sleep(500)

def SayTheWords2(): 
    willekeurigGetal1 = random.randint(0, LengteWoordArray - 1)
    willekeurigGetal2 = random.randint(0, LengteWoordArray - 1)
    willekeurigGetal3 = random.randint(0, LengteWoordArray - 1)
    display.show(willekeurigGetal1 + willekeurigGetal2 + willekeurigGetal3)
    SayTheWords1(onderwerp[willekeurigGetal1])
    SayTheWords1(werkwoord[willekeurigGetal2])
    SayTheWords1(rest[willekeurigGetal3])

while True:
    if button_a.is_pressed(): 
        display.show(Image.CONFUSED)
        sleep(2000)
        display.scroll("Hallo")
        SayTheWords1()
    elif button_b.is_pressed(): 
        display.show(Image.MEH)
        sleep(2000)
        display.scroll("Doei")
        SayTheWords1()
    elif display.read_light_level() < 50:
        SayTheWords2()
    else:
        display.show(Image.ANGRY)