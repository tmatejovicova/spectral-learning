import pickle

class ObjectMethods:
    """
    Methods to save and load objects using pickle
    """
    def __init__(self):
        return

    @staticmethod
    def save_obj(obj, name, folder):
        obj_name = folder + '/' + name + '.pkl'
        with open(obj_name, 'wb') as file:
            pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_obj(name, folder):
        obj_name = folder + '/' + name + '.pkl'
        with open(obj_name, 'rb') as file:
            return pickle.load(file)
