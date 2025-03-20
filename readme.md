# HvZ Noti Application

This application is my attempt to stop myself from staring at my school's Humans Vs Zombies website while I'm in class by having notifications sent to both my discord account and my phone. 

## Main Goals
This application is relatively simple and requires performs 3 main tasks:
1. Maintain an up-to-date human and zombie count obtained from the website (https://hvzrit.club).
2. Host that information in a JSON that is obtainable through a curl or rest request
3. Send notifications to my discord account when certain thresholds are reached (50/50 split of humans and zombies, zombie majority, etc.)

## Tech Stack

This application is going to be built mostly using python. I may attempt to rewrite it in rust at some point to learn rust, but since I am making this the weekend before the weeklong game starts, I am going to stick with what I know for now.

To obtain the human and zombie count from the hvz website, I am going to build a webscraper using MechanicalSoup. The JSON will be obtainable using a Flask app, and phone notifications will be done using the iPhone `Shortcuts` feature.