from booking.bookings import Booking
import time

with Booking() as bot: 
    bot.land_first_page()
    bot.remove_banner()
    bot.change_currency("GBP")
