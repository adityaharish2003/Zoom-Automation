# Zoom-Automation
A tool in python to automate Zoom with respect to timetable and passwords/ids mentioned in a .csv file.
Run  `pip install -r requirements.txt` in your command shell to install the necessary libs.
Stores ids according to timetable in *ids.csv* and passwords in *pass.csv*


# Command line options 
Running `python3 auto.py --w` will parse the passwords from the word file(which must be saved as "*wordID.docx*") and enter it into *pass.csv*
Running `python3 auto.py --m` will result in entry user-based input of password and id followed by automated logging in.




To avoid complications keep the zoom window at the front with considerable height and width 
