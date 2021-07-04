#!/bin/python3
from json import loads as json
from os import system as cmd

episodes = None
dl_option = "wget -O "
src_url = "https://www.peppercarrot.com/0_sources/"

def dl(url, location):
    cmd(dl_option + location + " " + url)

dl(src_url + "episodes-v1.json", "episodes.json")

with open("episodes.json") as f:
    episodes = json(f.read())

for ep in episodes:
    cmd("mkdir " + ep["name"])
    dl(src_url + ep["name"] + "/hi-res/en_" + ep["pages"]["cover"], ep["name"] + "/" + ep["pages"]["cover"])
    for page in range(1, len(ep["pages"]) - 2):
        dl(src_url + ep["name"] + "/hi-res/en_" + ep["pages"][str(page)], ep["name"] + "/" + ep["pages"][str(page)])
    dl(src_url + ep["name"] + "/hi-res/en_" + ep["pages"]["credits"], ep["name"] + "/" + ep["pages"]["credits"])

for ep in episodes:
    cmd("img2pdf " + ep["name"] + "/*.jpg -o" + ep["name"] + ".pdf")
