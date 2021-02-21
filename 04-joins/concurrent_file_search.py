import os
from os.path import isdir, join, expanduser
from threading import Lock, Thread

mutex = Lock()
matches = []

def file_search(root, filename):
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()

def main():
    dirname = expanduser('~') + '/Desktop'
    t = Thread(target=file_search, args=([dirname, '.DS_Store']))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)

main()
