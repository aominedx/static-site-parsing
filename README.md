Parsing is only suitable for static websites.
To ensure proper operation, run the following commands in the terminal:
pip install -r requirements.txt
pip freeze > requirements.txt
Next, in the file code "download_excel", change the link to the correct location of the Excel file.
Also, to reduce the load on the site, it is advisable to set sleep() randomly between 1 and 3 seconds.
