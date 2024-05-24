from django_seed import Seed
from rooms.models import *


def runroom():
    seed = Seed.seeder()

    # amenity = [
    #     {
    #         'titre': "2 - 5 personnes",
    #         'image': "gg-user"
    #     },
    #     {
    #         'titre': "Wi-Fi",
    #         'image': "gg-data"
    #     },
    #     {
    #         'titre': "Piscine",
    #         'image': "gg-drop"
    #     },
    #     {
    #         'titre': "Petit-déjeuner",
    #         'image': "gg-coffee"
    #     },
    #     {
    #         'titre': "Rooms SQFT",
    #         'image': "gg-home-alt"
    #     },
    #     {
    #         'titre': "Gym",
    #         'image': "gg-gym"
    #     }
    # ]

    # for item in amenity:
    #     seed.add_entity(Amenity, 1, item)

    room_data = [
        {
            'titre': "Chambre Deluxe",
            'description': "Une chambre spacieuse et confortable avec vue sur la ville.",
            'image': "images/deluxe.jpg",
            'prix': 120.00,
            'quantite': 5,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 30,
            'note': 4.5,
            'lit': 2,
            'date_in': "2022-01-01",
            'date_out': "2022-01-02",
            'remise': 10
        },
        {
            'titre': "Suite Présidentielle",
            'description': "Une suite luxueuse avec une vue imprenable.",
            'image': "images/suite.jpg",
            'prix': 200.00,
            'quantite': 2,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 50,
            'note': 4.8,
            'lit': 3,
            'date_in': "2022-01-07",
            'date_out': "2022-01-08",
            'remise': 20
        },
        {
            'titre': "Chambre Standard",
            'description': "Une chambre confortable avec toutes les commodités de base.",
            'image': "images/standard.jpg",
            'prix': 80.00,
            'quantite': 10,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 20,
            'note': 4.0,
            'lit': 1,
            'date_in': "2022-01-03",
            'date_out': "2022-01-04",
            'remise': 5
        },
        {
            'titre': "Chambre Double",
            'description': "Une chambre confortable pour deux personnes.",
            'image': "images/double.jpg",
            'prix': 90.00,
            'quantite': 7,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 25,
            'note': 4.2,
            'lit': 2,
            'date_in': "2022-01-05",
            'date_out': "2022-01-06",
            'remise': 7
        },
        {
            'titre': "Chambre Familiale",
            'description': "Une grande chambre parfaite pour les familles.",
            'image': "images/family.jpg",
            'prix': 150.00,
            'quantite': 3,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 40,
            'note': 4.7,
            'lit': 3,
            'date_in': "2022-01-05",
            'date_out': "2022-01-06",
            'remise': 15
        },
        {
            'titre': "Chambre Simple",
            'description': "Une petite chambre pour une personne.",
            'image': "images/single.jpg",
            'prix': 60.00,
            'quantite': 8,
            'amenities': [Amenity.objects.get(titre="2 - 5 personnes"),
                          Amenity.objects.get(titre="Wi-Fi"),
                          Amenity.objects.get(titre="Piscine"),
                          Amenity.objects.get(titre="Petit-déjeuner"),
                          Amenity.objects.get(titre="Rooms SQFT"),
                          Amenity.objects.get(titre="Gym")],
            'taille': 15,
            'note': 3.8,
            'lit': 1,
            'date_in': "2022-01-07",
            'date_out': "2022-01-08",
            'remise': 0
        }
    ]

    for item in room_data:
        post = Room.objects.create(
            titre = item['titre'],
            description = item['description'],
            image = item['image'],
            prix = item['prix'],
            quantite = item['quantite'],
            taille = item['taille'],
            note = item['note'],
            lit = item['lit'],
            date_in = item['date_in'],
            date_out = item['date_out'],
            remise = item['remise']
        )
        post.amenities.set(item['amenities'])
        

    seed.execute()