import django
django.setup()

from home.seed import *
from rooms.seed import *
from hotel.seed import *
from services.seed import *
from manager.seed import *
from employe.seed import *
from contact.seed import *
from testimonial.seed import *
from authentification.seed import *

if __name__ == '__main__':
    # run()
    # runroom()
    # runhotel()
    # runservices()
    # runmanager()
    # run_contact()
    # runtestimonial()
    run_authentification()