from booking.bookings import Booking
import time

with Booking() as bot: 
    bot.land_first_page()
    bot.remove_banner()
    bot.change_currency("AED")
    bot.set_destination('Netherlands')
    bot.travel_dates('12 December 2023', '8 January 2024')
    bot.set_adults(1)
    bot.click_search_button()
    input("Press Enter to close the browser...")

    bot.quit()