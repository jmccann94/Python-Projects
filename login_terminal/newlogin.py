#!/usr/bin/python3

import os
import io
import string

filename = "data/data.txt"
userInfo = {}


def initialize():
    try:
        f = open(filename, "r")
        lines = [line.rstrip() for line in f]
    except:
        print("No Users Currently Exist, Or Data File Is Missing")
        return
    pair = ""
    for l in lines:
        pair = l.split(" ", 1)
        userInfo.update( { pair[0] : pair[1] } )
    f.close()

def userExist(user):
    for key, value in userInfo.items():
        if (key == user):
            return True
    return False

def verifyPass(user, passphrase):
    chances = 3
    while chances > 0: 
        for key, value in userInfo.items():
            if ((key == user) and (value == passphrase)):
                return True
        chances = chances - 1
        print( chances + "Attempts Remaining")
        passphrase = input("Please Enter Password: ")
    print("Out Of Attempts")
    return False

def userPrompt(user):
    print("Greeting " + user)
    while True:
        print("Select An Option From The List:")
        print("c - Change Password")
        print("l - List Users")
        print("d - Delete User")
        print("e - Logout")
        x = input("")
        if x in ("C", "c"):
            changePass(user)
        elif x in ("L", "l"):
            print("User List:")
            listUser()
        elif x in ("D", "d"):
            deleteUser()
        elif x in ("E", "e"):
            return
        else:
            print("Invalid Entry")

def changePass(user):
    attempts = 3
    while attempts > 0:
        pass1 = input("Input Passphrase:\n")
        pass2 = input("Input Passphrase Again\n")
        attempts = attempts - 1
        if pass1 == pass2:
            userInfo[user] = pass1
            try:
                f = open("data/data.txt", "w")
                for key, value in userInfo.items():
                    f.write(key + " " + value + "\n")
                f.close()
            except:
                print("Saving Data Error")
            return
    
def listUser():
    for key, value in userInfo.items():
        print(key)

def deleteUser():
    print("User List")
    listUser()
    x = input("Enter User To Delete: ")
    try:
        del userInfo[x]
        try:
            f = open("data/data.txt", "w")
            for key, value in userInfo.items():
                f.write(key + " " + value + "\n")
            f.close()
        except:
            print("Saving Data Error")
    except:
        print("User Does Not Exist")

def yesOrno():
    while True:
        x = input("Enter y/n:")
        if x not in ("n", "y", "N", "Y"):
            print("Try Again")
        elif x in ("n", "N"):
            return False
        elif x in ("y", "Y"):
            return True
        
def addUser(user):
    attempts = 3
    while attempts > 0:
        pass1 = input("Input Passphrase:\n")
        pass2 = input("Input Passphrase Again\n")
        attempts = attempts - 1
        if pass1 == pass2:
            userInfo.update({ user : pass1 })
            try:
                f = open("data/data.txt", "a")
                f.write(user + " " + pass1 + "\n")
                f.close()
            except:
                print("Appending Data error")
            return
        

#main loop
initialize()

while True:
    
    currUser = input("Please Enter Username: ")

    if userExist(currUser):
        passphrase = input("Please Enter Password: ")
        if(verifyPass(currUser, passphrase)):
            print("Login Successful")
            userPrompt(currUser)
    else:
        print(currUser + " Does Not Exist, Would You Like To Create One?")
        if yesOrno():
            addUser(currUser)
    



    
