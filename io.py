import pickle
import json


class Text:

    @staticmethod
    def load(path, lines=False):
        with open(path, 'r') as file:
            if lines:
                return file.readlines()
            return file.read()

    @staticmethod
    def save(path, string):
        with open(path, 'w') as file:
            file.write(string)

class Pickle:
    @staticmethod
    def load(path):
        with open(path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def save(path, obj):
        with open(path, 'wb') as file:
            pickle.dump(obj, file)


class Json:

    @staticmethod
    def load(path):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save(path, dictionary):
        with open(path, 'wb') as file:
            json.dump(dictionary, file)
