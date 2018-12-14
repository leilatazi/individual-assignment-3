# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:45:54 2018

@author: Leila
"""

#%%

#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.

from flask import Flask, jsonify

server = Flask("phonebookmanager")

phonebook = {"hannah":"514","javi":"123","felix":"456"}

@server.route("/add_contact/<name>/<phone>")
def add_contact(name,phone): 
    phonebook[name] = phone   
    return jsonify("You have added " + name + " to your list of contacts")

@server.route("/get_contact/<name>")
def get_contact(name): 
    phone = phonebook[name]   
    return jsonify("The phone number for " + name + " is " + phone)

@server.route("/delete_contact/<name>")
def delete_contact(name): 
    phonebook.pop(name)
    return jsonify("You have delete " + name + " from your list of contacts")

@server.route("/update_contact/<name>/<phone>")
def update_contact(name,phone): 
    phonebook[name] = phone   
    return jsonify("You have changed the phone number for " + name + " to " + phone)

@server.route("/phonebook")
def show_phonebook():
    return jsonify(phonebook)


server.run()