
The Holberton School Checker App

This Application will allow you to send correction requests by taking your holberton informations 
- Holberton email
- Holberton password
- Your Holberton API key (that you’ll find on the intranet/tools).
- Click on Connect


Once you’ve made your authentication you’ll just need to pass the project ID and the number of the task that you want to check and then click on Request Correction to send a correction request. Once the progress bar is loaded you’ll finally see the result of the correction.


Installation:
To develop this up we used Kivy to build the graphical interface. That leads to say that You'll need to have kivy on your laptop. It's really simple and it won't take much of your time.

You'll need to update your pip:

$ python -m pip install --upgrade --user pip setuptools virtualenv

Then make and load the virtualenv. This is optional, but highly recommended:

$ python -m virtualenv ~/kivy_venv

$ source ~/kivy_venv/bin/activate

Finally install the Kivy wheel and optionally the kivy-examples:

$ python -m pip install kivy

$ python -m pip install kivy_examples

To run the program just type:

$ python3 main
