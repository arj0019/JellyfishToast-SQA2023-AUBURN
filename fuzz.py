import constants
import logging
import os
import random
import scanner
import sys
import traceback

log_formatter = logging.Formatter("%(asctime)s %(message)s")
logger = logging.getLogger("fuzzLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("fuzz.log", mode='w')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

def fuzzYAML():
    if scanner.getYAMLFiles(os.getcwd()) == []: logger.error("path is valid; %s", os.getcwd())
    if scanner.getYAMLFiles(os.getcwd() + str(random.randint(100000,1000000))) != []: logger.error("path is not valid; %s does not exist", secret)

def fuzzUserName():
    [logger.error("username is not valid; %s is forbidden", uName) for uName in constants.FORBIDDEN_USER_NAMES if scanner.isValidUserName(uName) != False]
    [logger.error("username is not valid; %s != str", type(uName)) for uName in [0, 0.0, {}, [], True] if scanner.isValidUserName(uName) != False]

def fuzzPassword():
    [logger.error("username is not valid; %s is forbidden", pName) for pName in constants.FORBIDDEN_PASS_NAMES if scanner.isValidPasswordName(pName) != False]
    [logger.error("username is not valid; %s != str", type(pName)) for pName in [0, 0.0, {}, [], True] if scanner.isValidPasswordName(pName) != False]

def fuzzKey():
    [logger.error("key is valid; %s is legit", key) for key in constants.LEGIT_KEY_NAMES if scanner.isValidKey(key) != True]
    [logger.error("key is not valid; %s != str", type(key)) for key in [0, 0.0, {}, [], True] if scanner.isValidKey(key) != False]

def fuzzSecret():
    [logger.error("secret is not valid; %s is not legit", secret) for secret in constants.INVALID_SECRET_CONFIG_VALUES if scanner.checkIfValidSecret(secret) != False]
    if scanner.checkIfValidSecret('a') != False: logger.error("secret is not valid; %s is too short", secret)

if __name__=='__main__':
    fuzzYAML()
    fuzzUserName()
    fuzzPassword()
    fuzzKey()
    fuzzSecret()