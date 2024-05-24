from django_seed import Seed
from services.models import *

def runservices():
    seed = Seed.seeder()
    
    services_data = [
        {
            'theme': 'FITNESS',
            'titre': "Salle de sport",
            'description': "Une salle de sport entièrement équipée pour vous permettre de rester en forme pendant votre séjour.",
            'image': "images/fitness.jpg",
            'ordre': 1
        },
        {
           'theme': 'FITNESS',
            'titre': "Piscine",
            'description': "Profitez de notre piscine extérieure pour vous détendre et vous rafraîchir.",
            'image': "images/piscine.jpg", 
            'ordre': 2
        },
        {
            'theme': 'RESTAURANT',
            'titre': "Restaurant",
            'description': "Notre restaurant vous propose des plats savoureux et variés pour satisfaire toutes vos envies.",
            'image': "images/restaurant.jpg",
            'ordre': 3
        },
        {
            'theme': 'EXPERIENCE',
            'titre': "entrenainement de gym",
            'description': "Une salle de sport entièrement équipée pour vous permettre de rester en forme pendant votre séjour.",
            'image': "images/coach.jpg",
            'ordre': 4
        }
    ]   
    for data in services_data:
        seed.add_entity(Services, 1, data)   
    seed.execute()