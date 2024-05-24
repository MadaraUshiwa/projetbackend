from django_seed import Seed
from .models import *

def run_authentification():
    seeder = Seed.seeder()
    
    roles = [
        {
            'name' : 'administrator'
        },{
            'name' : 'webmaster'
        },{
            'name' : 'utilisateur'
        },{
            'name' : 'receptionniste'
        },{
            'name' : 'redacteur'
        }
    ]

    for item in roles:
        seeder.add_entity(Role, 1, item)
    seeder.execute()