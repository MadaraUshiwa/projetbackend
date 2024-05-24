from django_seed import Seed
from hotel.models import *

def runhotel():
    seed = Seed.seeder()
    
    hotel_data = {
            'titre' : "LUXURY BEST HOTEL IN CITY CALIFORNIA, USA",
            'description' : "Niché au cœur de la vibrante Californie, notre hôtel incarne l'élégance et le raffinement. Imprégnez-vous de l'atmosphère enchanteresse de notre oasis urbaine, où chaque détail a été pensé pour vous offrir une expérience inoubliable. Réveillez-vous avec des vues panoramiques à couper le souffle depuis nos chambres et suites somptueusement aménagées.",
            'image' : "images/hotel1.jpg",
            'video' : "https://www.youtube.com/watch?v=JgHfx2v9zOU",
            'localisation' : "California, USA"
        }
        
    seed.add_entity(hotel, 1, hotel_data)
    seed.execute()
