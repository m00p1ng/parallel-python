import json
import urllib.request
import time
from threading import Thread

finished_count = 0

def count_letter(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1

def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0

    start = time.time()
    for i in range(1000, 1020):
        url = f"http://www.rfc-editor.org/rfc/rfc{i}.txt"
        print(url)
        Thread(target=count_letter, args=(url, frequency)).start()
    while finished_count < 20:
        time.sleep(0.5)
    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)

main()

