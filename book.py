"""
**Lots of features yet to be added**, including:
* Booking for any given day. At present, script only works for a specific day
* Deleting/Editing existing bookings
* Printing the day's menu to your terminal
* Better error handling and checking for booking success
* Viewing your profile (how many bookings you have made this term, etc.)
* Printing out special events and enabling booking for those as well
* Adding to waitlist in case booking has closed

Also would be nice to restructure the program so that Raven authentication is
done right after login credentials are entered so that potential errors are
detected before having to input a lot of other data (which can be annoying)
"""

from robobrowser import RoboBrowser
import time


def event(selection):
    return {
        'f': '618',  # first hall
        'o': '617',  # formal hall
        'c': '623',  # cafeteria hall
        's': '622',  # sunday formal hall
    }.get(selection, 'error')  # return error for invalid input


# def confirm_book_success(html):
#     #TODO


# login credentials and other input data
"""
This will be replaced with a 'default settings option' wherein the
default settings are stored in a text file and read from at runtime
"""

print('Enter your CRSid: ')
raven_id = input()

print('Enter your Raven password: ')
raven_password = input()

# TODO improve by accepting days of the week as input -
# choosing the upcoming one by default
print('Enter day to book for in yyyy-mm-dd format: ')
date = input()

print('Enter \'f\' for first hall, \'o\' for formal hall,\n \'c\' for '
      'Cafeteria Hall or \'s\' for Sunday Formal: ')
selection = input()

event = event(selection)
book_url = 'https://www.mealbookings.cai.cam.ac.uk/bookings.php?event=' + \
            event + '&date=' + date  # generate custom booking URL
raven_url = 'https://raven.cam.ac.uk/auth/login.html'  # raven login URL


browser = RoboBrowser(parser='html.parser')

# Login to Raven
browser.open(raven_url)
raven_form = browser.get_form(action="authenticate2.html")
raven_form['userid'].value = raven_id
raven_form['pwd'].value = raven_password
browser.submit_form(raven_form, submit=raven_form['submit'])

print('Passed Raven')

# Proceed to specific entry on meal booking website
browser.open(book_url)

# Click on 'Meal Booking' button
init_form = browser.get_form(method='post')
browser.submit_form(init_form, submit=init_form.submit_fields['edit'])
# submit = init_form['edit']

# Submit final form
final_form = browser.get_form(action='')
browser.submit_form(final_form)
# submit = final_form['update'] ////  ,
# submit=final_form.submit_fields["update"]

print(browser.parsed)  # print out HTML of final page
# print('Success')
