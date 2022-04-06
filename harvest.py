############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    Muskmelon = MelonType(
        'musk',
        '1998',
        'green',
        True,
        True,
        'Muskmelon'
    )

    Casaba = MelonType(
        'cas',
        '2003',
        'orange',
        False,
        False,
        'Casaba'
    )
    
    Crenshaw = MelonType(
        'cren',
        '1996',
        'green',
        False,
        False,
        'Crenshaw'    
    )

    Yellow_Watermelon = MelonType(
        'yw',
        '2013',
        'yellow',
        False,
        True,
        'Yellow Watermelon'
    )
    
    Casaba.add_pairing('strawberries')
    Casaba.add_pairing('mint')
    Yellow_Watermelon.add_pairing('ice cream')
    Muskmelon.add_pairing('mint')
    Crenshaw.add_pairing('prosciutto')

    all_melon_types.append(Muskmelon)
    all_melon_types.append(Casaba)
    all_melon_types.append(Crenshaw)
    all_melon_types.append(Yellow_Watermelon)
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f' {melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    reporting_codes = {}

    for melon in melon_types:
        #Muskmelon.code = key
        #Muskmelon.name = value
        reporting_codes[melon.code] = melon

    return reporting_codes
    
all_melon_types = make_melon_types()
#print_pairing_info(all_melon_types)
print(make_melon_type_lookup(all_melon_types))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester_name):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester_name = harvester_name
    
    def is_sellable(self):
        #shape AND color ratings > 5 = sellable
        #did not come from field 3 = sellable
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3
    
def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
