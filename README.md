This is a simple apllication that fetches links from the wiki page.

It can be run in two modes GUI or command line.

GUI mode runs without any arguments, if argument is passed, then app will act in a command lime mode.

The results are presented in raw format without any preliminary prettify functions.

Run GUI mode:
python3 linkcounter.py

Run CL mode:
python3 -m linkcounter --get random 
                    or --view article_name (the string must be in quotes)
                    or --count article_name (the string must be in quotes)

setup.py is included in order to package project
