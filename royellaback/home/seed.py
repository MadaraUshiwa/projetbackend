from home.models import *
from django_seed import Seed

def run():
    seed = Seed.seeder()
    
    banner = [{
        'titre' : 'THE BEST LUXURY HOTEL IN CALIFORNIA',
        'image' : 'images/hotel1.jpg',
        'stars' : 5
    },{
        'titre' : 'THE BEST LUXURY HOTEL IN KASHMIR',
        'image' : 'images/hotel2.jpg',
        'stars' : 5
    },{
        'titre' : 'THE BEST LUXURY HOTEL IN COLOSSEUM',
        'image' : 'images/hotel3.jpg',
        'stars' : 4
    },{
        'titre' : 'THE BEST LUXURY HOTEL IN SRILANKA',
        'image' : 'images/hotel4.avif',
        'stars' : 5
    }]
    
    for item in banner:
        seed.add_entity(Banner, 1, item)
    
    seed.execute()