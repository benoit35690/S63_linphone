# -*- coding: utf-8 -*-
from threading import Timer, Lock
import pyaudio
import wave
import Constantes
import time

class Tonalite:

    # lectureActive mis a jour par startLecture et stopLecture
    lectureActive   = None

    fichierTonalite = None
    lectureEnBoucle = 0
    mutex           = None
    timerLecture    = None
    pyAudio         = None
    waveFile        = None
    stream          = None
    data            = None

    def __init__(self):
        print "[Tonalite] __init__"
        self.mutex = Lock()
        self.pyAudio = pyaudio.PyAudio()

    def startLecture(self, fichier, boucle):
        print "[Tonalite] startLecture boucle= ", boucle
        self.mutex.acquire()
        try:
            if (self.lectureActive is not None) or\
                    self.waveFile is not None or\
                    self.stream is not None:
                print "[Tonalite] startLecture lecture en cours"

                # on ferme d'abord le flux en cours
                self.stream.stop_stream()
                self.stream.close()
                print "[Tonalite] startLecture stream closed"
                self.waveFile.close()
                print "[Tonalite] startLecture wave closed"
                self.lectureEnBoucle = None
                self.fichierTonalite = None
                self.lectureActive   = None

            # mise à jour avec parametre du flux à jouer
            self.lectureEnBoucle = boucle
            self.fichierTonalite = fichier

            # ouverture du flux à jouer
            self.waveFile = wave.open(self.fichierTonalite, 'rb')
            self.stream = self.pyAudio.open(
                                    format=self.pyAudio.get_format_from_width(
                                                self.waveFile.getsampwidth()),
                                    channels=self.waveFile.getnchannels(),
                                    rate=self.waveFile.getframerate(),
                                    output=True)

            if self.timerLecture is not None:
                print "[Tonalite] thread de lecture deja demarre"
            else:
                # demarage du thread de lecture
                print "[Tonalite] demarage du thread de lecture"
                self.timerLecture = Timer(0, self.lecture)
                self.timerLecture.start()

            self.lectureActive = 1
        finally:
            self.mutex.release()

    def stopLecture(self):
        print "[Tonalite] stopLecture"
        self.mutex.acquire()
        print "[Tonalite] stopLecture mutex.acquire done"
        try:
            # fermeture du flux
            if self.stream is not None:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
                print "[Tonalite] stopLecture stream closed"
            else:
                print "[Tonalite] self.stream is None"

            # fermeture du fichier
            if self.waveFile is not None:
                self.waveFile.close()
                self.waveFile = None
                print "[Tonalite] stopLecture wave closed"
            else:
                print "[Tonalite] self.waveFile is None"

            self.data = None

            # arret du thread de lecture
            if self.timerLecture is not None:
                self.timerLecture.cancel()
                self.timerLecture = None
            else:
                print "[Tonalite] self.timerLecture is None"

            self.lectureActive = None
        finally:
            self.mutex.release()
            print "[Tonalite] stopLecture mutex.release done"

    def lecture(self):
        # wave file can be closed outside of this thread by
        print "[Tonalite] lecture fichier = ", self.fichierTonalite, \
            " boucle = ", self.lectureEnBoucle

        lectureActive = None
        self.mutex.acquire()
        print "[Tonalite] lecture mutex.acquire 1 done"
        try:
            lectureActive = self.lectureActive
        finally:
            self.mutex.release()
            print "[Tonalite] lecture mutex.release 1 done"

        while lectureActive is not None:
            # ce while sert a gerer le rebouclage
            self.mutex.acquire()
            print "[Tonalite] lecture mutex.acquire 2 done"
            try:
                if self.waveFile is not None:
                    self.data = self.waveFile.readframes(Constantes.AUDIO_CHUNK)
            finally:
                self.mutex.release()
                print "[Tonalite] lecture mutex.release 2 done"

            while self.data is not None and\
                    self.data != '' and\
                    lectureActive:
                self.mutex.acquire()
                #print "[Tonalite] lecture mutex.acquire 3 done"
                try:
                    if self.stream is not None and\
                         self.waveFile is not None:
                        #print "[Tonalite] lecture stream.write"
                        if self.data is None or self.data == '':
                            print "[Tonalite] lecture self.data is None"
                        self.stream.write(self.data)
                        self.data = self.waveFile.readframes(Constantes.AUDIO_CHUNK)
                        lectureActive = self.lectureActive
                finally:
                    self.mutex.release()
                    #print "[Tonalite] lecture mutex.release 3 done"

            self.mutex.acquire()
            #print "[Tonalite] lecture mutex.acquire 4 done"
            try:
                if self.waveFile is not None and\
                   self.timerLecture is not None and\
                   self.lectureEnBoucle == 1:
                    print "[Tonalite] lecture rebouclage"
                    self.waveFile.rewind()
            finally:
                self.mutex.release()
                #print "[Tonalite] lecture mutex.release 4 done"

            # end while lectureActive

        print "[Tonalite] lecture fin de procedure"
