#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:31:24 2022

@author: phillipcatanzaro

Wiki Search Engine
"""

"""
This is my first time working with Flask, so I have comments to help me 
work through and understand it.
"""
import requests #for requesting URL
from bs4 import BeautifulSoup #parse HTML code

import wikipedia

from flask import Flask, render_template
app = Flask(__name__)
from flask import jsonify #to make it so we can return list to flask
 



@app.route("/") #function decorator, what url will trigger function
def main():
    return render_template('index.html')
    return "<h1>Type in a slash followed by the category.<h1>"

@app.route("/<name>") #variable placed after 
def search(name):
    try:
        word = wikipedia.search(name)
        wikipedia.summary(name,auto_suggest = False)  #test if there is one match
        searchResults = wikipedia.search(name) #gets list of search results

        #turning off auto_suggest prevents weird results 
        #page= wikipedia.page(name) 
        link =  "https://en.wikipedia.org/wiki/" + searchResults[0]
        return link

    except: 
        #display items from search
        search = wikipedia.search(name)
        
        i = 0 #counter for for loop and links list
        links = [] #empty list to add possible links
        for queries in search:
            links.append("https://en.wikipedia.org/wiki/" + search[i])
            i = i + 1;
        return jsonify(links)

        

#for the app to start
if __name__ == '__main__':
    # inorder to turn on debug mode
	app.run(debug=True)
