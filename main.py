from booking.bookings import Booking
import time

with Booking() as bot: 
    bot.land_first_page()
    bot.remove_banner()
    # bot.change_currency("USD")
    bot.set_destination('Monaco')
    bot.travel_dates('12 December 2023', '8 January 2024')
    bot.set_adults(1)
    bot.click_search_button()
    # bot.apply_filtration(3,4,5)
    bot.sort_results()
    # A workaround so that our bot can collect the updated data
    bot.refresh()
    bot.report()
    input("Press Enter to close the browser...")

    bot.quit()