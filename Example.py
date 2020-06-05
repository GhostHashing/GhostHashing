import GhostHashing #Imports the GhostHashing.py file if it is in the current directory. If not, please move it to it.

print(GhostHashing.Hash("Hello World!", "28e9uasd", 64)) #Hashes the string "Hello World!" with salt 28e9uasd with finally hashes the result 64 times with SHA256
