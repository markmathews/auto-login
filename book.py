'''

**Lots of features yet to be added**, including:
* Booking for any given day. At present, script only works for a specific day
* Deleting/Editing existing bookings 
* Printing the day's menu to your terminal 
* Better error handling and checking for booking success 

'''

from robobrowser import RoboBrowser 

raven_url = 'https://raven.cam.ac.uk/auth/login.html'
print('Enter your CRSid')
raven_id = input() #ENTER CRSID
print('Enter your Raven password')
raven_password = input() #ENTER RAVEN PASSWORD
book_url = 'https://www.mealbookings.cai.cam.ac.uk/bookings.php?event=618&date=2017-02-06'

browser = RoboBrowser(parser = 'html.parser')

#login to Raven 
browser.open(raven_url) 
raven_form = browser.get_form(action = "authenticate2.html")
raven_form['userid'].value = raven_id  
raven_form['pwd'].value = raven_password  
browser.submit_form(raven_form, submit = raven_form['submit'])

print('Passed Raven')

#Proceed to specific entry on meal booking website 
browser.open(book_url)

#click on 'Meal Booking' button
init_form = browser.get_form(method = "post")
browser.submit_form(init_form, submit=init_form.submit_fields["edit"]) #submit = init_form['edit']

#submit final form 
final_form = browser.get_form(action = '')
browser.submit_form(final_form) #submit = final_form['update'] ////  , submit=final_form.submit_fields["update"]

print(browser.parsed) #print out HTML of final page 
print('Success')




