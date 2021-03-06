# -*- coding: utf-8 -*-
# module Constantes
"""
    Definie les constantes utilisées dans le projet
"""

# liste des PIN du Raspberry
PIN_CADRAN               = 4
PIN_COMBINE              = 3
PIN_SOLENOIDE_GAUCHE     = 1
PIN_SOLENOIDE_DROIT      = 2
PIN_COMBINE_ANTIREBOND   = 100

# liste des timer
TIMER_INITIALISATION     = 0
TIMER_DECROCHER_REPOS    = 1
TIMER_TONAL_ACHEMINEMENT = 2

# aprés 0.9s on considère que le cadran a fini de numéroter le chiffre
TIMOUT_CHIFFRE_CADRAN    = 0.9
TEMPO_ENTRE_IMPULSIONS   = 0.002

TIMER_COMBINE            = 2
TIMEOUT_VERIF_COMBINE    = 1

TIMEOUT_AUTOMATE         = 0.5
TIMEOUT_DECROCHE_REPOS   = 20
#TIMEOUT_DECROCHE_REPOS   = 10
TIMEOUT_INITIALISATION   = 5

# etats du combiné
COMBINE_INITIALISATION   = 0
COMBINE_DECROCHE         = 1
COMBINE_RACCROCHE        = 2

# liste des états de l'automate
ETAT_INIT                = 0
ETAT_REPOS               = 1
ETAT_DECROCHE_REPOS      = 2
ETAT_DECROCHE_OUBLIE     = 3
ETAT_SONNERIE            = 4
ETAT_APPEL_ENTRANT       = 5
ETAT_NUMEROTATION        = 6
ETAT_TONALITE_SORTANT    = 7
ETAT_INIT_APPEL_SORTANT  = 8
ETAT_ECHEC_APPEL_SORTANT = 9
ETAT_APPEL_SORTANT       = 10

# liste des transitions de l'automate
TRANSITION_INIT          = 0
TRANSITION_RACCROCHE     = 1
TRANSITION_DECROCHE      = 2
TRANSITION_APPEL_ENTRANT = 3
TRANSITION_FIN_APPEL     = 4
TRANSITION_TIMER_OUBLIE  = 5
TRANSITION_ECHEC_NUM     = 6
TRANSITION_CHIFFRE_COMP  = 7
TRANSITION_NUMERO_VALIDE = 8
TRANSITION_TIMER_SORTANT = 9
TRANSITION_TIMER_NUMEROT = 10
TRANSITION_FIN_TON_ECHEC = 11
TRANSITION_TIMER_CONNEX  = 12
TRANSITION_APPEL_SORTANT = 13

AUDIO_CHUNK              = 1024

#liste des tonalités
TONALITE_OCCUPATION      = "./assets/ringtones/tonalites/occupation.WAV"
TONALITE_INVITATION      = "./assets/ringtones/tonalites/invitation_a_numeroter.WAV"
TONALITE_ACHEMINEMENT    = "./assets/ringtones/tonalites/acheminement.WAV"
