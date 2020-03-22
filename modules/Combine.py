# -*- coding: utf-8 -*-
# module Combine
"""
    Module qui gère le contact electrique reçue de l'interrupteur du combine
    du S63
    Notifie l'état du combiné
"""

import Constantes
import RPi.GPIO as GPIO
from threading import Timer
import time


class Combine:
    # Timer to ensure we're on hook
    onhook_timer = None
    should_verify_hook = True

    def __init__(self):
        """
            Initialisation de la PIN du Raspberry reliée au combiné du S63
        """
        print ("[Combine __init__]")

        # Set GPIO mode to Broadcom SOC numbering
        GPIO.setmode(GPIO.BCM)

        # Configuration du GPIO pour écouter les mouvements du cadran
        # On utilise un "pull up" pour forcer l'état haut quand l'interrupteur
        # du combiné est ouvert
        # pour éviter d'être notifié plusieurs fois par évenement, on définie
        # un temps d'anti-rebond de 100 ms
        # A chaque changement d'état la callback EvenementDecroche est appelée
        GPIO.setup(Constantes.PIN_COMBINE, GPIO.IN,
                   pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(Constantes.PIN_COMBINE, GPIO.BOTH,
                              callback=self.EvenementDecroche,
                              bouncetime=Constantes.PIN_COMBINE_ANTIREBOND)

#        self.onhook_timer = Timer(2, self.verifyHook)
#        self.onhook_timer.start()

    def EvenementDecroche(self, channel):
        print ("[Combine EvenementDecroche]")
        input = GPIO.input(Constantes.PIN_COMBINE)
        if input:
            self.etat_decroche = 1
            self.NotificationRaccroche()
        else:
            self.etat_decroche = 0
            self.NotificationDecroche()

#    def StopVerifyHook(self):
#        print("[RotaryDial StopVerifyHook]", input)
#        self.should_verify_hook = False

#    def verifyHook(self):
#        while self.should_verify_hook:
#            state = GPIO.input(self.pin_onhook)
#            #if state == GPIO.HIGH:
#            #    print("[RotaryDial verifyHook] HIGH")
#            #else:
#            #    print("[RotaryDial verifyHook] LOW")
#            self.OnVerifyHook(state)
#            time.sleep(1)

    # Enregistrement des callbacks
    def RegisterCallback(self, NotificationDecroche, NotificationRaccroche):
    #                     NotificationVerifDecroche):
        """
            Enregistrement de la callbacks utilisée pour notifier quand
            l'état du combiné change
        """
        print ("[Combine RegisterCallback]")
        self.NotificationDecroche = NotificationDecroche
        self.NotificationRaccroche = NotificationRaccroche
#        self.NotificationVerifDecroche = NotificationVerifDecroche
        input = GPIO.input(Constantes.PIN_COMBINE)
        if input:
            self.NotificationDecroche()
        else:
            self.NotificationRaccroche()