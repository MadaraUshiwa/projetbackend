from contact.models import *
from django_seed import Seed

def run_contact():
    seed = Seed.seeder()
    
    # contact = {
    #     'tel' : '+32 489 (00) 00',
    #     'email' : 'info@uzumi.be',
    #     'location' : 'Wemmel - Belgique - 1780',
    #     'maps' : 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387190.279909073!2d-74.25987368715491!3d40.69767006458873!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sbd!4v1633418400558!5m2!1sen!2sbd'
    # }
    
    # seed.add_entity(Contact, 1, contact)
    
    images = [
        {'image' : 'images/hotel1.jpg' },
        {'image' : 'images/hotel2.jpg' },
        {'image' : 'images/hotel3.jpg' },
        {'image' : 'images/hotel4.jpg' },
        {'image' : 'images/hoteltest.jpg' },
        {'image' : 'images/restaurant.jpg' },
        {'image' : 'images/single.jpg' },
        {'image' : 'images/suite.jpg' },
        {'image' : 'images/family.jpg' }
    ]
    
    for item in images :
        seed.add_entity(Images, 1, item)
    
    seed.execute()