# freshPy
A very simple Python script built using PRAW which searches /r/hiphopheads for any new releases by the artists listed in the artists.txt file.

Artists are written in the txt file on a separate line. Artists with alternative names can be grouped together by using a " / " between their names, this can then also be used to group together similar artists under one name.
The first artist's name will be the name which will be displayed for the searches.
The artists.txt file provided displays such examples.

Requires set-up using reddit application authorisation, and putting the client-id and client-secret into a file named "sensitive.txt" such that the id and secret are on separate lines.
