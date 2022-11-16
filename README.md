![📚_Project_Library](https://user-images.githubusercontent.com/90692939/200117993-2d724024-09e0-4769-8c69-b8a13b7920db.png)
# Project Library
A Python Flask website for renting books from a bookstore with some other features
## Requirements
Recommended python version=3.9.13

You will need this python packages below
```bash
bcrypt
flask 
flask_sqlalchemy
flask_bcrypt
flask_wtf
functools
datetime
sqlalchemy
cv2
pytesseract
numpy
werkzeug.utils
os
wtforms
mysql
```
Also you need to download tesseract-ocr for this project

For Windows: [tesseract-ocr](https://github.com/UB-Mannheim/tesseract/wiki)

For Linux:
```bash
sudo apt install tesseract-ocr -y
```
For Mac:
```bash
brew install tesseract
```
You will need to change the tesseract-ocr location with yours at dashboard.py line 207

You will need to change the database address at config.py file to your local/online database server address

Here is the database you will need:
[db_server.zip](https://github.com/Blankbee/project_library/files/10025744/db_server.zip)


Here is the some images of the project:
[bs-images.zip](https://github.com/Blankbee/project_library/files/10025691/bs-images.zip)


## Running
Just run the app.py file and you are good to go
