def get_valid_input(input_string, valid_options):
    """
    Input function which loops until option from valid_options is entered.
    :param input_string: str
    :param valid_options: tuple
    :return: str
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """ Class for property representation """

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Initialise class Property by it's area (square_feet), ammounts of beds, baths, and some optional
        arguements for future inheritance.
        :param square_feet: str
        :param beds: str
        :param baths: str
        :param kwargs: because we will be using this class in inheritance
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Output string representation of Property class.
        :return: NoneType
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}:".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Return a dictionary by user input to initialise class Property.
        :return: dict
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """ Class representation of apartment """

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solitarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialise class Apartment by state and presence of balcony and laundry, and by optional elements in case of
        future inheritance.
        :param balcony: str
        :param laundry: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Output string representation of Apartment class.
        :return: NoneType
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print()

    def prompt_init():
        """
        Create dictionary by user input for initialising Apartment class.
        :return: dict
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries
        )
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies
        )
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """ Class representation of a house """

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        Initialise House class by number of its stories, presence and state of garage, by if it is fenced
        or not, and by optional arguements in case of future inheritance.
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Output string representation of a House class.
        :return: NoneType
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
        print()

    def prompt_init():
        """
        Create a dictionary by user input for initialising House class.
        :return: dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    """ Class representation of a purchase """

    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialise class Purchase by the price of a purchase, taxes, and by optional arguements in
        case of future inheritance.
        :param price: str
        :param taxes: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Output string representation of a class Purchase.
        :return: NoneType
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
        print()

    def prompt_init():
        """
        Create a dictinary by user input for initialisation of a Purchase class.
        :return: dict
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? ")
        )
    prompt_init = staticmethod(prompt_init)


class Rental:
    """ Class representation of a rental of the property """

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        """
        Initialise Rental class by if it is furnished, its utilities, rent ammount, and optinal arguements for
        furure inheritance.
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Output string representation of a class Rental.
        :return: NoneType
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))
        print()

    def prompt_init():
        """
        Create a dictionary by user input for initialising class Rental.
        :return: dict
        """
        return dict(
            rent=input("What is the monthy rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """ Class for representation of a house rental """

    def prompt_init():
        """
        Create a dictionary by user input for initialising class HouseRental.
        :return: dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """ Class for representation of rental of an apartment """
    def prompt_init():
        """
        Create a dictionary by user input for initialising the class ApartmentRental
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """ Class for representation of purchase of an apartment """

    def prompt_init():
        """
        Create a dictionary by user input for initialising class ApartmentPurchase.
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """ Class representation of purchase of a house """

    def prompt_init():
        """
        Create a dictionary by user input for initialising class HousePurchase.
        :return: dict
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """ Class for representation of a manager of the property """
    def __init__(self):
        """ Initialise Agent class with zero property after initialisation """
        self.property_list = []

    def display_properties(self):
        """
        Output string representations of all the properties of the Agent.
        :return: NoneType
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Add property to all property of the Agent by entering if it is house or apartment and if it is for
        purchase or for rental
        :return: NoneType
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def clear_property(self):
        """
        Clear property of the Agent.
        :return: NoneType
        """
        self.property_list = []

    def display_chosen_properties(self, *args):
        """
        Display properties of given type or types of properties. If there is one arguement exept self, the
        method will print all properties with the arguement (in example, "house"). If there are two arguements,
        method will print all properties with BOTH arguements at the same time. If there are more arguements,
        method will return properties with ANY of those arguements.
        :return: NoneType
        """
        all_types = ["house", "apartment", "purchase", "rental"]
        chosen_types = []

        if len(args) == 1 or len(args) > 3:
            for arg_1 in args:
                for type_1 in all_types:
                    if tuple([arg_1, type_1]) in self.type_map.keys():
                        chosen_types.append(self.type_map[(arg_1, type_1)])
            for property_1 in self.property_list:
                for type_1 in chosen_types:
                    if isinstance(property_1, type_1):
                        property_1.display()
        elif len(args) == 2:
            if args in self.type_map.keys():
                chosen_types.append(self.type_map[(args[0], args[1])])
            for property_1 in self.property_list:
                for type_1 in chosen_types:
                    if isinstance(property_1, type_1):
                        property_1.display()
