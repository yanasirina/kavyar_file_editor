# Kavyar files editor
This project is made for magazines that get submissions from kavyar.com

## What is Kavyar
Kavyar is a platform, that connects creatives and publishers. More than 600 magazines get submissions from photographers 
via this platform.
You can get more information about Kavyar here: **<a href="https://kavyar.com/home">kavyar.com</a>**

## Why can this project be helpful
Kavyar has the same submission form for all partner magazines. Photographers send pictures and informations about them 
using this form.
Then Kavyar generates folders with photos and txt files. These txt files need to be manually parsed and modified.
For example, magazines usually need to separately collect submitters' instagrams and emails, information for the cover 
and for pages.
These things are usually made manually. However, this project allows magazines to automate such routine work.

## How to use
Python file should be placed in a directory with folders created by Kavyar. The next step is running program.
```
python main.py
```
After running the app it will create 3 txt files:
<li>file1.txt includes all information for the cover</li>
<li>file2.txt includes all information for pages</li>
<li>file3.txt includes title and participants of the shooting, their emails and instagrams</li><br>
This program also translates russian text in english, if submitter forgot to translate it theirselves.

## Example of work
There is a directory 'example' in this project that includes folders that were made by Kavyar, main.py and files created 
using it.
In this directory you can see how the program works.

## The idea of the project
For a long time i was a designer in Marika Magazine, that gets submissions from Kavyar. 
It usually took me about an hour a day to create all the txt files, so I decided to automate this proccess and make my 
and other Marika's designers work easier. However, Marika is only one of more than 600 magazines on the Kavyar and 
details of generating files there can be differents. That is why i publish the code here, so people from other magazines 
can change it to build a files' editor for them.
