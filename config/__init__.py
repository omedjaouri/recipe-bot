from os import environ

def get_env(key):
    return environ.get(key)
