from abc import ABC, abstractmethod


class Hero:
    power = None
    @abstractmethod
    def superPower(self):
        pass

    def display(self):
        print("i am a super hero.")
