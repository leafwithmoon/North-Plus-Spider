import pymongo
# this file include the configuration used in this project,please input your own username and password
# init website address
html_address = 'http://bbs.imoutolove.me/'

# user information
# input your own account
username = ''
password = ''

# fid indicate which section you want
# fid 4:Video 5:Painting 6:Game 14:CG 128:Voice 135:GalGame
fid_table = {
    4: "Video",
    5: "Painting",
    6: "Game",
    14: "CG",
    128: "Voice",
    135: "GalGame"
}
fid = 14

# fid_type indicate which category you want
# Video 0:All 1:Unknown 2:Raw 3:Chinese with Mosaic 4:Chinese without Mosaic 5:3D 6:MMD
# Painting 0:All 1:Japanese 2:Chinese 3:Collection 4:English
# Game 0:All 1:Enterprise Game 2:Personal Game
# CG 0:ALL 1:Game CG 2:Personal CG 3:Painting Collection
# Voice 0:All 1:Personal Voice 4: Personal Music
# GalGame 0:All
fid_type = 0

# mongodb config
MONGO_HOST = "10.128.6.39"
MONGO_PORT = 8290

client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = client.np


