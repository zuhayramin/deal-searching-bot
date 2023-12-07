from booking.bookings import Booking

with Booking() as bot: 
    bot.land_first_page()
    print('Exiting...')