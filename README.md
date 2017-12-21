# VuduList
A python program to login to your vudu account and scrape the names of the movies you own

It opens chrome using selenium, must have chrome driver installed

Navigates to Vudu login page

Logs into your account !!!Make sure to change your username and password to make this work!!!

After login it navigates to the My Vudu section

It scrapes all the movie name data from the page, scrolling while doing so to load the dynamic page content

It then deletes any duplicate names that were scraped

Then it sorts the movie names alphabetically

The program then writes the names to a csv file in one column    (You can change the csv file name! It will create a new file if necessary)
