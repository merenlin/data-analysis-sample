""" Utilities methods used all over the project."""
import random

def get_halo():
    """Get a halo."""
    halos = ['Halo 1',
             'Halo: Spartan Assault',
             'Halo Wars',
             'Halo 2']
    return random.choice(halos)
