from booking.bookings import Booking
import time

with Booking() as bot: 
    bot.land_first_page()
    bot.remove_banner()
    bot.change_currency("USD")
    bot.set_destination('New York')
    bot.travel_dates('12 December 2023', '8 January 2024')
    bot.set_travellers(5)
