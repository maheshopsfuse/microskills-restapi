import hashlib
import os


def convertMD5(password):
    return str(hashlib.md5(str(password).encode()).hexdigest())


def generateSalt():
    return os.urandom(32)


def convertPBKDF2_HMAC(password, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        b'{salt}',
        100000
    )
    return key


def generatePassword(password, salt):
    password = convertMD5(password=password)
    password = convertPBKDF2_HMAC(password, salt)
    return password


def validatePassword(password, currentPassword, salt):
    password = convertMD5(password=password)
    password = convertPBKDF2_HMAC(password, salt)
    if currentPassword == str(password):
        return True
    return False
