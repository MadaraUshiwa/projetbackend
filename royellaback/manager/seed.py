from django_seed import Seed
from manager.models import *

def runmanager():
    seed = Seed.seeder()
    manager_data = {
            'nom': "John D. Alexon",
            'poste': "Manager Général",
            'image': "images/manager.jpg",
            'citation': "Nous sommes une famille. Nous sommes un hôtel. Nous sommes un service. Nous sommes un rêve.",
        }
    
    seed.add_entity(Manager, 1, manager_data)
    seed.execute()