from flask import Flask
from random import randint

chosen_number = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
    return '<div style="text-align: center"><h1>Guess a number between 0 and 9</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHFoMGZ4NGl5Z3RiOW54dXYzcm4ybGptcnpkamNla21vZ2NmZ2IwZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif" /></div>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < chosen_number:
        return '<div style="text-align: center"><h1 style="color: red">Too low, try again!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDNibnA3ZGJ3MHF1MGRieDVla21lZ2ZjYmNpdnltbXc5bjNoMDFpMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CM1rHbKDMH2BW/giphy.gif" /></div>'
    
    elif guess > chosen_number:
        return '<div style="text-align: center"><h1 style="color: blue">Too high, try again!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmN2Nnh4OGo5NmU1OWhieGdnbXZ6OTVobzI5cnM3Nnp4bm9pbjV4cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TZBED1pP5m8N2/giphy.gif" /></div>'
    
    else:
        return '<div style="text-align: center"><h1 style="color: green">You found me!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGl2bzFwYW9tdm4yenExd2N3MjZ6dWpnaHVpeHk3ZDA4dHpmNDkyayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IUm2IUJcZqKZnfWDDo/giphy.gif" /></div>'


if __name__ == "__main__":
    app.run()