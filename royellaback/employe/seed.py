from django_seed import Seed
from employe.models import *

def runemploye():
    seed = Seed.seeder()
    
    employe_data = [
        {
            "nom": "Jean",
            "poste": "Developpeur",
            "image": "images/member-1.jpg",
            "citation": "Je suis le meilleur developpeur du monde"
        },
        {
            "nom": "Paula",
            "poste": "Designer",
            "image": "images/member-2.jpg",
            "citation": "Je suis le meilleur designer du monde"
        },
        {
            "nom": "Jacques",
            "poste": "Manager",
            "image": "images/member-3.jpg",
            "citation": "Je suis le meilleur manager du monde"
        },
        {
            "nom": "Marie",
            "poste": "Developpeur",
            "image": "images/member-4.jpg",
            "citation": "Je suis la meilleure developpeuse du monde"
        },
        {
            "nom": "Sofiane",
            "poste": "Designer",
            "image": "images/member-5.jpg",
            "citation": "Je suis la meilleure designer du monde"
        },
        {
            "nom": "Julie",
            "poste": "Manager",
            "image": "images/member-6.jpg",
            "citation": "Je suis la meilleure manager du monde"
        }
    ]
    
    
    for item in employe_data:
        seed.add_entity(Employe, 1, item)
    seed.execute()