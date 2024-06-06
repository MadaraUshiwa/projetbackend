from faq.models import *
from django_seed import Seed

def runfaq():
    seed = Seed.seeder()

    faqs = [
        {
            'question': "How to Booking a Room?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "What kinds of Bedroom available?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "Do you have any Discount Current Month?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "Have you available money back Guarantee?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "Do you have any Discount Current Month?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "How to Booking a Room?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "What kinds of Bedroom available?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },

        {
            'question': "Have you available money back Gaurentee?",
            'response': "Credibly morph resource maximizing applications rather than fully test metrics via intermandated expertise. Globally administrate reliable platfor Globally brand seamless systems",
            'active': False,
        },
    ];
    
    for item in faqs:
        seed.add_entity(Faq, 1, item)
    
    
    seed.execute()