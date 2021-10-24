# -------------------------------- Sniffer --------------------------------
# -------------------------------- <img src="https://github.com/leyuskckiran1510/Sniffer/blob/main/sniffer/sniffer.png"  height="150"> --------------------------------
The one only sniffer to sniff out provided text or file extension directory from any depth of folders. Nothing can escape from it's nose.



# insalling
```python
python -m pip install -r requirements.txt


```
# How to use
 ```python
 python ./sniffer.py -h  # for help
 python ./sniffer.py -p "C:/User/user" -t "hello"  # goes through every files and folder under path C:/User/user.. and print the path of files containig 
                                                   # string "hello" utf-8    encoded only for now
python ./sniffer.py -p "C:/" -e "mp4,jpg,png"     # will print all the paths of files having extension mp4,jpg,png under dir "C:/"
python ./sniffer.py -p "C:/" -r "[a-zA-Z]{5}[0-9]{2}" # will print all the files path having text that mathes the given regex pattren
puthon ./sniffer.py -e "jpg" # will print path of files containig jpg extension from the dirictory of the sniffer file 
python ./sniffer.py -l # will print all the files under the current dir or use -p to specify path 

# And yes you may be confused but Yes it can go folder inside the folder inside the folder deep under to the last fiels to find the files and will print their path if matchs the 
# specification

 ```
  

## What is the Use case then
1) If you have huge folder with many files and folder inside of it and you forget the file name that contains your data but you know some data like "username" .. 
    then you can just do 
    `python ./sniffer.py -p "your folder path" -t "username" `
    And it will print all the paths of files containig the word "username". Doing so you can save lot of your time and avoid the boring task of opening the file and waiting for      it to open then search for the word you want.

2) If you decompile some .dll or .apk or any other files then it will give you a huge folder with tons of folders and files then if you want to just find some text pattren in it
    like ; Let's take ann example . You want to find urls in that source file so that you may find some importannt endpoints for bug bounty
    then you can just run
    `python ./sniffer.py -p "your folder path" -r "pattren of data you want to search" `
  then it will print the dir for it you can directly open that specific file and continue your search insted of opening random file sand hoping to find some
  or you can just modify the code and print the text that matchs the pattren the you can find all the url printed in your console.
3) And many more that I can't even list here like for encoding the all the files or decoing all the file of a folder just by adding some small codein ti....
  


# Some inportant note
```diff
+ you must have python >3.5
+ permission to scan the folders 
+ basic knowledge of scripting and python

```

