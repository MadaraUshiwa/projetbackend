from testimonial.models import *
from django_seed import Seed

def runtestimonial():
    seed = Seed.seeder()
    
    testimonial_data = [
            {
                "nom": "Jean",
                "note": 5,
                "image": "images/member-1.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            },
            {
                "nom": "Paula",
                "note": 4,
                "image": "images/member-2.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            },
            {
                "nom": "Jacques",
                "note": 3,
                "image": "images/member-3.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            },
            {
                "nom": "Marie",
                "note": 5,
                "image": "images/member-4.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            },
            {
                "nom": "Sofiane",
                "note": 4,
                "image": "images/member-5.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            },
            {
                "nom": "Julie",
                "note": 3,
                "image": "images/member-6.jpg",
                "testimon": "Super hotel, je recommande",
                "ville": "Paris",
                "pays": "France"
            }
        ]
    for item in testimonial_data:
        seed.add_entity(Testimonial, 1, item)
    seed.execute()