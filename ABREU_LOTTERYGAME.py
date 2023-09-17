
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from exit import Ui_Dialogexit
from buy import Ui_Dialogbuy
from deducted import Ui_Dialogdeduct
from nobalance import Ui_Dialogsorry
import random
import sys


#THESE ARE JUST THE VARIABLES THAT WILL BE NEEDED FOR THE GAME LIKE SCORES, USER ENTRIES, ETC.
toy=""; toys=[]; ptoy=""
pwallet=""
sjackpot=100; ujackpot=200; hjackpot=100; phjackpot=150
srands=[]; srand1=0; srand2=0; srand3=0
sguessnum=[]
guesshorse=""
hlist=["Achilles", "Bullseye", "Gulliver", "Maximus", "Petra", "Rambo"]
randhorse=random.choice(hlist)
guess1=0; guess2=0; guess3=0
loc=""
loclist = ["Manila", "Cebu", "Davao"]
num = random.randint(30, 100)
land = random.choice(loclist)


class Ui_MainWindow(object):

    #THIS FUNCTION IS FOR EXITING THE PH WAR GAME ONLY
    def exitph(self):
        global pwallet
        self.wphwar.hide()
        self.lblwallet.setText(pwallet)

    #THIS FUNCTION IS FOR THE PLAY AGAIN BUTTON FOR THE PH WAR GAME
    def play_againph(self):
        global loclist, num, land
        global pwallet
        wallet=int(pwallet)
        #WILL CHECK FIRST IF THE PLAYER HAAS ENOUGH MONEY TO PLAY THE GAME
        if wallet < 10:
            #IF THE PLAYER DOESN'T HAVE ENOUGH GAME MONEY, A DIALOG WILL SHOW THAT HE/SHE DOES NOT HAVE ENOUGH MONEY
            self.open_sorry()
            self.pbexitph.setEnabled(False); self.pbplayagainph.setEnabled(False)
        elif wallet > 9:
            #IF PLAYER HAVE ENOUGH MONEY TO PLAY, 10 PESOS WILL BE DEDUCTED TO THE PLAYER'S MONEY
            wallet = wallet - 10
            self.lcdwalletph.display(wallet)
            loclist = ["Manila", "Cebu", "Davao"]
            #GENERATING RANDOM NUMBER AND LOCATION
            num = random.randint(30, 100)
            land = random.choice(loclist)
            self.frresult.hide()
            #DISABLING BUTTONS AND RESETING THE GAME
            self.pbexitph.setEnabled(False); self.pbfight.setEnabled(True); self.pbplayagainph.setEnabled(False); self.lbfilleft.hide()
            self.cbguess1ph.setCurrentIndex(0); self.cbguess2ph.setCurrentIndex(0); self.cbguess3ph.setCurrentIndex(0)

            self.secretnumph.setText(str(num)); self.secretplaceph.setText(land)
        pwallet=str(wallet)
        return loc, num, land, wallet

    #THIS FUNCTION IS FOR THE FIGHT BUTTON IN THE PH WAR GAME
    def fight_action(self):
        global guess1, guess2, guess3
        guess1 = int(self.cbguess1ph.currentText())
        guess2 = int(self.cbguess2ph.currentText())
        guess3 = int(self.cbguess3ph.currentText())
        totalnum= guess1 + guess2 + guess3
        #WILL CHECK IF THE USER HAS ENTERED A TOTAL OF 100 FILIPINOS IN ORDER TO CONTINUE THE GAME
        if totalnum != 100:
            if totalnum < 100:
                self.lbfilleft.show()
                self.lbfilleft.setText("Please assign all of them")
            elif totalnum > 100:
                self.lbfilleft.show()
                self.lbfilleft.setText("You exceeded!!!")
        elif totalnum == 100:
            self.ph_action()
        return guess1, guess2, guess3

    #IF THE USER ENTERED A TOTAL OF 100 FILIPINOS, THE GAME RESUMES
    def ph_action(self):
        global guess1, guess2, guess3
        global loclist, num, land
        global pwallet
        wallet=int(pwallet)

        self.frresult.show()

        self.lblnumofspaniards.setText(str(num))
        self.lblwherespaniadsland.setText(land)
        #CHECKING IF THE USER WINS OR LOSES THE GAME
        if land == "Manila":
            if guess1 > num:
                self.lblwinorlose.setText("YOU SAVED US!🎉")
                wallet=wallet+200
                self.pbfight.setEnabled(False)
            elif guess1 < num:
                self.lblwinorlose.setText("We lost..")
                self.pbfight.setEnabled(False)
            elif guess1 == num:
                self.lblwinorlose.setText("RETREAT!!!")
                self.pbfight.setEnabled(False)
        elif land == "Cebu":
            if guess2 > num:
                self.lblwinorlose.setText("YOU SAVED US!🎉")
                wallet = wallet + 200
                self.pbfight.setEnabled(False)
            elif guess2 < num:
                self.lblwinorlose.setText("We lost..")
                self.pbfight.setEnabled(False)
            elif guess2 == num:
                self.lblwinorlose.setText("RETREAT!!!")
                self.pbfight.setEnabled(False)
        elif land == "Davao":
            if guess3 > num:
                self.lblwinorlose.setText("YOU SAVED US!🎉")
                wallet = wallet + 200
                self.pbfight.setEnabled(False)
            elif guess3 < num:
                self.lblwinorlose.setText("We lost..")
                self.pbfight.setEnabled(False)
            elif guess3 == num:
                self.lblwinorlose.setText("RETREAT!!!")
                self.pbfight.setEnabled(False)

        self.pbplayagainph.setEnabled(True); self.pbexitph.setEnabled(True); self.lcdwalletph.display(wallet)
        pwallet=str(wallet)
        return pwallet

    #THIS IS THE FUNCTION WHEN THE USER CLICKED THE PHWAR BUTTON ON THE MAIN MENU OF THE GAME
    def open_phwar(self):
        global pwallet, phjackpot
        global loclist, land, num
        wallet=int(pwallet)
        wallet-=10

        if wallet < 10:
            self.open_sorry()
        elif wallet > 9:
            wallet -= 10
            self.open_deduct()

            #HIDING THE RESULT FRAME AND RESETING THE GAME
            self.frresult.hide(); self.lbfilleft.hide(); self.pbfight.setEnabled(True)

            self.wphwar.show(); self.hwidget.hide(); self.wultra.hide(); self.wsuperlottery.hide()
            self.pbplayagainph.setEnabled(False); self.pbexitph.setEnabled(False)
            self.lcdprizeph.display(phjackpot); self.lcdwalletph.display(wallet)
            self.secretplaceph.setText(land); self.secretnumph.setText(str(num))
            self.cbguess1ph.setCurrentIndex(0); self.cbguess2ph.setCurrentIndex(0); self.cbguess3ph.setCurrentIndex(0)
            pwallet=str(wallet)
        return pwallet, land, num

    #THIS IS FOR THE EXIT BUTTON IN THE HORSE RACE GAME
    def horseexit(self):
        global pwallet
        self.hwidget.hide()
        self.lblwallet.setText(pwallet)

    #THIS IS FOR THE SEE RESULTS BUTTON OF THE HORSE RACE GAME
    def see_horse(self):
        self.movie.stop()
        self.frracing.hide()

    #THIS IS FOR THE PLAY AGAIN BUTTON OF THE HORSE RACE GAME
    def playagain_horse(self):
        global pwallet, randhorse, hlist
        global guesshorse
        #HIDING THE RESULT FRAME AND RESETING THE GAME AGAIN
        self.lblhorsewipic.hide(); self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horseicongreen.png"))
        guesshorse=""
        self.rbachilles.setAutoExclusive(False); self.rbachilles.setChecked(False); self.rbachilles.setAutoExclusive(True)
        self.rbbullseye.setAutoExclusive(False); self.rbbullseye.setChecked(False); self.rbbullseye.setAutoExclusive(True)
        self.rbgulliver.setAutoExclusive(False); self.rbgulliver.setChecked(False); self.rbgulliver.setAutoExclusive(True)
        self.rbmaximus.setAutoExclusive(False); self.rbmaximus.setChecked(False); self.rbmaximus.setAutoExclusive(True)
        self.rbpetra.setAutoExclusive(False); self.rbpetra.setChecked(False); self.rbpetra.setAutoExclusive(True)
        self.rbrambo.setAutoExclusive(False); self.rbrambo.setChecked(False); self.rbrambo.setAutoExclusive(True)
        wallet=int(pwallet)
        #CHECKING IF THE USER HAS ENOUGH MONEY TO PLAY THE GAME
        if wallet < 10:
            self.open_sorry()
            self.pbexithorse.setEnabled(True); self.pbpagainhorse.setEnabled(False)
        elif wallet > 9:
            wallet = wallet - 10
            self.frhorseselection.setEnabled(True); self.frwinresulthorse.hide()
            self.pbenterhorse.setEnabled(False); self.pbexithorse.setEnabled(False); self.pbpagainhorse.setEnabled(False)
            self.lcdwallethorse.display(wallet)
        hlist = ["Achilles", "Bullseye", "Gulliver", "Maximus", "Petra", "Rambo"]
        randhorse = random.choice(hlist)
        self.secret.setText(randhorse)
        pwallet=str(wallet)
        return pwallet, randhorse, guesshorse

    # THIS FUNCTION IS FOR THE ENTER BUTTON OF THE HORSE RACE GAME
    def horseenter_action(self):
        global guesshorse
        global pwallet
        wallet=int(pwallet)
        self.frhorseselection.setEnabled(False)
        self.lblnamehorsewin.setText(randhorse)

        self.frracing.show(); self.movie.start()
        #A PICTURE OF THE HORSE WILL SHOW ONCE ITS NAME IS CLICKED
        if randhorse == "Achilles":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse1.png"))
        elif randhorse == "Bullseye":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse2.png"))
        elif randhorse == "Gulliver":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse3.png"))
        elif randhorse == "Maximus":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse4.png"))
        elif randhorse == "Petra":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse6.png"))
        elif randhorse == "Rambo":
            self.lblhorsewipic.setPixmap(QtGui.QPixmap("horse5.png"))

        self.frwinresulthorse.show(); self.lblhorsewipic.show()

        if guesshorse == randhorse:
            self.lblwinorlose_2.setText("YOU WON")
            wallet=wallet+100
            self.lcdwallethorse.display(wallet)
        elif guesshorse != randhorse:
            self.lblwinorlose_2.setText("YOU LOSE :(")

        self.pbpagainhorse.setEnabled(True); self.pbexithorse.setEnabled(True)
        pwallet=str(wallet)
        return pwallet

    #THE FUNCTION IF HORSE NAMED ACHILLES IS CLICKED
    def horse1_clicked(self):
        global guesshorse
        guesshorse = "Achilles"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse1.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THE FUNCTION IF HORSE NAMED BULLSEYE IS CLICKED
    def horse2_clicked(self):
        global guesshorse
        guesshorse = "Bullseye"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse2.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THE FUNCTION IF HORSE NAMED GULLIVER IS CLICKED
    def horse3_clicked(self):
        global guesshorse
        guesshorse = "Gulliver"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse3.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THE FUNCTION IF HORSE NAMED MAXIMUS IS CLICKED
    def horse4_clicked(self):
        global guesshorse
        guesshorse = "Maximus"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse4.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THE FUNCTION IF HORSE NAMED PETRA IS CLICKED
    def horse5_clicked(self):
        global guesshorse
        guesshorse = "Petra"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse6.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THE FUNCTION IF HORSE NAMED RAMBO IS CLICKED
    def horse6_clicked(self):
        global guesshorse
        guesshorse = "Rambo"
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horse5.png"))
        self.pbenterhorse.setEnabled(True)
        return guesshorse

    # THIS IS THE FUNCTION FOR OPENING THE HORSE RACE GAME MODE PUSH BUTTON
    def open_horse(self):
        global pwallet, hjackpot
        global hlist, randhorse
        wallet=int(pwallet)
        wallet-=10

        if wallet < 10:
            self.open_sorry()
        elif wallet > 9:
            wallet -= 10
            self.open_deduct()
            self.rbachilles.setAutoExclusive(False); self.rbachilles.setChecked(False); self.rbachilles.setAutoExclusive(True)
            self.rbbullseye.setAutoExclusive(False); self.rbbullseye.setChecked(False); self.rbbullseye.setAutoExclusive(True)
            self.rbgulliver.setAutoExclusive(False); self.rbgulliver.setChecked(False); self.rbgulliver.setAutoExclusive(True)
            self.rbmaximus.setAutoExclusive(False); self.rbmaximus.setChecked(False); self.rbmaximus.setAutoExclusive(True)
            self.rbpetra.setAutoExclusive(False); self.rbpetra.setChecked(False); self.rbpetra.setAutoExclusive(True)
            self.rbrambo.setAutoExclusive(False); self.rbrambo.setChecked(False); self.rbrambo.setAutoExclusive(True)

            self.frhorseselection.setEnabled(True); self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horseicongreen.png"))

            self.hwidget.show(); self.wultra.hide(); self.wsuperlottery.hide(); self.wphwar.hide()
            self.frracing.hide(); self.pbpagainhorse.setEnabled(False); self.pbexithorse.setEnabled(False); self.pbenterhorse.setEnabled(False); self.frwinresulthorse.hide(); self.lblhorsewipic.hide()
            self.lcdprizehorse.display(hjackpot); self.lcdwallethorse.display(wallet)
            self.secret.setText(randhorse)
            pwallet=str(wallet)
        return pwallet, randhorse

    # THIS IS FOR THE EXIT BUTTON OF THE ULTRA LOTTERY GAME
    def ultraexit(self):
        global sguessnum, srands, pwallet
        sguessnum.clear(); srands.clear()
        self.wultra.hide()
        self.lblwallet.setText(pwallet)

    # THE PLAY AGAIN BUTTON FOR THE ULTRA LOTTERY GAME
    def ultraplay_again(self):
        global sguessnum
        global pwallet, srands
        global srand1, srand2, srand3
        wallet=int(pwallet)

        sguessnum.clear()
        srands.clear()
        srand1 = random.randint(1, 10)
        srands.append(srand1)
        srand2 = random.randint(1, 10)
        while srand2 in srands:
            srand2=random.randint(1,10)
            if srand2 not in srands:
                break
        srands.append(srand2)
        srand3 = random.randint(1, 10)
        while srand3 in srands:
            srand3 = random.randint(1, 10)
            if srand3 not in srands:
                break
        srands.append(srand3)
        srands.sort()
        self.label_11.setText(str(srands))
        #WILL CHECK FIRST IF PLAYER HAS ENOUGH MONEY TO PLAY
        if wallet < 10:
            self.lblotresult_2.setText("NO MORE MONEY :("); self.lblotresult_2.setStyleSheet("background-color: red")
            self.PBUEXIT.setEnabled(True); self.PBUPAGAIN.setEnabled(False)
        elif wallet > 9:
            self.PBU1.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU2.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU3.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU4.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU5.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU6.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU7.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU8.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU9.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU10.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU11.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU12.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU13.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU14.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU15.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU1.setEnabled(True); self.PBU2.setEnabled(True); self.PBU3.setEnabled(True); self.PBU4.setEnabled(True); self.PBU5.setEnabled(True); self.PBU6.setEnabled(True); self.PBU7.setEnabled(True); self.PBU8.setEnabled(True); self.PBU9.setEnabled(True); self.PBU10.setEnabled(True); self.PBU11.setEnabled(True); self.PBU12.setEnabled(True); self.PBU13.setEnabled(True); self.PBU14.setEnabled(True); self.PBU15.setEnabled(True)
            wallet-=10
            self.PBUPAGAIN.setEnabled(False)
            self.PBUEXIT.setEnabled(False)
            self.LCDWALLETULTRA.display(wallet)
        self.UBALL1.hide(); self.UBALL2.hide(); self.UBALL3.hide(); self.LCDURESULT1.hide(); self.LCDURESULT2.hide(); self.LCDURESULT3.hide(); self.LBLULTRAWINORLOSE_2.hide()

        self.LCDULTRAJACKPOT.display(ujackpot)
        pwallet=str(wallet)
        return sguessnum, pwallet, srands

    #THIS IS FOR THE "GO" BUTTON OF THE ULTRA LOTTERY GAME
    def ultrago_action(self):
        global pwallet, sguessnum
        global srands, ujackpot
        wallet=int(pwallet)
        sguessnum.sort()
        self.UBALL1.show(); self.UBALL2.show(); self.UBALL3.show(); self.LCDURESULT1.show(); self.LCDURESULT2.show(); self.LCDURESULT3.show()
        self.LCDURESULT1.display(srands[0])
        self.LCDURESULT2.display(srands[1])
        self.LCDURESULT3.display(srands[2])

        if sguessnum == srands:
            self.LBLULTRAWINORLOSE_2.show(); self.LBLULTRAWINORLOSE_2.setText("YOU WIN")
            wallet=wallet+100
            ujackpot=100
        elif sguessnum != srands:
            self.LBLULTRAWINORLOSE_2.show();
            self.LBLULTRAWINORLOSE_2.setText("YOU LOSE")
            ujackpot=ujackpot+10

        self.PBUGO.setEnabled(False)
        self.PBUPAGAIN.setEnabled(True), self.PBUEXIT.setEnabled(True)
        self.LCDWALLETULTRA.display(wallet); self.LCDULTRAJACKPOT.display(ujackpot)
        pwallet=str(wallet)
        return pwallet, ujackpot

    #THIS IS WHAT WILL HAPPEN IF NUMBER 1 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum1clicked(self):
        global sguessnum
        sguessnum.append(1)
        self.PBU1.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 2 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum2clicked(self):
        global sguessnum
        sguessnum.append(2)
        self.PBU2.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 3 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum3clicked(self):
        global sguessnum
        sguessnum.append(3)
        self.PBU3.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 4 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum4clicked(self):
        global sguessnum
        sguessnum.append(4)
        self.PBU4.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 5 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum5clicked(self):
        global sguessnum
        sguessnum.append(5)
        self.PBU5.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 6 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum6clicked(self):
        global sguessnum
        sguessnum.append(6)
        self.PBU6.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 7 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum7clicked(self):
        global sguessnum
        sguessnum.append(7)
        self.PBU7.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 8 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum8clicked(self):
        global sguessnum
        sguessnum.append(8)
        self.PBU8.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 9 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum9clicked(self):
        global sguessnum
        sguessnum.append(9)
        self.PBU9.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 10 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum10clicked(self):
        global sguessnum
        sguessnum.append(10)
        self.PBU10.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 11 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum11clicked(self):
        global sguessnum
        sguessnum.append(11)
        self.PBU11.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 12 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum12clicked(self):
        global sguessnum
        sguessnum.append(12)
        self.PBU12.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 13 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum13clicked(self):
        global sguessnum
        sguessnum.append(13)
        self.PBU13.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 14 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum14clicked(self):
        global sguessnum
        sguessnum.append(14)
        self.PBU14.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 15 PUSH BUTTON IS CLICKED IN THE ULTRA LOTTERY GAME
    def unum15clicked(self):
        global sguessnum
        sguessnum.append(15)
        self.PBU15.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 3:
            self.PBU1.setEnabled(False); self.PBU2.setEnabled(False); self.PBU3.setEnabled(False); self.PBU4.setEnabled(False); self.PBU5.setEnabled(False); self.PBU6.setEnabled(False); self.PBU7.setEnabled(False); self.PBU8.setEnabled(False); self.PBU9.setEnabled(False); self.PBU10.setEnabled(False)
            self.PBU11.setEnabled(False); self.PBU12.setEnabled(False); self.PBU13.setEnabled(False); self.PBU14.setEnabled(False); self.PBU15.setEnabled(False);
            self.PBUGO.setEnabled(True)
        return sguessnum

    # THIS IS THE ACTION FOR THE PUSH BUTTON FOR OPENING THE ULTRA LOTTERY GAME MODE
    def open_ultra(self):
        global pwallet, ujackpot
        global srands, srand1, srand2, srand3
        wallet=int(pwallet)
        wallet-=10

        if wallet < 10:
            self.open_sorry()
        elif wallet > 9:
            wallet -= 10
            self.open_deduct()
            #RETURNED ALL THE BUTTONS TO THEIR ORIGINAL STATE
            self.PBU1.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU2.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU3.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU4.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU5.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU6.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU7.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU8.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU9.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU10.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU11.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU12.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU13.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU14.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBU15.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBU1.setEnabled(True); self.PBU2.setEnabled(True); self.PBU3.setEnabled(True); self.PBU4.setEnabled(True); self.PBU5.setEnabled(True)
            self.PBU6.setEnabled(True); self.PBU7.setEnabled(True); self.PBU8.setEnabled(True); self.PBU9.setEnabled(True); self.PBU10.setEnabled(True)
            self.PBU11.setEnabled(True); self.PBU12.setEnabled(True); self.PBU13.setEnabled(True); self.PBU14.setEnabled(True); self.PBU15.setEnabled(True)

            self.wultra.show(); self.wsuperlottery.hide(); self.hwidget.hide(); self.wphwar.hide()
            self.LCDWALLETULTRA.display(wallet); self.LCDULTRAJACKPOT.display(ujackpot)
            self.PBUGO.setEnabled(False); self.UBALL1.hide(); self.UBALL2.hide(); self.UBALL3.hide(); self.LCDURESULT1.hide(); self.LCDURESULT2.hide(); self.LCDURESULT3.hide()
            self.LBLULTRAWINORLOSE_2.hide(); self.PBUPAGAIN.setEnabled(False); self.PBUEXIT.setEnabled(False)
            #GENERATING RANDOM NUMBERS
            srand1 = random.randint(1, 10)
            srands.append(srand1)
            srand2 = random.randint(1, 10)
            while srand2 in srands:
                srand2 = random.randint(1, 10)
                if srand2 not in srands:
                    break
            srands.append(srand2)
            srand3 = random.randint(1, 10)
            while srand3 in srands:
                srand3 = random.randint(1, 10)
                if srand3 not in srands:
                    break
            srands.append(srand3)
            srands.sort()
            self.label_11.setText(str(srands))
            pwallet=str(wallet)
        return srands, srand1, srand2, srand3, pwallet

    # THIS IS THE EXIT BUTTON FOR THE SUPER LOTTERY GAME
    def superexit(self):
        global sguessnum, srands, pwallet
        sguessnum.clear(); srands.clear()
        self.wsuperlottery.hide()
        self.lblwallet.setText(pwallet)

    # THIS IS THE PLAY AGAIN BUTTON FOR THE SUPPER LOTTERY GAME
    def superplay_again(self):
        global sguessnum
        global pwallet
        global srands, srand1, srand2
        wallet=int(pwallet)

        sguessnum.clear()
        srands.clear()
        srand1 = random.randint(1, 10)
        srands.append(srand1)
        srand2 = random.randint(1, 10)
        while srand2 in srands:
            srand2=random.randint(1,10)
            if srand2 not in srands:
                break
        srands.append(srand2)
        srands.sort()
        self.secretsuper.setText(str(srands))

        if wallet < 10:
            self.lblotresult.setText("NO MORE MONEY :("); self.lblotresult.setStyleSheet("background-color: red")
            self.PBSEXIT.setEnabled(True); self.PBSPAGAIN.setEnabled(False)
        elif wallet > 9:
            self.PBS1.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS2.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS3.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS4.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS5.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBS6.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS7.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS8.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS9.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS10.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBS1.setEnabled(True); self.PBS2.setEnabled(True); self.PBS3.setEnabled(True); self.PBS4.setEnabled(True); self.PBS5.setEnabled(True); self.PBS6.setEnabled(True); self.PBS7.setEnabled(True); self.PBS8.setEnabled(True); self.PBS9.setEnabled(True); self.PBS10.setEnabled(True);
            wallet-=10
            self.PBSPAGAIN.setEnabled(False)
            self.PBSEXIT.setEnabled(False)
            self.lcdwalletsuper.display(wallet)
        self.SBALL1.hide(); self.SBALL2.hide(); self.LCDSRES2super.hide(); self.LCDSRES1super.hide(); self.LBLSUPERWINORLOSE.hide()

        self.lcdjackpotsuper.display(sjackpot)

        pwallet=str(wallet)
        return sguessnum, pwallet, srands

    # THIS IS WHAT WILL HAPPEN WHEN THE "GO" BUTTON ON THE SUPPER LOTTERY GAME WAS CLICKED
    def supergo_action(self):
        global pwallet
        global sguessnum
        global srands
        global sjackpot
        wallet=int(pwallet)
        sguessnum.sort()
        self.SBALL1.show(); self.SBALL2.show(); self.LCDSRES1super.show(); self.LCDSRES2super.show()
        self.LCDSRES1super.display(srands[0])
        self.LCDSRES2super.display(srands[1])

        if sguessnum == srands:
            self.LBLSUPERWINORLOSE.show(); self.LBLSUPERWINORLOSE.setText("YOU WIN")
            wallet=wallet+100
            sjackpot=100

            self.lcdwalletsuper.show()
        elif sguessnum != srands:
            self.LBLSUPERWINORLOSE.show();
            self.LBLSUPERWINORLOSE.setText("YOU LOSE")
            sjackpot=sjackpot+10

        self.PBSGO.setEnabled(False)
        self.PBSPAGAIN.setEnabled(True); self.PBSEXIT.setEnabled(True)
        pwallet=str(wallet)
        self.lcdwalletsuper.display(int(pwallet)), self.lcdjackpotsuper.display(sjackpot)
        return pwallet, sjackpot

    # THIS IS WHAT WILL HAPPEN IF NUMBER 1 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num1clicked(self):
        global sguessnum
        sguessnum.append(1)
        self.PBS1.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 2 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num2clicked(self):
        global sguessnum
        sguessnum.append(2)
        self.PBS2.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS2.setEnabled(False); self.PBS1.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 3 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num3clicked(self):
        global sguessnum
        sguessnum.append(3)
        self.PBS3.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS3.setEnabled(False); self.PBS2.setEnabled(False); self.PBS1.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 4 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num4clicked(self):
        global sguessnum
        sguessnum.append(4)
        self.PBS4.setStyleSheet("background-color: gray; border-radius: 10px;")
        var=len(sguessnum)
        if var == 2:
            self.PBS4.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS1.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 5 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num5clicked(self):
        global sguessnum
        sguessnum.append(5)
        self.PBS5.setStyleSheet("background-color: gray; border-radius: 10px;")
        var=len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 6 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num6clicked(self):
        global sguessnum
        sguessnum.append(6)
        self.PBS6.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 7 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num7clicked(self):
        global sguessnum
        sguessnum.append(7)
        self.PBS7.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 8 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num8clicked(self):
        global sguessnum
        sguessnum.append(8)
        self.PBS8.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 9 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num9clicked(self):
        global sguessnum
        sguessnum.append(9)
        self.PBS9.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS WHAT WILL HAPPEN IF NUMBER 10 PUSH BUTTON IS CLICKED IN THE SUPER LOTTERY GAME
    def num10clicked(self):
        global sguessnum
        sguessnum.append(10)
        self.PBS10.setStyleSheet("background-color: gray; border-radius: 10px;")
        var = len(sguessnum)
        if var == 2:
            self.PBS1.setEnabled(False); self.PBS2.setEnabled(False); self.PBS3.setEnabled(False); self.PBS4.setEnabled(False); self.PBS5.setEnabled(False); self.PBS6.setEnabled(False); self.PBS7.setEnabled(False); self.PBS8.setEnabled(False); self.PBS9.setEnabled(False); self.PBS10.setEnabled(False)
            self.PBSGO.setEnabled(True)
        return sguessnum

    # THIS IS THE FUNCTION FOR OPENING THE SUPER LOTTERY GAME BUTTON
    def open_super(self):
        global pwallet, sjackpot
        global srands, srand1, srand2
        wallet=int(pwallet)

        if wallet < 10:
            self.open_sorry()
        elif wallet > 9:
            wallet -= 10
            self.open_deduct()

            self.PBS1.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS2.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS3.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS4.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS5.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBS6.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS7.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS8.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS9.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)"); self.PBS10.setStyleSheet("border-radius: 10px; background-color: rgb(0, 211, 0)")
            self.PBS1.setEnabled(True); self.PBS2.setEnabled(True); self.PBS3.setEnabled(True); self.PBS4.setEnabled(True); self.PBS5.setEnabled(True);
            self.PBS6.setEnabled(True); self.PBS7.setEnabled(True); self.PBS8.setEnabled(True); self.PBS9.setEnabled(True); self.PBS10.setEnabled(True);

            self.wsuperlottery.show(); self.wultra.hide(); self.hwidget.hide(); self.wphwar.hide()
            self.lcdwalletsuper.display(wallet); self.lcdjackpotsuper.display(sjackpot)
            self.PBSGO.setEnabled(False); self.SBALL1.hide(); self.SBALL2.hide(); self.LCDSRES1super.hide(); self.LCDSRES2super.hide()
            self.LBLSUPERWINORLOSE.hide(); self.PBSPAGAIN.setEnabled(False); self.PBSEXIT.setEnabled(False)

            srand1 = random.randint(1, 10)
            srands.append(srand1)
            srand2 = random.randint(1, 10)
            while srand2 in srands:
                srand2 = random.randint(1, 10)
                if srand2 not in srands:
                    break
            srands.append(srand2)
            srands.sort()
            self.secretsuper.setText(str(srands))
            pwallet=str(wallet)
        return srands, srand1, srand2, pwallet

    # THIS IS FOR THE SHOP BUTTON ON THE MAIN MENU
    def open_buy(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_Dialogbuy()
        self.ui.setupUi(self.window)
        self.window.show()

    # THIS IS DIALOG THAT WILL SHOW EVERYTIME USER OPENS A GAME
    def open_deduct(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_Dialogdeduct()
        self.ui.setupUi(self.window)
        self.window.show()

    # THIS THE DIALOG THAT WILL APPEAR IF LAYER DOESN'T HAVE ENOUGH MONEY TO PLAY THE GAME
    def open_sorry(self):
        self.window=QtWidgets.QDialog()
        self.ui = Ui_Dialogsorry()
        self.ui.setupUi(self.window)
        self.window.show()

    # THIS IS THE EXIT BUTTON OF THE MAIN MENU SCREEN
    def open_exit(self):
        global pwallet, toys
        self.lblerror.hide()
        user = self.lenameinput.text()
        with open(user+".txt", 'w') as file1:
            file1.write(pwallet)

        with open(user + "toy.txt", 'w') as file2:
            file2.writelines(toys)

        self.lblitem1.hide(); self.lblitem2.hide(); self.lblitem3.hide(); self.lblitem4.hide(); self.lblitem5.hide(); self.lblitem6.hide()
        self.wwelcome.show()
        self.lenameinput.setText("")

    # THIS IS THE EXIT BUTTON ON THE WELCOME SCREEN. CLICKING THIS WILL CLOSE THE GAME
    def exit_talaga(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialogexit()
        self.ui.setupUi(self.window)
        self.window.show()

    # THIS IS WHAT WILL HAPPEN IF PANDA FROM THE SHOP WAS CLICKED
    def panda_clicked(self):
        global toy
        toy="panda \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("panda.png"))
        return toy

    # THIS IS WHAT WILL HAPPEN IF PIG FROM THE SHOP WAS CLICKED
    def pig_clicked(self):
        global toy
        toy="pig \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("pig.png"))
        return toy

    # THIS IS WHAT WILL HAPPEN IF KOALA FROM THE SHOP WAS CLICKED
    def koala_clicked(self):
        global toy
        toy="koala \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("koala.png"))
        return toy

    # THIS IS WHAT WILL HAPPEN IF CAT FROM THE SHOP WAS CLICKED
    def cat_clicked(self):
        global toy
        toy="cat \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("cat.png"))
        return toy

    # THIS IS WHAT WILL HAPPEN IF DOG FROM THE SHOP WAS CLICKED
    def dog_clicked(self):
        global toy
        toy="dog \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("puppy.png"))
        return toy

    # THIS IS WHAT WILL HAPPEN IF BEAR FROM THE SHOP WAS CLICKED
    def bear_clicked(self):
        global toy
        toy="bear \n"
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("bear.png"))
        return toy

    # THIS IS FOR THE BUY BUTTON IN THE SHOP. WILL CHECK FIRST IF THE PLAYER ALREADY BOUGHT THE TOY
    def checktoy(self):
        global toy, toys

        if toy in toys:
            self.lblnomoney.show()
            self.lblnomoney.setText("YOU ALREADY HAVE THIS TOY")
        elif toy not in toys:
            self.buy_action()

    #THEN WILL PROCEED TO CHECK IF PLAYER HAVE ENOUGH MONEY TO BUY THE TOY. THE PLAYER ACQUIRES THE TOY IF HE/SHE HAVE ENOUGH MONEY.
    def buy_action(self):
        global toy
        global pwallet
        global toys
        wallet=int(pwallet)

        if toy == "panda \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 150:
                    self.lblitem1.show()
                    toys.append(toy)
                    wallet-=150
                    self.open_buy()
                elif wallet < 150:
                    self.open_sorry()
        elif toy == "pig \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 150:
                    self.lblitem2.show()
                    toys.append(toy)
                    wallet-=150
                    self.open_buy()
                elif wallet < 150:
                    self.open_sorry()
        elif toy == "koala \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 200:
                    self.lblitem3.show()
                    toys.append(toy)
                    wallet-=200
                    self.open_buy()
                elif wallet < 200:
                    self.open_sorry()
        elif toy == "cat \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 200:
                    self.lblitem4.show()
                    toys.append(toy)
                    wallet-=200
                    self.open_buy()
                elif wallet < 200:
                    self.open_sorry()
        elif toy == "dog \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 250:
                    self.lblitem5.show()
                    toys.append(toy)
                    wallet-=250
                    self.open_buy()
                elif wallet < 250:
                    self.open_sorry()
        elif toy == "bear \n":
            if toy in toys:
                self.lblnomoney.show()
                self.lblnomoney.setText("YOU ALREADY HAVE THIS")
            elif toy not in toys:
                if wallet >= 250:
                    self.lblitem6.show()
                    toys.append(toy)
                    wallet-=250
                    self.open_buy()
                elif wallet < 250:
                    self.open_sorry()

        if wallet < 150:
            self.pbshop_2.setEnabled(False)

        pwallet=str(wallet)
        self.lblwallet.setText(pwallet)
        return pwallet, toys

    # THIS IS WHAT WILL HAPPEN IF GO BACK BUTTON FROM THE SHOP IS CLICKED
    def goback_action(self):
        self.frshop.hide()
        self.lblnomoney.hide()

    # THIS IS THE FUNCTION FOR THE SHOP BUTTON
    def open_shop(self):
        global pwallet
        self.frshop.show()
        wallet=int(pwallet)

        if wallet < 150:
            self.frtoys.setEnabled(False)
            self.pbshop_2.setEnabled(False)
        else:
            self.pbshop_2.setEnabled(True)
            self.frtoys.setEnabled(True)

    # THIS IS THE LOG IN BUTTON
    def login_action(self):
        global pwallet, ptoy
        try:
            if self.lenameinput.text() == "":
                self.lblerror.show(); self.lblerror.setText("     Please write a user name!")
            else:
                self.lblerror.hide()
                user=self.lenameinput.text()
                self.lblplayer.setText(user)
                with open(user+'.txt', 'r') as fname:
                    wallet = fname.read()
                    pwallet=str(wallet)
                    self.lblwallet.setText(pwallet)
                with open(user+'toy.txt', 'r') as ftoy:
                    ptoy=ftoy.read()

                if "panda" in ptoy:
                    self.lblitem1.show()
                if "pig" in ptoy:
                    self.lblitem2.show()
                if "koala" in ptoy:
                    self.lblitem3.show()
                if "cat" in ptoy:
                    self.lblitem4.show()
                if "dog" in ptoy:
                    self.lblitem5.show()
                if "bear" in ptoy:
                    self.lblitem6.show()
                self.wwelcome.hide()
        except:
            self.lblerror.show(); self.lblerror.setText("Player with this user name does not exist")
        return pwallet, ptoy

    # THIS IS THE NEW USER BUTTON AT THE WELCOME SCREEN
    def newuser_action(self):
        import os.path
        from os import path
        global pwallet, toys
        user = self.lenameinput.text()
        if self.lenameinput.text() == "":
            self.lblerror.show(); self.lblerror.setText("              Invalid name!!!")
        elif path.exists(user+".txt") == True:
            self.lblerror.show();
            self.lblerror.setText("   This username exists. LOG IN instead.")
        else:
            self.lblerror.hide()

            self.lblplayer.setText(user)
            with open(user+".txt", 'w') as fname:
                fname.write(str(100))
            pwallet="100"

            with open(user+"toy.txt", 'w') as ftoy:
                ftoy.write("")
            self.lblwallet.setText(pwallet)
            toys.clear()
            self.wwelcome.hide()
        return pwallet, toys

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(896, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wmainmenu = QtWidgets.QWidget(self.centralwidget)
        self.wmainmenu.setGeometry(QtCore.QRect(0, 0, 901, 631))
        self.wmainmenu.setObjectName("wmainmenu")
        self.mbg = QtWidgets.QLabel(self.wmainmenu)
        self.mbg.setGeometry(QtCore.QRect(-40, -10, 971, 621))
        self.mbg.setMouseTracking(False)
        self.mbg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.mbg.setText("")
        self.mbg.setPixmap(QtGui.QPixmap("layout1.png"))
        self.mbg.setScaledContents(True)
        self.mbg.setObjectName("mbg")
        self.lblogo = QtWidgets.QLabel(self.wmainmenu)
        self.lblogo.setGeometry(QtCore.QRect(70, 90, 231, 71))
        self.lblogo.setText("")
        self.lblogo.setPixmap(QtGui.QPixmap("LOGOLG.png"))
        self.lblogo.setScaledContents(True)
        self.lblogo.setObjectName("lblogo")
        self.frnamewallet = QtWidgets.QFrame(self.wmainmenu)
        self.frnamewallet.setGeometry(QtCore.QRect(620, 83, 191, 87))
        self.frnamewallet.setStyleSheet("border: 1px solid green;\n"
"background-color: rgb(0, 0, 0);")
        self.frnamewallet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frnamewallet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frnamewallet.setObjectName("frnamewallet")
        self.lblwallet = QtWidgets.QLabel(self.frnamewallet)
        self.lblwallet.setGeometry(QtCore.QRect(50, 45, 131, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.lblwallet.setFont(font)
        self.lblwallet.setStyleSheet("color: rgb(0, 211, 0);\n"
"border-color: rgb(0, 211, 0);")
        self.lblwallet.setText("")
        self.lblwallet.setObjectName("lblwallet")

        self.lblplayer = QtWidgets.QLabel(self.frnamewallet)
        self.lblplayer.setGeometry(QtCore.QRect(50, 8, 131, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.lblplayer.setFont(font)
        self.lblplayer.setStyleSheet("color: rgb(0, 211, 0);\n"
                                     "border-color: rgb(0, 211, 0);")
        self.lblplayer.setText("")
        self.lblplayer.setObjectName("lblplayer")

        self.picwallet = QtWidgets.QLabel(self.frnamewallet)
        self.picwallet.setGeometry(QtCore.QRect(10, 45, 31, 31))
        self.picwallet.setStyleSheet("background-color: none;\n"
"border-color: none;")
        self.picwallet.setText("")
        self.picwallet.setPixmap(QtGui.QPixmap("walleticon.png"))
        self.picwallet.setScaledContents(True)
        self.picwallet.setObjectName("picwallet")

        self.picplayer = QtWidgets.QLabel(self.frnamewallet)
        self.picplayer.setGeometry(QtCore.QRect(8, 8, 33, 33))
        self.picplayer.setStyleSheet("background-color: none;\n"
                                     "border-color: none;")
        self.picplayer.setText("")
        self.picplayer.setPixmap(QtGui.QPixmap("playericon.png"))
        self.picplayer.setScaledContents(True)
        self.picplayer.setObjectName("picplayer")

        self.frgames = QtWidgets.QFrame(self.wmainmenu)
        self.frgames.setGeometry(QtCore.QRect(70, 190, 191, 321))
        self.frgames.setStyleSheet("border: 1px solid green;")
        self.frgames.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frgames.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frgames.setObjectName("frgames")
        self.pbsuperlottery = QtWidgets.QPushButton(self.frgames, clicked=lambda: self.open_super())
        self.pbsuperlottery.setGeometry(QtCore.QRect(20, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.pbsuperlottery.setFont(font)
        self.pbsuperlottery.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(143, 255, 39);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"    \n"
"}")
        self.pbsuperlottery.setObjectName("pbsuperlottery")
        self.pbhorserace = QtWidgets.QPushButton(self.frgames, clicked=lambda: self.open_horse())
        self.pbhorserace.setGeometry(QtCore.QRect(20, 170, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.pbhorserace.setFont(font)
        self.pbhorserace.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(143, 255, 39);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"    \n"
"}")
        self.pbhorserace.setObjectName("pbhorserace")
        self.pbphwar = QtWidgets.QPushButton(self.frgames, clicked=lambda: self.open_phwar())
        self.pbphwar.setGeometry(QtCore.QRect(20, 240, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.pbphwar.setFont(font)
        self.pbphwar.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(143, 255, 39);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"    \n"
"}")
        self.pbphwar.setObjectName("pbphwar")
        self.pbultralottery = QtWidgets.QPushButton(self.frgames, clicked=lambda: self.open_ultra())
        self.pbultralottery.setGeometry(QtCore.QRect(20, 100, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.pbultralottery.setFont(font)
        self.pbultralottery.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(143, 255, 39);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"    \n"
"}")
        self.pbultralottery.setObjectName("pbultralottery")
        self.lbgamemode = QtWidgets.QLabel(self.wmainmenu)
        self.lbgamemode.setGeometry(QtCore.QRect(90, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbgamemode.setFont(font)
        self.lbgamemode.setMouseTracking(True)
        self.lbgamemode.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbgamemode.setObjectName("lbgamemode")
        self.frbag = QtWidgets.QFrame(self.wmainmenu)
        self.frbag.setGeometry(QtCore.QRect(620, 190, 191, 261))
        self.frbag.setStyleSheet("border: 1px solid green;\n"
"background-color: rgb(0, 0, 0);")
        self.frbag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frbag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frbag.setObjectName("frbag")
        self.lbbag = QtWidgets.QLabel(self.frbag)
        self.lbbag.setGeometry(QtCore.QRect(70, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbbag.setFont(font)
        self.lbbag.setMouseTracking(True)
        self.lbbag.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbbag.setObjectName("lbbag")
        self.lblitem1 = QtWidgets.QLabel(self.frbag)
        self.lblitem1.setGeometry(QtCore.QRect(20, 50, 61, 51))
        self.lblitem1.setStyleSheet("border: 0px;")
        self.lblitem1.setText("")
        self.lblitem1.setPixmap(QtGui.QPixmap("panda.png"))
        self.lblitem1.setScaledContents(True)
        self.lblitem1.setObjectName("lblitem1")
        self.lblitem3 = QtWidgets.QLabel(self.frbag)
        self.lblitem3.setGeometry(QtCore.QRect(20, 110, 61, 61))
        self.lblitem3.setStyleSheet("border: 0px;")
        self.lblitem3.setText("")
        self.lblitem3.setPixmap(QtGui.QPixmap("koala.png"))
        self.lblitem3.setScaledContents(True)
        self.lblitem3.setObjectName("lblitem3")
        self.lblitem5 = QtWidgets.QLabel(self.frbag)
        self.lblitem5.setGeometry(QtCore.QRect(20, 180, 61, 61))
        self.lblitem5.setStyleSheet("border: 0px;")
        self.lblitem5.setText("")
        self.lblitem5.setPixmap(QtGui.QPixmap("puppy.png"))
        self.lblitem5.setScaledContents(True)
        self.lblitem5.setObjectName("lblitem5")
        self.lblitem2 = QtWidgets.QLabel(self.frbag)
        self.lblitem2.setGeometry(QtCore.QRect(110, 40, 61, 61))
        self.lblitem2.setStyleSheet("border: 0px;")
        self.lblitem2.setText("")
        self.lblitem2.setPixmap(QtGui.QPixmap("pig.png"))
        self.lblitem2.setScaledContents(True)
        self.lblitem2.setObjectName("lblitem2")
        self.lblitem4 = QtWidgets.QLabel(self.frbag)
        self.lblitem4.setGeometry(QtCore.QRect(110, 110, 61, 61))
        self.lblitem4.setStyleSheet("border: 0px;")
        self.lblitem4.setText("")
        self.lblitem4.setPixmap(QtGui.QPixmap("cat.png"))
        self.lblitem4.setScaledContents(True)
        self.lblitem4.setObjectName("lblitem4")
        self.lblitem6 = QtWidgets.QLabel(self.frbag)
        self.lblitem6.setGeometry(QtCore.QRect(110, 180, 61, 61))
        self.lblitem6.setStyleSheet("border: 0px;")
        self.lblitem6.setText("")
        self.lblitem6.setPixmap(QtGui.QPixmap("bear.png"))
        self.lblitem6.setScaledContents(True)
        self.lblitem6.setObjectName("lblitem6")
        self.pbshop = QtWidgets.QPushButton(self.wmainmenu, clicked=lambda: self.open_shop())
        self.pbshop.setGeometry(QtCore.QRect(620, 470, 91, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.pbshop.setFont(font)
        self.pbshop.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(255, 234, 3);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.pbshop.setObjectName("pbshop")
        self.pbexit = QtWidgets.QPushButton(self.wmainmenu, clicked=lambda: self.open_exit())
        self.pbexit.setGeometry(QtCore.QRect(730, 470, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.pbexit.setFont(font)
        self.pbexit.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.pbexit.setObjectName("pbexit")
        self.frshop = QtWidgets.QFrame(self.wmainmenu)
        self.frshop.setGeometry(QtCore.QRect(280, 190, 531, 321))
        self.frshop.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 1px solid green;\n"
"")
        self.frshop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frshop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frshop.setObjectName("frshop")
        self.lbshop = QtWidgets.QLabel(self.frshop)
        self.lbshop.setGeometry(QtCore.QRect(130, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbshop.setFont(font)
        self.lbshop.setMouseTracking(True)
        self.lbshop.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbshop.setObjectName("lbshop")
        self.lblselecttoypic = QtWidgets.QLabel(self.frshop)
        self.lblselecttoypic.setGeometry(QtCore.QRect(230, 40, 261, 251))
        self.lblselecttoypic.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.lblselecttoypic.setText("")
        self.lblselecttoypic.setPixmap(QtGui.QPixmap("black.png"))
        self.lblselecttoypic.setScaledContents(True)
        self.lblselecttoypic.setObjectName("lblselecttoypic")
        self.frtoys = QtWidgets.QFrame(self.frshop)
        self.frtoys.setGeometry(QtCore.QRect(20, 40, 171, 211))
        self.frtoys.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frtoys.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frtoys.setObjectName("frtoys")
        self.radioButton = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.panda_clicked())
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.pig_clicked())
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.koala_clicked())
        self.radioButton_3.setGeometry(QtCore.QRect(20, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.cat_clicked())
        self.radioButton_4.setGeometry(QtCore.QRect(20, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.dog_clicked())
        self.radioButton_5.setGeometry(QtCore.QRect(20, 130, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frtoys, clicked=lambda: self.bear_clicked())
        self.radioButton_6.setGeometry(QtCore.QRect(20, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 248, 32);")
        self.radioButton_6.setObjectName("radioButton_6")
        self.pbshop_2 = QtWidgets.QPushButton(self.frshop, clicked=lambda: self.checktoy())
        self.pbshop_2.setGeometry(QtCore.QRect(20, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pbshop_2.setFont(font)
        self.pbshop_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 158, 1);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(255, 85, 0);\n"
"    \n"
"}")
        self.pbshop_2.setObjectName("pbshop_2")
        self.pbshop_3 = QtWidgets.QPushButton(self.frshop, clicked=lambda: self.goback_action())
        self.pbshop_3.setGeometry(QtCore.QRect(110, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pbshop_3.setFont(font)
        self.pbshop_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(0, 254, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.pbshop_3.setObjectName("pbshop_3")
        self.lgpic = QtWidgets.QLabel(self.wmainmenu)
        self.lgpic.setGeometry(QtCore.QRect(280, 220, 311, 241))
        self.lgpic.setText("")
        self.lgpic.setPixmap(QtGui.QPixmap("LG1.png"))
        self.lgpic.setScaledContents(True)
        self.lgpic.setObjectName("lgpic")
        self.lblnomoney = QtWidgets.QLabel(self.wmainmenu)
        self.lblnomoney.setGeometry(QtCore.QRect(310, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setUnderline(False)
        self.lblnomoney.setFont(font)
        self.lblnomoney.setStyleSheet("color: rgb(200, 11, 4);\n"
"")
        self.lblnomoney.setObjectName("lblnomoney")
        self.mbg.raise_()
        self.lblogo.raise_()
        self.frnamewallet.raise_()
        self.frgames.raise_()
        self.lbgamemode.raise_()
        self.frbag.raise_()
        self.pbshop.raise_()
        self.pbexit.raise_()
        self.lgpic.raise_()
        self.frshop.raise_()
        self.lblnomoney.raise_()
        self.wphwar = QtWidgets.QWidget(self.centralwidget)
        self.wphwar.setGeometry(QtCore.QRect(0, 0, 901, 611))
        self.wphwar.setObjectName("wphwar")
        self.lbmainbg = QtWidgets.QLabel(self.wphwar)
        self.lbmainbg.setGeometry(QtCore.QRect(-160, -80, 1201, 701))
        self.lbmainbg.setMouseTracking(False)
        self.lbmainbg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.lbmainbg.setText("")
        self.lbmainbg.setPixmap(QtGui.QPixmap("shop.png"))
        self.lbmainbg.setScaledContents(True)
        self.lbmainbg.setObjectName("lbmainbg")
        self.lbiconwar = QtWidgets.QLabel(self.wphwar)
        self.lbiconwar.setGeometry(QtCore.QRect(80, 90, 101, 81))
        self.lbiconwar.setStyleSheet("")
        self.lbiconwar.setText("")
        self.lbiconwar.setPixmap(QtGui.QPixmap("swords.png"))
        self.lbiconwar.setScaledContents(True)
        self.lbiconwar.setObjectName("lbiconwar")
        self.lbinputhere_2 = QtWidgets.QLabel(self.wphwar)
        self.lbinputhere_2.setGeometry(QtCore.QRect(250, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbinputhere_2.setFont(font)
        self.lbinputhere_2.setMouseTracking(True)
        self.lbinputhere_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbinputhere_2.setObjectName("lbinputhere_2")
        self.lbinputhere_4 = QtWidgets.QLabel(self.wphwar)
        self.lbinputhere_4.setGeometry(QtCore.QRect(220, 140, 591, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbinputhere_4.setFont(font)
        self.lbinputhere_4.setMouseTracking(True)
        self.lbinputhere_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbinputhere_4.setObjectName("lbinputhere_4")
        self.lbinputhere_3 = QtWidgets.QLabel(self.wphwar)
        self.lbinputhere_3.setGeometry(QtCore.QRect(220, 110, 591, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbinputhere_3.setFont(font)
        self.lbinputhere_3.setMouseTracking(True)
        self.lbinputhere_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbinputhere_3.setObjectName("lbinputhere_3")
        self.frphgame = QtWidgets.QFrame(self.wphwar)
        self.frphgame.setGeometry(QtCore.QRect(80, 190, 521, 161))
        self.frphgame.setStyleSheet("border: 1px solid green;")
        self.frphgame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frphgame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frphgame.setObjectName("frphgame")
        self.lbinputhere = QtWidgets.QLabel(self.frphgame)
        self.lbinputhere.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbinputhere.setFont(font)
        self.lbinputhere.setMouseTracking(True)
        self.lbinputhere.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbinputhere.setObjectName("lbinputhere")
        self.pbfight = QtWidgets.QPushButton(self.frphgame, clicked=lambda: self.fight_action())
        self.pbfight.setGeometry(QtCore.QRect(330, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.pbfight.setFont(font)
        self.pbfight.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(143, 255, 39);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"    \n"
"}")
        self.pbfight.setObjectName("pbfight")
        self.lbfilleft = QtWidgets.QLabel(self.frphgame)
        self.lbfilleft.setGeometry(QtCore.QRect(20, 120, 301, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lbfilleft.setFont(font)
        self.lbfilleft.setMouseTracking(True)
        self.lbfilleft.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(200, 11, 4);")
        self.lbfilleft.setObjectName("lbfilleft")
        self.cbguess1ph = QtWidgets.QComboBox(self.frphgame)
        self.cbguess1ph.setGeometry(QtCore.QRect(20, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.cbguess1ph.setFont(font)
        self.cbguess1ph.setStyleSheet("color: rgb(0, 248, 32);\n"
"background-color: rgb(0, 0, 0);")
        self.cbguess1ph.setObjectName("cbguess1ph")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess1ph.addItem("")
        self.cbguess2ph = QtWidgets.QComboBox(self.frphgame)
        self.cbguess2ph.setGeometry(QtCore.QRect(120, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.cbguess2ph.setFont(font)
        self.cbguess2ph.setStyleSheet("color: rgb(0, 248, 32);\n"
"background-color: rgb(0, 0, 0);")
        self.cbguess2ph.setObjectName("cbguess2ph")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess2ph.addItem("")
        self.cbguess3ph = QtWidgets.QComboBox(self.frphgame)
        self.cbguess3ph.setGeometry(QtCore.QRect(230, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.cbguess3ph.setFont(font)
        self.cbguess3ph.setStyleSheet("color: rgb(0, 248, 32);\n"
"background-color: rgb(0, 0, 0);")
        self.cbguess3ph.setObjectName("cbguess3ph")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.cbguess3ph.addItem("")
        self.mnl = QtWidgets.QLabel(self.frphgame)
        self.mnl.setGeometry(QtCore.QRect(20, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.mnl.setFont(font)
        self.mnl.setMouseTracking(True)
        self.mnl.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: none;")
        self.mnl.setObjectName("mnl")
        self.cebu = QtWidgets.QLabel(self.frphgame)
        self.cebu.setGeometry(QtCore.QRect(120, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.cebu.setFont(font)
        self.cebu.setMouseTracking(True)
        self.cebu.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: none;")
        self.cebu.setObjectName("cebu")
        self.davao = QtWidgets.QLabel(self.frphgame)
        self.davao.setGeometry(QtCore.QRect(230, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.davao.setFont(font)
        self.davao.setMouseTracking(True)
        self.davao.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: none;")
        self.davao.setObjectName("davao")
        self.cbguess3ph.raise_()
        self.lbfilleft.raise_()
        self.lbinputhere.raise_()
        self.pbfight.raise_()
        self.cbguess2ph.raise_()
        self.davao.raise_()
        self.mnl.raise_()
        self.cebu.raise_()
        self.cbguess1ph.raise_()
        self.frwalletph = QtWidgets.QFrame(self.wphwar)
        self.frwalletph.setGeometry(QtCore.QRect(630, 190, 171, 161))
        self.frwalletph.setStyleSheet("border: 1px solid green;")
        self.frwalletph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frwalletph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frwalletph.setObjectName("frwalletph")
        self.lbprizeph = QtWidgets.QLabel(self.frwalletph)
        self.lbprizeph.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbprizeph.setFont(font)
        self.lbprizeph.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbprizeph.setObjectName("lbprizeph")
        self.lcdwalletph = QtWidgets.QLCDNumber(self.frwalletph)
        self.lcdwalletph.setGeometry(QtCore.QRect(10, 70, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdwalletph.setFont(font)
        self.lcdwalletph.setObjectName("lcdwalletph")
        self.frresult = QtWidgets.QFrame(self.wphwar)
        self.frresult.setGeometry(QtCore.QRect(80, 360, 371, 121))
        self.frresult.setStyleSheet("border: 1px solid green;")
        self.frresult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frresult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frresult.setObjectName("frresult")
        self.lblnumofspaniards = QtWidgets.QLabel(self.frresult)
        self.lblnumofspaniards.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblnumofspaniards.setFont(font)
        self.lblnumofspaniards.setMouseTracking(True)
        self.lblnumofspaniards.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 211, 0);\n"
"color: rgb(35, 234, 13);")
        self.lblnumofspaniards.setText("")
        self.lblnumofspaniards.setObjectName("lblnumofspaniards")
        self.lblwherespaniadsland = QtWidgets.QLabel(self.frresult)
        self.lblwherespaniadsland.setGeometry(QtCore.QRect(20, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblwherespaniadsland.setFont(font)
        self.lblwherespaniadsland.setMouseTracking(True)
        self.lblwherespaniadsland.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 211, 0);\n"
"color: rgb(35, 234, 13);")
        self.lblwherespaniadsland.setText("")
        self.lblwherespaniadsland.setObjectName("lblwherespaniadsland")
        self.lbllandedat = QtWidgets.QLabel(self.frresult)
        self.lbllandedat.setGeometry(QtCore.QRect(120, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbllandedat.setFont(font)
        self.lbllandedat.setMouseTracking(True)
        self.lbllandedat.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbllandedat.setObjectName("lbllandedat")
        self.lblwinorlose = QtWidgets.QLabel(self.frresult)
        self.lblwinorlose.setGeometry(QtCore.QRect(130, 60, 221, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblwinorlose.setFont(font)
        self.lblwinorlose.setMouseTracking(True)
        self.lblwinorlose.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 211, 0);\n"
"color: rgb(35, 234, 13);")
        self.lblwinorlose.setText("")
        self.lblwinorlose.setObjectName("lblwinorlose")
        self.frprice = QtWidgets.QFrame(self.wphwar)
        self.frprice.setGeometry(QtCore.QRect(460, 360, 141, 121))
        self.frprice.setStyleSheet("border: 1px solid green;")
        self.frprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frprice.setObjectName("frprice")
        self.lbpriceph = QtWidgets.QLabel(self.frprice)
        self.lbpriceph.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbpriceph.setFont(font)
        self.lbpriceph.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbpriceph.setObjectName("lbpriceph")
        self.lcdprizeph = QtWidgets.QLCDNumber(self.frprice)
        self.lcdprizeph.setGeometry(QtCore.QRect(10, 50, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdprizeph.setFont(font)
        self.lcdprizeph.setObjectName("lcdprizeph")
        self.pbplayagainph = QtWidgets.QPushButton(self.wphwar, clicked=lambda: self.play_againph())
        self.pbplayagainph.setGeometry(QtCore.QRect(630, 370, 171, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pbplayagainph.setFont(font)
        self.pbplayagainph.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(255, 236, 20);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.pbplayagainph.setObjectName("pbplayagainph")
        self.pbexitph = QtWidgets.QPushButton(self.wphwar, clicked=lambda: self.exitph())
        self.pbexitph.setGeometry(QtCore.QRect(630, 430, 171, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.pbexitph.setFont(font)
        self.pbexitph.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.pbexitph.setObjectName("pbexitph")
        self.secretplaceph = QtWidgets.QLabel(self.wphwar)
        self.secretplaceph.setGeometry(QtCore.QRect(740, 530, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.secretplaceph.setFont(font)
        self.secretplaceph.setMouseTracking(True)
        self.secretplaceph.setStyleSheet("color: rgb(109, 109, 109);\n"
"border-color: none;")
        self.secretplaceph.setObjectName("secretplaceph")
        self.secretnumph = QtWidgets.QLabel(self.wphwar)
        self.secretnumph.setGeometry(QtCore.QRect(740, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.secretnumph.setFont(font)
        self.secretnumph.setMouseTracking(True)
        self.secretnumph.setStyleSheet("color: rgb(109, 109, 109);\n"
"border-color: none;")
        self.secretnumph.setObjectName("secretnumph")
        self.hwidget = QtWidgets.QWidget(self.centralwidget)
        self.hwidget.setGeometry(QtCore.QRect(0, 0, 901, 611))
        self.hwidget.setObjectName("hwidget")
        self.lbmainbg_2 = QtWidgets.QLabel(self.hwidget)
        self.lbmainbg_2.setGeometry(QtCore.QRect(-100, -30, 1091, 681))
        self.lbmainbg_2.setMouseTracking(False)
        self.lbmainbg_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.lbmainbg_2.setText("")
        self.lbmainbg_2.setPixmap(QtGui.QPixmap("shop.png"))
        self.lbmainbg_2.setScaledContents(True)
        self.lbmainbg_2.setObjectName("lbmainbg_2")
        self.label = QtWidgets.QLabel(self.hwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 248, 32);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.hwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 181, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.hwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 491, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_3.setObjectName("label_3")
        self.frprizehorse = QtWidgets.QFrame(self.hwidget)
        self.frprizehorse.setGeometry(QtCore.QRect(110, 140, 201, 51))
        self.frprizehorse.setStyleSheet("border: 1px solid green;")
        self.frprizehorse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frprizehorse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frprizehorse.setObjectName("frprizehorse")
        self.lbprice = QtWidgets.QLabel(self.frprizehorse)
        self.lbprice.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbprice.setFont(font)
        self.lbprice.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbprice.setObjectName("lbprice")
        self.lcdprizehorse = QtWidgets.QLCDNumber(self.frprizehorse)
        self.lcdprizehorse.setGeometry(QtCore.QRect(110, 10, 81, 31))
        self.lcdprizehorse.setObjectName("lcdprizehorse")
        self.frhorsewallet = QtWidgets.QFrame(self.hwidget)
        self.frhorsewallet.setGeometry(QtCore.QRect(320, 140, 211, 51))
        self.frhorsewallet.setStyleSheet("border: 1px solid green;")
        self.frhorsewallet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frhorsewallet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frhorsewallet.setObjectName("frhorsewallet")
        self.lbjackpot_3 = QtWidgets.QLabel(self.frhorsewallet)
        self.lbjackpot_3.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbjackpot_3.setFont(font)
        self.lbjackpot_3.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbjackpot_3.setObjectName("lbjackpot_3")
        self.lcdwallethorse = QtWidgets.QLCDNumber(self.frhorsewallet)
        self.lcdwallethorse.setGeometry(QtCore.QRect(120, 10, 81, 31))
        self.lcdwallethorse.setObjectName("lcdwallethorse")
        self.pbpagainhorse = QtWidgets.QPushButton(self.hwidget, clicked=lambda: self.playagain_horse())
        self.pbpagainhorse.setGeometry(QtCore.QRect(560, 140, 111, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pbpagainhorse.setFont(font)
        self.pbpagainhorse.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(243, 255, 5);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.pbpagainhorse.setObjectName("pbpagainhorse")
        self.pbexithorse = QtWidgets.QPushButton(self.hwidget, clicked=lambda: self.horseexit())
        self.pbexithorse.setGeometry(QtCore.QRect(680, 140, 111, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pbexithorse.setFont(font)
        self.pbexithorse.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.pbexithorse.setObjectName("pbexithorse")
        self.frhorseselection = QtWidgets.QFrame(self.hwidget)
        self.frhorseselection.setGeometry(QtCore.QRect(280, 210, 511, 131))
        self.frhorseselection.setStyleSheet("border: 1px solid green;")
        self.frhorseselection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frhorseselection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frhorseselection.setObjectName("frhorseselection")
        self.rbachilles = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse1_clicked())
        self.rbachilles.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbachilles.setFont(font)
        self.rbachilles.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbachilles.setObjectName("rbachilles")
        self.rbbullseye = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse2_clicked())
        self.rbbullseye.setGeometry(QtCore.QRect(30, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbbullseye.setFont(font)
        self.rbbullseye.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbbullseye.setObjectName("rbbullseye")
        self.rbgulliver = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse3_clicked())
        self.rbgulliver.setGeometry(QtCore.QRect(30, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbgulliver.setFont(font)
        self.rbgulliver.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbgulliver.setObjectName("rbgulliver")
        self.rbmaximus = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse4_clicked())
        self.rbmaximus.setGeometry(QtCore.QRect(200, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbmaximus.setFont(font)
        self.rbmaximus.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbmaximus.setObjectName("rbmaximus")
        self.rbpetra = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse5_clicked())
        self.rbpetra.setGeometry(QtCore.QRect(200, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbpetra.setFont(font)
        self.rbpetra.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbpetra.setObjectName("rbpetra")
        self.rbrambo = QtWidgets.QRadioButton(self.frhorseselection, clicked=lambda: self.horse6_clicked())
        self.rbrambo.setGeometry(QtCore.QRect(200, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.rbrambo.setFont(font)
        self.rbrambo.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 0, 0);")
        self.rbrambo.setObjectName("rbrambo")
        self.pbenterhorse = QtWidgets.QPushButton(self.frhorseselection, clicked=lambda: self.horseenter_action())
        self.pbenterhorse.setGeometry(QtCore.QRect(380, 40, 101, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.pbenterhorse.setFont(font)
        self.pbenterhorse.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(115, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(0, 211, 0);\n"
"}")
        self.pbenterhorse.setObjectName("pbenterhorse")
        self.lblselecthorsepic = QtWidgets.QLabel(self.hwidget)
        self.lblselecthorsepic.setGeometry(QtCore.QRect(120, 210, 141, 131))
        self.lblselecthorsepic.setStyleSheet("")
        self.lblselecthorsepic.setText("")
        self.lblselecthorsepic.setPixmap(QtGui.QPixmap("horseicongreen.png"))
        self.lblselecthorsepic.setScaledContents(True)
        self.lblselecthorsepic.setObjectName("lblselecthorsepic")
        self.frwinresulthorse = QtWidgets.QFrame(self.hwidget)
        self.frwinresulthorse.setGeometry(QtCore.QRect(120, 370, 501, 131))
        self.frwinresulthorse.setStyleSheet("border: 1px solid green;")
        self.frwinresulthorse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frwinresulthorse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frwinresulthorse.setObjectName("frwinresulthorse")
        self.lblnamehorsewin = QtWidgets.QLabel(self.frwinresulthorse)
        self.lblnamehorsewin.setGeometry(QtCore.QRect(280, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lblnamehorsewin.setFont(font)
        self.lblnamehorsewin.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lblnamehorsewin.setText("")
        self.lblnamehorsewin.setObjectName("lblnamehorsewin")
        self.lblwontherace = QtWidgets.QLabel(self.frwinresulthorse)
        self.lblwontherace.setGeometry(QtCore.QRect(280, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lblwontherace.setFont(font)
        self.lblwontherace.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lblwontherace.setObjectName("lblwontherace")
        self.lblwinorlose_2 = QtWidgets.QLabel(self.frwinresulthorse)
        self.lblwinorlose_2.setGeometry(QtCore.QRect(20, 20, 241, 91))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(26)
        self.lblwinorlose_2.setFont(font)
        self.lblwinorlose_2.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lblwinorlose_2.setText("")
        self.lblwinorlose_2.setObjectName("lblwinorlose_2")
        self.lblhorsewipic = QtWidgets.QLabel(self.hwidget)
        self.lblhorsewipic.setGeometry(QtCore.QRect(640, 370, 141, 131))
        self.lblhorsewipic.setStyleSheet("")
        self.lblhorsewipic.setText("")
        self.lblhorsewipic.setPixmap(QtGui.QPixmap("horseicongreen.png"))
        self.lblhorsewipic.setScaledContents(True)
        self.lblhorsewipic.setObjectName("lblhorsewipic")
        self.secret = QtWidgets.QLabel(self.hwidget)
        self.secret.setGeometry(QtCore.QRect(820, 530, 131, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        self.secret.setFont(font)
        self.secret.setStyleSheet("color: rgb(111, 111, 111);")
        self.secret.setObjectName("secret")
        self.frracing = QtWidgets.QFrame(self.hwidget)
        self.frracing.setGeometry(QtCore.QRect(70, 80, 761, 481))
        self.frracing.setStyleSheet("background-color: rgb(2, 2, 2);")
        self.frracing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frracing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frracing.setObjectName("frracing")
        self.takbuhan = QtWidgets.QLabel(self.frracing)
        self.takbuhan.setGeometry(QtCore.QRect(160, 30, 441, 341))
        self.takbuhan.setText("")
        self.takbuhan.setObjectName("takbuhan")
        self.pbseeresultshorse = QtWidgets.QPushButton(self.frracing, clicked=lambda: self.see_horse())
        self.pbseeresultshorse.setGeometry(QtCore.QRect(310, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pbseeresultshorse.setFont(font)
        self.pbseeresultshorse.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(115, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(0, 211, 0);\n"
"}")
        self.pbseeresultshorse.setObjectName("pbseeresultshorse")
        self.wsuperlottery = QtWidgets.QWidget(self.centralwidget)
        self.wsuperlottery.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.wsuperlottery.setObjectName("wsuperlottery")
        self.LBLSBG = QtWidgets.QLabel(self.wsuperlottery)
        self.LBLSBG.setGeometry(QtCore.QRect(-120, -30, 1131, 701))
        self.LBLSBG.setMouseTracking(False)
        self.LBLSBG.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.LBLSBG.setText("")
        self.LBLSBG.setPixmap(QtGui.QPixmap("shop.png"))
        self.LBLSBG.setScaledContents(True)
        self.LBLSBG.setObjectName("LBLSBG")
        self.label_4 = QtWidgets.QLabel(self.wsuperlottery)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 591, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.wsuperlottery)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 541, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.wsuperlottery)
        self.label_6.setGeometry(QtCore.QRect(220, 10, 541, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_6.setObjectName("label_6")
        self.lbicon = QtWidgets.QLabel(self.wsuperlottery)
        self.lbicon.setGeometry(QtCore.QRect(100, 20, 71, 61))
        self.lbicon.setStyleSheet("")
        self.lbicon.setText("")
        self.lbicon.setPixmap(QtGui.QPixmap("supericongreen.png"))
        self.lbicon.setScaledContents(True)
        self.lbicon.setObjectName("lbicon")
        self.FRULTRAGAME = QtWidgets.QFrame(self.wsuperlottery)
        self.FRULTRAGAME.setGeometry(QtCore.QRect(100, 140, 551, 391))
        self.FRULTRAGAME.setStyleSheet("border: 1px solid green;")
        self.FRULTRAGAME.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRULTRAGAME.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRULTRAGAME.setObjectName("FRULTRAGAME")
        self.lbguesshere = QtWidgets.QLabel(self.FRULTRAGAME)
        self.lbguesshere.setGeometry(QtCore.QRect(190, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbguesshere.setFont(font)
        self.lbguesshere.setMouseTracking(True)
        self.lbguesshere.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbguesshere.setObjectName("lbguesshere")
        self.lblotresult = QtWidgets.QLabel(self.FRULTRAGAME)
        self.lblotresult.setGeometry(QtCore.QRect(190, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblotresult.setFont(font)
        self.lblotresult.setMouseTracking(True)
        self.lblotresult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lblotresult.setObjectName("lblotresult")
        self.PBSGO = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.supergo_action())
        self.PBSGO.setGeometry(QtCore.QRect(440, 90, 81, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.PBSGO.setFont(font)
        self.PBSGO.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(243, 255, 5);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.PBSGO.setObjectName("PBSGO")
        self.PBS1 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num1clicked())
        self.PBS1.setGeometry(QtCore.QRect(30, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS1.setFont(font)
        self.PBS1.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS1.setObjectName("PBS1")
        self.PBS2 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num2clicked())
        self.PBS2.setGeometry(QtCore.QRect(110, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS2.setFont(font)
        self.PBS2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS2.setObjectName("PBS2")
        self.PBS3 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num3clicked())
        self.PBS3.setGeometry(QtCore.QRect(190, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS3.setFont(font)
        self.PBS3.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS3.setObjectName("PBS3")
        self.PBS4 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num4clicked())
        self.PBS4.setGeometry(QtCore.QRect(270, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS4.setFont(font)
        self.PBS4.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS4.setObjectName("PBS4")
        self.PBS5 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num5clicked())
        self.PBS5.setGeometry(QtCore.QRect(350, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS5.setFont(font)
        self.PBS5.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS5.setObjectName("PBS5")
        self.PBS6 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num6clicked())
        self.PBS6.setGeometry(QtCore.QRect(30, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS6.setFont(font)
        self.PBS6.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS6.setObjectName("PBS6")
        self.PBS7 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num7clicked())
        self.PBS7.setGeometry(QtCore.QRect(110, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS7.setFont(font)
        self.PBS7.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS7.setObjectName("PBS7")
        self.PBS8 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num8clicked())
        self.PBS8.setGeometry(QtCore.QRect(190, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS8.setFont(font)
        self.PBS8.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS8.setObjectName("PBS8")
        self.PBS9 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num9clicked())
        self.PBS9.setGeometry(QtCore.QRect(270, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS9.setFont(font)
        self.PBS9.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS9.setObjectName("PBS9")
        self.PBS10 = QtWidgets.QPushButton(self.FRULTRAGAME, clicked=lambda: self.num10clicked())
        self.PBS10.setGeometry(QtCore.QRect(350, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBS10.setFont(font)
        self.PBS10.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 211, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(115, 255, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.PBS10.setObjectName("PBS10")
        self.SBALL1 = QtWidgets.QLabel(self.FRULTRAGAME)
        self.SBALL1.setGeometry(QtCore.QRect(90, 240, 131, 131))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SBALL1.setFont(font)
        self.SBALL1.setMouseTracking(True)
        self.SBALL1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.SBALL1.setText("")
        self.SBALL1.setPixmap(QtGui.QPixmap("ball.png"))
        self.SBALL1.setScaledContents(True)
        self.SBALL1.setObjectName("SBALL1")
        self.LCDSRES1super = QtWidgets.QLCDNumber(self.FRULTRAGAME)
        self.LCDSRES1super.setGeometry(QtCore.QRect(70, 270, 101, 61))
        self.LCDSRES1super.setStyleSheet("border-color: none;")
        self.LCDSRES1super.setObjectName("LCDSRES1super")
        self.SBALL2 = QtWidgets.QLabel(self.FRULTRAGAME)
        self.SBALL2.setGeometry(QtCore.QRect(320, 240, 131, 131))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SBALL2.setFont(font)
        self.SBALL2.setMouseTracking(True)
        self.SBALL2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.SBALL2.setText("")
        self.SBALL2.setPixmap(QtGui.QPixmap("ball.png"))
        self.SBALL2.setScaledContents(True)
        self.SBALL2.setObjectName("SBALL2")
        self.LCDSRES2super = QtWidgets.QLCDNumber(self.FRULTRAGAME)
        self.LCDSRES2super.setGeometry(QtCore.QRect(300, 270, 101, 61))
        self.LCDSRES2super.setStyleSheet("border-color: none;")
        self.LCDSRES2super.setObjectName("LCDSRES2super")
        self.frwalletsuper = QtWidgets.QFrame(self.wsuperlottery)
        self.frwalletsuper.setGeometry(QtCore.QRect(660, 140, 141, 101))
        self.frwalletsuper.setStyleSheet("border: 1px solid green;")
        self.frwalletsuper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frwalletsuper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frwalletsuper.setObjectName("frwalletsuper")
        self.lbjackpot_4 = QtWidgets.QLabel(self.frwalletsuper)
        self.lbjackpot_4.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbjackpot_4.setFont(font)
        self.lbjackpot_4.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbjackpot_4.setObjectName("lbjackpot_4")
        self.lcdwalletsuper = QtWidgets.QLCDNumber(self.frwalletsuper)
        self.lcdwalletsuper.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.lcdwalletsuper.setObjectName("lcdwalletsuper")
        self.frjackpotsuper = QtWidgets.QFrame(self.wsuperlottery)
        self.frjackpotsuper.setGeometry(QtCore.QRect(660, 250, 141, 101))
        self.frjackpotsuper.setStyleSheet("border: 1px solid green;")
        self.frjackpotsuper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frjackpotsuper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frjackpotsuper.setObjectName("frjackpotsuper")
        self.lbjackpot = QtWidgets.QLabel(self.frjackpotsuper)
        self.lbjackpot.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbjackpot.setFont(font)
        self.lbjackpot.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbjackpot.setObjectName("lbjackpot")
        self.lcdjackpotsuper = QtWidgets.QLCDNumber(self.frjackpotsuper)
        self.lcdjackpotsuper.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.lcdjackpotsuper.setObjectName("lcdjackpotsuper")
        self.LBLSUPERWINORLOSE = QtWidgets.QLabel(self.wsuperlottery)
        self.LBLSUPERWINORLOSE.setGeometry(QtCore.QRect(660, 360, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.LBLSUPERWINORLOSE.setFont(font)
        self.LBLSUPERWINORLOSE.setStyleSheet("color: rgb(255, 199, 0);\n"
"border: 1px solid green;")
        self.LBLSUPERWINORLOSE.setObjectName("LBLSUPERWINORLOSE")
        self.PBSPAGAIN = QtWidgets.QPushButton(self.wsuperlottery, clicked=lambda: self.superplay_again())
        self.PBSPAGAIN.setGeometry(QtCore.QRect(660, 420, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.PBSPAGAIN.setFont(font)
        self.PBSPAGAIN.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(243, 255, 5);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.PBSPAGAIN.setObjectName("PBSPAGAIN")
        self.PBSEXIT = QtWidgets.QPushButton(self.wsuperlottery, clicked=lambda: self.superexit())
        self.PBSEXIT.setGeometry(QtCore.QRect(660, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.PBSEXIT.setFont(font)
        self.PBSEXIT.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.PBSEXIT.setObjectName("PBSEXIT")
        self.secretsuper = QtWidgets.QLabel(self.wsuperlottery)
        self.secretsuper.setGeometry(QtCore.QRect(820, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        self.secretsuper.setFont(font)
        self.secretsuper.setStyleSheet("color: rgb(111, 111, 111);")
        self.secretsuper.setObjectName("secretsuper")
        self.wultra = QtWidgets.QWidget(self.centralwidget)
        self.wultra.setGeometry(QtCore.QRect(-1, -1, 901, 611))
        self.wultra.setObjectName("wultra")
        self.LBLUBG = QtWidgets.QLabel(self.wultra)
        self.LBLUBG.setGeometry(QtCore.QRect(-140, -30, 1171, 701))
        self.LBLUBG.setMouseTracking(False)
        self.LBLUBG.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.LBLUBG.setText("")
        self.LBLUBG.setPixmap(QtGui.QPixmap("shop.png"))
        self.LBLUBG.setScaledContents(True)
        self.LBLUBG.setObjectName("LBLUBG")
        self.label_7 = QtWidgets.QLabel(self.wultra)
        self.label_7.setGeometry(QtCore.QRect(190, 10, 541, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.wultra)
        self.label_9.setGeometry(QtCore.QRect(190, 30, 541, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.wultra)
        self.label_8.setGeometry(QtCore.QRect(190, 50, 591, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_8.setObjectName("label_8")
        self.lbicon_2 = QtWidgets.QLabel(self.wultra)
        self.lbicon_2.setGeometry(QtCore.QRect(80, 10, 91, 81))
        self.lbicon_2.setStyleSheet("")
        self.lbicon_2.setText("")
        self.lbicon_2.setPixmap(QtGui.QPixmap("ultraicongreen.png"))
        self.lbicon_2.setScaledContents(True)
        self.lbicon_2.setObjectName("lbicon_2")
        self.label_10 = QtWidgets.QLabel(self.wultra)
        self.label_10.setGeometry(QtCore.QRect(190, 70, 591, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 248, 32);")
        self.label_10.setObjectName("label_10")
        self.FRULTRAGAME_2 = QtWidgets.QFrame(self.wultra)
        self.FRULTRAGAME_2.setGeometry(QtCore.QRect(120, 130, 511, 401))
        self.FRULTRAGAME_2.setStyleSheet("border: 1px solid green;")
        self.FRULTRAGAME_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRULTRAGAME_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRULTRAGAME_2.setObjectName("FRULTRAGAME_2")
        self.lbguesshere_2 = QtWidgets.QLabel(self.FRULTRAGAME_2)
        self.lbguesshere_2.setGeometry(QtCore.QRect(140, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbguesshere_2.setFont(font)
        self.lbguesshere_2.setMouseTracking(True)
        self.lbguesshere_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbguesshere_2.setObjectName("lbguesshere_2")
        self.lblotresult_2 = QtWidgets.QLabel(self.FRULTRAGAME_2)
        self.lblotresult_2.setGeometry(QtCore.QRect(140, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblotresult_2.setFont(font)
        self.lblotresult_2.setMouseTracking(True)
        self.lblotresult_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lblotresult_2.setObjectName("lblotresult_2")
        self.PBUGO = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.ultrago_action())
        self.PBUGO.setGeometry(QtCore.QRect(380, 110, 101, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.PBUGO.setFont(font)
        self.PBUGO.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(243, 255, 5);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.PBUGO.setObjectName("PBUGO")
        self.UBALL1 = QtWidgets.QLabel(self.FRULTRAGAME_2)
        self.UBALL1.setGeometry(QtCore.QRect(20, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.UBALL1.setFont(font)
        self.UBALL1.setMouseTracking(True)
        self.UBALL1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.UBALL1.setText("")
        self.UBALL1.setPixmap(QtGui.QPixmap("ball.png"))
        self.UBALL1.setScaledContents(True)
        self.UBALL1.setObjectName("UBALL1")
        self.PBU1 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum1clicked())
        self.PBU1.setGeometry(QtCore.QRect(20, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU1.setFont(font)
        self.PBU1.setObjectName("PBU1")
        self.PBU2 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum2clicked())
        self.PBU2.setGeometry(QtCore.QRect(90, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU2.setFont(font)
        self.PBU2.setObjectName("PBU2")
        self.PBU3 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum3clicked())
        self.PBU3.setGeometry(QtCore.QRect(160, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU3.setFont(font)
        self.PBU3.setObjectName("PBU3")
        self.PBU4 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum4clicked())
        self.PBU4.setGeometry(QtCore.QRect(230, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU4.setFont(font)
        self.PBU4.setObjectName("PBU4")
        self.PBU5 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum5clicked())
        self.PBU5.setGeometry(QtCore.QRect(300, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU5.setFont(font)
        self.PBU5.setObjectName("PBU5")
        self.PBU6 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum6clicked())
        self.PBU6.setGeometry(QtCore.QRect(20, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU6.setFont(font)
        self.PBU6.setObjectName("PBU6")
        self.PBU7 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum7clicked())
        self.PBU7.setGeometry(QtCore.QRect(90, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU7.setFont(font)
        self.PBU7.setObjectName("PBU7")
        self.PBU8 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum8clicked())
        self.PBU8.setGeometry(QtCore.QRect(160, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU8.setFont(font)
        self.PBU8.setObjectName("PBU8")
        self.PBU9 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum9clicked())
        self.PBU9.setGeometry(QtCore.QRect(230, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU9.setFont(font)
        self.PBU9.setObjectName("PBU9")
        self.PBU10 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum10clicked())
        self.PBU10.setGeometry(QtCore.QRect(300, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU10.setFont(font)
        self.PBU10.setObjectName("PBU10")
        self.LCDURESULT1 = QtWidgets.QLCDNumber(self.FRULTRAGAME_2)
        self.LCDURESULT1.setGeometry(QtCore.QRect(0, 310, 81, 41))
        self.LCDURESULT1.setStyleSheet("border-color: none;")
        self.LCDURESULT1.setObjectName("LCDURESULT1")
        self.PBU11 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum11clicked())
        self.PBU11.setGeometry(QtCore.QRect(20, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU11.setFont(font)
        self.PBU11.setObjectName("PBU11")
        self.PBU12 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum12clicked())
        self.PBU12.setGeometry(QtCore.QRect(90, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU12.setFont(font)
        self.PBU12.setObjectName("PBU12")
        self.PBU13 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum13clicked())
        self.PBU13.setGeometry(QtCore.QRect(160, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU13.setFont(font)
        self.PBU13.setObjectName("PBU13")
        self.PBU14 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum14clicked())
        self.PBU14.setGeometry(QtCore.QRect(230, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU14.setFont(font)
        self.PBU14.setObjectName("PBU14")
        self.PBU15 = QtWidgets.QPushButton(self.FRULTRAGAME_2, clicked=lambda: self.unum15clicked())
        self.PBU15.setGeometry(QtCore.QRect(300, 180, 51, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.PBU15.setFont(font)
        self.PBU15.setObjectName("PBU15")
        self.UBALL2 = QtWidgets.QLabel(self.FRULTRAGAME_2)
        self.UBALL2.setGeometry(QtCore.QRect(180, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.UBALL2.setFont(font)
        self.UBALL2.setMouseTracking(True)
        self.UBALL2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.UBALL2.setText("")
        self.UBALL2.setPixmap(QtGui.QPixmap("ball.png"))
        self.UBALL2.setScaledContents(True)
        self.UBALL2.setObjectName("UBALL2")
        self.LCDURESULT2 = QtWidgets.QLCDNumber(self.FRULTRAGAME_2)
        self.LCDURESULT2.setGeometry(QtCore.QRect(160, 310, 81, 41))
        self.LCDURESULT2.setStyleSheet("border-color: none;")
        self.LCDURESULT2.setObjectName("LCDURESULT2")
        self.UBALL3 = QtWidgets.QLabel(self.FRULTRAGAME_2)
        self.UBALL3.setGeometry(QtCore.QRect(340, 280, 101, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.UBALL3.setFont(font)
        self.UBALL3.setMouseTracking(True)
        self.UBALL3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.UBALL3.setText("")
        self.UBALL3.setPixmap(QtGui.QPixmap("ball.png"))
        self.UBALL3.setScaledContents(True)
        self.UBALL3.setObjectName("UBALL3")
        self.LCDURESULT3 = QtWidgets.QLCDNumber(self.FRULTRAGAME_2)
        self.LCDURESULT3.setGeometry(QtCore.QRect(320, 310, 81, 41))
        self.LCDURESULT3.setStyleSheet("border-color: none;")
        self.LCDURESULT3.setObjectName("LCDURESULT3")
        self.FRRULTRAWALLET = QtWidgets.QFrame(self.wultra)
        self.FRRULTRAWALLET.setGeometry(QtCore.QRect(650, 130, 141, 101))
        self.FRRULTRAWALLET.setStyleSheet("border: 1px solid green;")
        self.FRRULTRAWALLET.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRRULTRAWALLET.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRRULTRAWALLET.setObjectName("FRRULTRAWALLET")
        self.lbjackpot_5 = QtWidgets.QLabel(self.FRRULTRAWALLET)
        self.lbjackpot_5.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbjackpot_5.setFont(font)
        self.lbjackpot_5.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbjackpot_5.setObjectName("lbjackpot_5")
        self.LCDWALLETULTRA = QtWidgets.QLCDNumber(self.FRRULTRAWALLET)
        self.LCDWALLETULTRA.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.LCDWALLETULTRA.setObjectName("LCDWALLETULTRA")
        self.FRULTRAJACKPOT = QtWidgets.QFrame(self.wultra)
        self.FRULTRAJACKPOT.setGeometry(QtCore.QRect(650, 240, 141, 101))
        self.FRULTRAJACKPOT.setStyleSheet("border: 1px solid green;")
        self.FRULTRAJACKPOT.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRULTRAJACKPOT.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRULTRAJACKPOT.setObjectName("FRULTRAJACKPOT")
        self.lbjackpot_2 = QtWidgets.QLabel(self.FRULTRAJACKPOT)
        self.lbjackpot_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lbjackpot_2.setFont(font)
        self.lbjackpot_2.setStyleSheet("color: rgb(0, 248, 32);\n"
"border-color: rgb(0, 170, 0);")
        self.lbjackpot_2.setObjectName("lbjackpot_2")
        self.LCDULTRAJACKPOT = QtWidgets.QLCDNumber(self.FRULTRAJACKPOT)
        self.LCDULTRAJACKPOT.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.LCDULTRAJACKPOT.setObjectName("LCDULTRAJACKPOT")
        self.LBLULTRAWINORLOSE_2 = QtWidgets.QLabel(self.wultra)
        self.LBLULTRAWINORLOSE_2.setGeometry(QtCore.QRect(650, 350, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.LBLULTRAWINORLOSE_2.setFont(font)
        self.LBLULTRAWINORLOSE_2.setStyleSheet("color: rgb(255, 199, 0);\n"
"border: 1px solid green;")
        self.LBLULTRAWINORLOSE_2.setObjectName("LBLULTRAWINORLOSE_2")
        self.PBUPAGAIN = QtWidgets.QPushButton(self.wultra, clicked=lambda: self.ultraplay_again())
        self.PBUPAGAIN.setGeometry(QtCore.QRect(650, 420, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.PBUPAGAIN.setFont(font)
        self.PBUPAGAIN.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(243, 255, 5);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.PBUPAGAIN.setObjectName("PBUPAGAIN")
        self.PBUEXIT = QtWidgets.QPushButton(self.wultra, clicked=lambda: self.ultraexit())
        self.PBUEXIT.setGeometry(QtCore.QRect(650, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.PBUEXIT.setFont(font)
        self.PBUEXIT.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.PBUEXIT.setObjectName("PBUEXIT")
        self.label_11 = QtWidgets.QLabel(self.wultra)
        self.label_11.setGeometry(QtCore.QRect(770, 560, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(104, 104, 104);")
        self.label_11.setObjectName("label_11")
        self.wwelcome = QtWidgets.QWidget(self.centralwidget)
        self.wwelcome.setGeometry(QtCore.QRect(0, 0, 901, 611))
        self.wwelcome.setObjectName("wwelcome")
        self.lbmainbg_3 = QtWidgets.QLabel(self.wwelcome)
        self.lbmainbg_3.setGeometry(QtCore.QRect(0, 0, 901, 621))
        self.lbmainbg_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);")
        self.lbmainbg_3.setText("")
        self.lbmainbg_3.setPixmap(QtGui.QPixmap("layout2.png"))
        self.lbmainbg_3.setScaledContents(True)
        self.lbmainbg_3.setObjectName("lbmainbg_3")
        self.lbtitle = QtWidgets.QLabel(self.wwelcome)
        self.lbtitle.setGeometry(QtCore.QRect(230, 170, 451, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.lbtitle.setFont(font)
        self.lbtitle.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbtitle.setObjectName("lbtitle")
        self.lbplayername = QtWidgets.QLabel(self.wwelcome)
        self.lbplayername.setGeometry(QtCore.QRect(240, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbplayername.setFont(font)
        self.lbplayername.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(35, 234, 13);")
        self.lbplayername.setObjectName("lbplayername")
        self.lenameinput = QtWidgets.QLineEdit(self.wwelcome)
        self.lenameinput.setGeometry(QtCore.QRect(420, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lenameinput.setFont(font)
        self.lenameinput.setStyleSheet("background-color: rgb(0, 198, 0);")
        self.lenameinput.setText("")
        self.lenameinput.setObjectName("lenameinput")
        self.pblogin = QtWidgets.QPushButton(self.wwelcome, clicked=lambda: self.login_action())
        self.pblogin.setGeometry(QtCore.QRect(280, 400, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.pblogin.setFont(font)
        self.pblogin.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(166, 248, 34);\n"
"    \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.pblogin.setObjectName("pblogin")
        self.pbnewuser = QtWidgets.QPushButton(self.wwelcome, clicked=lambda: self.newuser_action())
        self.pbnewuser.setGeometry(QtCore.QRect(480, 400, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.pbnewuser.setFont(font)
        self.pbnewuser.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    background-color: rgb(0, 248, 32);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(166, 248, 34);\n"
"    \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(0, 211, 0);\n"
"    \n"
"}")
        self.pbnewuser.setObjectName("pbnewuser")

        self.pbexitna = QtWidgets.QPushButton(self.wwelcome, clicked=lambda: self.exit_talaga())
        self.pbexitna.setGeometry(QtCore.QRect(380, 521, 141, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.pbexitna.setFont(font)
        self.pbexitna.setStyleSheet("QPushButton\n"
                                     "{\n"
                                     "   \n"
                                     "    background-color: red;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "   \n"
                                     "    background-color: yellow;\n"
                                     "    \n"
                                     "}\n"
                                     "QPushButton:pressed\n"
                                     "{\n"
                                     "   \n"
                                     "    background-color: red;\n"
                                     "    \n"
                                     "}")
        self.pbexitna.setObjectName("pbexitna")

        self.lblerror = QtWidgets.QLabel(self.wwelcome)
        self.lblerror.setGeometry(QtCore.QRect(250, 340, 381, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblerror.setFont(font)
        self.lblerror.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(226, 11, 4);")
        self.lblerror.setObjectName("lblerror")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.lblerror.hide()
        self.wsuperlottery.hide(); self.wultra.hide(); self.hwidget.hide(); self.wphwar.hide()
        self.lblnomoney.hide(); self.frshop.hide()
        self.lblitem1.hide(); self.lblitem5.hide(); self.lblitem6.hide(); self.lblitem4.hide(); self.lblitem3.hide(); self.lblitem2.hide()

        self.movie = QMovie("takbo.gif")
        self.takbuhan.setMovie(self.movie)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbsuperlottery.setText(_translate("MainWindow", "Super Lottery"))
        self.pbhorserace.setText(_translate("MainWindow", "Horse Race"))
        self.pbphwar.setText(_translate("MainWindow", "PH War"))
        self.pbultralottery.setText(_translate("MainWindow", "Ultra Lottery"))
        self.lbgamemode.setText(_translate("MainWindow", " GAME MODE"))
        self.lbbag.setText(_translate("MainWindow", "BAG"))
        self.pbshop.setText(_translate("MainWindow", "Shop"))
        self.pbexit.setText(_translate("MainWindow", "Exit"))
        self.lbshop.setText(_translate("MainWindow", "SHOP"))
        self.radioButton.setText(_translate("MainWindow", " PANDA          P150"))
        self.radioButton_2.setText(_translate("MainWindow", " PIG                P150"))
        self.radioButton_3.setText(_translate("MainWindow", " KOALA         P200"))
        self.radioButton_4.setText(_translate("MainWindow", " KITTEN         P200"))
        self.radioButton_5.setText(_translate("MainWindow", " PUPPY         P250"))
        self.radioButton_6.setText(_translate("MainWindow", " BEAR            P250"))
        self.pbshop_2.setText(_translate("MainWindow", "Buy"))
        self.pbshop_3.setText(_translate("MainWindow", "Go Back"))
        self.lblnomoney.setText(_translate("MainWindow", "YOU HAVE 0 MONEY LEFT!"))
        self.lbinputhere_2.setText(_translate("MainWindow", "Game Rules"))
        self.lbinputhere_4.setText(_translate("MainWindow", "⚔️ Distribute 100 Filipinos to Manila, Cebu and Davao"))
        self.lbinputhere_3.setText(_translate("MainWindow", "⚔️ Help the Filipinos win against the Spaniards!"))
        self.lbinputhere.setText(_translate("MainWindow", "Input Here ⚔️"))
        self.pbfight.setText(_translate("MainWindow", "Fight!"))
        self.lbfilleft.setText(_translate("MainWindow", "Filipinos left"))
        self.cbguess1ph.setItemText(0, _translate("MainWindow", "0"))
        self.cbguess1ph.setItemText(1, _translate("MainWindow", "10"))
        self.cbguess1ph.setItemText(2, _translate("MainWindow", "20"))
        self.cbguess1ph.setItemText(3, _translate("MainWindow", "30"))
        self.cbguess1ph.setItemText(4, _translate("MainWindow", "40"))
        self.cbguess1ph.setItemText(5, _translate("MainWindow", "50"))
        self.cbguess1ph.setItemText(6, _translate("MainWindow", "60"))
        self.cbguess1ph.setItemText(7, _translate("MainWindow", "70"))
        self.cbguess1ph.setItemText(8, _translate("MainWindow", "80"))
        self.cbguess1ph.setItemText(9, _translate("MainWindow", "90"))
        self.cbguess1ph.setItemText(10, _translate("MainWindow", "100"))
        self.cbguess2ph.setItemText(0, _translate("MainWindow", "0"))
        self.cbguess2ph.setItemText(1, _translate("MainWindow", "10"))
        self.cbguess2ph.setItemText(2, _translate("MainWindow", "20"))
        self.cbguess2ph.setItemText(3, _translate("MainWindow", "30"))
        self.cbguess2ph.setItemText(4, _translate("MainWindow", "40"))
        self.cbguess2ph.setItemText(5, _translate("MainWindow", "50"))
        self.cbguess2ph.setItemText(6, _translate("MainWindow", "60"))
        self.cbguess2ph.setItemText(7, _translate("MainWindow", "70"))
        self.cbguess2ph.setItemText(8, _translate("MainWindow", "80"))
        self.cbguess2ph.setItemText(9, _translate("MainWindow", "90"))
        self.cbguess2ph.setItemText(10, _translate("MainWindow", "100"))
        self.cbguess3ph.setItemText(0, _translate("MainWindow", "0"))
        self.cbguess3ph.setItemText(1, _translate("MainWindow", "10"))
        self.cbguess3ph.setItemText(2, _translate("MainWindow", "20"))
        self.cbguess3ph.setItemText(3, _translate("MainWindow", "30"))
        self.cbguess3ph.setItemText(4, _translate("MainWindow", "40"))
        self.cbguess3ph.setItemText(5, _translate("MainWindow", "50"))
        self.cbguess3ph.setItemText(6, _translate("MainWindow", "60"))
        self.cbguess3ph.setItemText(7, _translate("MainWindow", "70"))
        self.cbguess3ph.setItemText(8, _translate("MainWindow", "80"))
        self.cbguess3ph.setItemText(9, _translate("MainWindow", "90"))
        self.cbguess3ph.setItemText(10, _translate("MainWindow", "100"))
        self.mnl.setText(_translate("MainWindow", "Manila"))
        self.cebu.setText(_translate("MainWindow", "Cebu"))
        self.davao.setText(_translate("MainWindow", "Davao"))
        self.lbprizeph.setText(_translate("MainWindow", "  WALLET"))
        self.lbllandedat.setText(_translate("MainWindow", "Spaniards landed at"))
        self.lbpriceph.setText(_translate("MainWindow", " PRIZE"))
        self.pbplayagainph.setText(_translate("MainWindow", "play again"))
        self.pbexitph.setText(_translate("MainWindow", "Exit"))
        self.secretplaceph.setText(_translate("MainWindow", "Davao"))
        self.secretnumph.setText(_translate("MainWindow", "Davao"))
        self.label.setText(_translate("MainWindow", "Game Rules:"))
        self.label_2.setText(_translate("MainWindow", "🍀 Bet for a HORSE"))
        self.label_3.setText(_translate("MainWindow", "🍀 Win the jackpot prize if your horse wins the race!"))
        self.lbprice.setText(_translate("MainWindow", "PRIZE"))
        self.lbjackpot_3.setText(_translate("MainWindow", "WALLET"))
        self.pbpagainhorse.setText(_translate("MainWindow", "play again"))
        self.pbexithorse.setText(_translate("MainWindow", "Exit"))
        self.rbachilles.setText(_translate("MainWindow", "ACHILLES"))
        self.rbbullseye.setText(_translate("MainWindow", "BULLSEYE"))
        self.rbgulliver.setText(_translate("MainWindow", "GULLIVER"))
        self.rbmaximus.setText(_translate("MainWindow", "MAXIMUS"))
        self.rbpetra.setText(_translate("MainWindow", "PETRA"))
        self.rbrambo.setText(_translate("MainWindow", "RAMBO"))
        self.pbenterhorse.setText(_translate("MainWindow", "Enter"))
        self.lblwontherace.setText(_translate("MainWindow", "WON THE RACE"))
        self.secret.setText(_translate("MainWindow", "secret"))
        self.pbseeresultshorse.setText(_translate("MainWindow", "See result ➡️"))
        self.label_4.setText(_translate("MainWindow", "🍀 Win the jackpot prize if your guesses are correct!"))
        self.label_5.setText(_translate("MainWindow", "🍀 Choose TWO numbers"))
        self.label_6.setText(_translate("MainWindow", "Game Rules:"))
        self.lbguesshere.setText(_translate("MainWindow", "Guess here ⬇️"))
        self.lblotresult.setText(_translate("MainWindow", "LOTTERY RESULT"))
        self.PBSGO.setText(_translate("MainWindow", "GO!"))
        self.PBS1.setText(_translate("MainWindow", "1"))
        self.PBS2.setText(_translate("MainWindow", "2"))
        self.PBS3.setText(_translate("MainWindow", "3"))
        self.PBS4.setText(_translate("MainWindow", "4"))
        self.PBS5.setText(_translate("MainWindow", "5"))
        self.PBS6.setText(_translate("MainWindow", "6"))
        self.PBS7.setText(_translate("MainWindow", "7"))
        self.PBS8.setText(_translate("MainWindow", "8"))
        self.PBS9.setText(_translate("MainWindow", "9"))
        self.PBS10.setText(_translate("MainWindow", "10"))
        self.lbjackpot_4.setText(_translate("MainWindow", " WALLET"))
        self.lbjackpot.setText(_translate("MainWindow", "JACKPOT"))
        self.LBLSUPERWINORLOSE.setText(_translate("MainWindow", "YOU LOSE!"))
        self.PBSPAGAIN.setText(_translate("MainWindow", "play again"))
        self.PBSEXIT.setText(_translate("MainWindow", "exit"))
        self.secretsuper.setText(_translate("MainWindow", "secret"))
        self.label_7.setText(_translate("MainWindow", "Game Rules:"))
        self.label_9.setText(_translate("MainWindow", "🍀 Choose THREE numbers"))
        self.label_8.setText(_translate("MainWindow", "🍀 Win the jackpot prize if your guesses are correct!"))
        self.label_10.setText(_translate("MainWindow", "🍀 Enjoy the game!"))
        self.lbguesshere_2.setText(_translate("MainWindow", "Guess here ⬇️"))
        self.lblotresult_2.setText(_translate("MainWindow", "LOTTERY RESULT"))
        self.PBUGO.setText(_translate("MainWindow", "GO!"))
        self.PBU1.setText(_translate("MainWindow", "1"))
        self.PBU2.setText(_translate("MainWindow", "2"))
        self.PBU3.setText(_translate("MainWindow", "3"))
        self.PBU4.setText(_translate("MainWindow", "4"))
        self.PBU5.setText(_translate("MainWindow", "5"))
        self.PBU6.setText(_translate("MainWindow", "6"))
        self.PBU7.setText(_translate("MainWindow", "7"))
        self.PBU8.setText(_translate("MainWindow", "8"))
        self.PBU9.setText(_translate("MainWindow", "9"))
        self.PBU10.setText(_translate("MainWindow", "10"))
        self.PBU11.setText(_translate("MainWindow", "11"))
        self.PBU12.setText(_translate("MainWindow", "12"))
        self.PBU13.setText(_translate("MainWindow", "13"))
        self.PBU14.setText(_translate("MainWindow", "14"))
        self.PBU15.setText(_translate("MainWindow", "15"))
        self.lbjackpot_5.setText(_translate("MainWindow", " WALLET"))
        self.lbjackpot_2.setText(_translate("MainWindow", "JACKPOT"))
        self.LBLULTRAWINORLOSE_2.setText(_translate("MainWindow", "YOU LOSE!"))
        self.PBUPAGAIN.setText(_translate("MainWindow", "Play Again"))
        self.PBUEXIT.setText(_translate("MainWindow", "Exit"))
        self.label_11.setText(_translate("MainWindow", "secret"))
        self.lbtitle.setText(_translate("MainWindow", "LOTTERY GAME"))
        self.lbplayername.setText(_translate("MainWindow", "User name :"))
        self.pblogin.setText(_translate("MainWindow", "Log in"))
        self.pbnewuser.setText(_translate("MainWindow", "New User"))
        self.pbexitna.setText(_translate("MainWindow", "Exit"))
        self.lblerror.setText(_translate("MainWindow", "Player with this user name does not exist!"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
