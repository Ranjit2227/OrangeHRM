import configparser

config= configparser.ConfigParser()

config.read("Config/config.ini")

""" create methods """

def get_base_url():
    return config["url"]["base_url"]

def get_browser():
    return  config["browser"]["type"]

def get_username():
    return  config["credentials"]["username"]

def get_password():
    return config["credentials"]["password"]

