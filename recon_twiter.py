#!/usr/bin/python3
import os
import twint
import time
from colorama import init
from termcolor import colored


os.system('clear')
print('''\033[1;31;40m
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠾⠿⠿⠟⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠂     \033[1;m    ⠀⠀⠀⠀
\033[1;33;30m   ⠀⠀⠀⠀⠀⠀\033[1;m⠀⠰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀\033[1;36;40m⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀    \033[1;m
\033[1;33;30m   ⠀⠀⠀⠀⢀⣴⡄\033[1;m⠙\033[1;m⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\033[1;36;40m⠀⠀⠀⢀⣾⠋⡈⢿⡄⠀\033[1;m\033[1;32m+ -- -- +=[ Author : longhoang
\033[1;33;30m   ⠀⠀⢠⣾⣿⣿⣿⣦⡀\033[1;m⠀⠻⢿⣿⣿⣿⣿⣿⣿⠛⠛⠃\033[1;36;40m⠀⠀⠀⣼⡇⠀⠁⢸⡇⠀\033[1;m\033[1;32m+ -- -- +=[ T-L Recon
\033[1;33;30m   ⠀⣠⣤⣤⣌⣉⠙⠻⢿⣦⣄\033[1;m⠀⠙⠻⠿⣿⡿⠃\033[1;32;40m⠰⣦\033[1;m⠀⠀\033[1;36;40m⠀⠀⣿⡄⠀⠀⣼⠇⠀\033[1;m\033[1;32m+ -- -- +=[ Contact :
\033[1;33;30m   ⠀⣿⣿⣿⣿⣿⣿⣶⣤⣈⠛⢿⣶⣄⠀⠀⠀⠀\033[1;32;40m⢸⠇\033[1;m⠀⠀\033[1;36;40m⠀⠀⠸⣧⣀⣰⠏⠀⠀\033[1;m\033[1;32m+ -- -- +=[ Versions : v1.0
\033[1;33;30m   ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡈⠛⢷⠀⠀⠀\033[1;32;40m⣾\033[1;m⠀⠀⠀⠀\033[1;36;40m⠀⠀⢸⡿⠁⠀⠀⠀\033[1;m
\033[1;33;30m   ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀\033[1;32;40m⢸⣿⣿⣷⣦\033[1;m⠀\033[1;36;40m⠀⠀⢸⡇⠀⠀⠀⠀\033[1;m
\033[1;33;30m   ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀\033[1;32;40m⠘⠿⣿⠿⠋\033[1;m⠀⠀\033[1;36;40m⠀⣸⡇⠀⠀⠀⠀\033[1;m
\033[1;33;30m   ⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀\033[1;32;40m⠀⠀⠀⠀⠀ \033[1;36;40m ⠛⠁\033[1;m
        \033[1;m⠀⠀⠀⠀
''')


save = time.strftime("%Y.%m.%d - %H.%M.%S")
json = ('_top10_tweets.json')
csv = ('_top10_tweets.csv')
search = input("[!] What do you want to search ? ")
x = input("[!] Choose file save format 1 (json) or 2 (csv) ? ")
likes = input("[!] Filter Like minimum ? ")
retweets = input("[!] Filter retweets minimum ? ")
replies = input("[!] Filter replies minimum ? ")

if x == "1" :
    c = twint.Config()
    c.Search = search
    c.Populer_tweets = True
    c.Store_json = True
    c.Hashtags = True
    c.Timeline = True
    c.Output = save + json
    c.Min_likes = likes
    c.Min_retweets = retweets
    c.Min_replies = replies
    twint.run.Search(c)
else :
    c = twint.Config()
    c.Search = search
    c.Populer_tweets = True
    c.Store_csv = True
    c.Hashtags = True
    c.Timeline = True
    c.Output = save + csv
    c.Min_likes = likes
    c.Min_retweets = retweets
    c.Min_replies = replies
    twint.run.Search(c)
    