import eel
import lib
import sqlite3 as sq3 

eel.init('./gui')

@eel.expose
def App():
    print('a')

App()

eel.start('index.html',size=(500,600))
