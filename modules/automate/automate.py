# -*- coding: utf-8 -*-
# module Automate
"""

"""
import sys
import signal
from modules.cadran.cadran import Cadran
from modules.combine.combine import Combine


class Automate:

    Cadran  = None
    Combine = None

    def __init__(self):
        """
            Initialisation de la PIN du Raspberry reliée au cadran du S63
        """
#        signal.signal(signal.SIGINT, self.OnSignal)

        self.Cadran = Cadran()
        self.Combine = Combine()

        self.Cadran.RegisterCallback(NotificationChiffre=self.ReceptionChiffre)
        self.Combine.RegisterCallback(
            NotificationDecroche=self.ReceptionDecroche,
            NotificationRaccroche=self.ReceptionRaccroche,
            NotificationVerifDecroche=self.ReceptionVerifDecroche)

    def NotificationChiffre(self, chiffre):
        print ("[Automate NotificationChiffre] Chiffre recu = ", chiffre)

    def ReceptionDecroche(self):
        print ("[Automate ReceptionDecroche] Chiffre recu = ")

    def ReceptionRaccroche(self):
        print ("[Automate ReceptionRaccroche] Chiffre recu = ")

    def ReceptionVerifDecroche(self, etat):
        print ("[Automate ReceptionVerifDecroche] Chiffre recu = ", etat)

#    def OnSignal(self, signal, frame):
#        print "[SIGNAL] Shutting down on %s" % signal
#        sys.exit(0)
