import keyboard

class KeyboardListener:
    @staticmethod
    def is_pressed(key):
        return keyboard.is_pressed(key)