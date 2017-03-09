class Property:
    # It`s a class that keeps/shows info about property.
    # It will be used as parent class

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        # Initiates classes variables
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        # Prints classes variables
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        # Asks user to enter info
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    # Class that subordinates to class Property
    # Also, it has a couple of public variables
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        # Initiates 2 classes variables
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        # Prints classes variables
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? "
                            "({})".format(", ".join(Apartment.valid_balconies)))
            parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    def prompt_init():
        # Asks user to enter info
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    # Class that subordinates to class Property
    # Also, it has a couple of public variables
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        # Initiates some classes variables
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        # Prints classes variables
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        # Asks user to enter info
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
    # This class will be used as parent class
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        # Initiates all classes variables
        self.price = price
        self.taxes = taxes

    def display(self):
        # Prints classes variables
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        # Asks user to enter info
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    # This is rental class.
    # It will be used as parent class
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        # Initiates all classes variables
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        # Prints classes variables
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        # Asks user to enter info
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    # Subordinates to classes Rental and House

    def prompt_init():
        # Creates variables using classes House and Rental
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    # Checks if your input is correct until it is.
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class ApartmentRental(Rental, Apartment):
    # Subordinates to classes Rental and Apartment

    def prompt_init():
        # Creates variables using classes House and Apartment
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    # Subordinates to classes Purchase and Apartment

    def prompt_init():
        # Creates variables using classes Purchase and Apartment
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    # Subordinates to classes Purchase and House

    def prompt_init():
        # Creates variables using classes House and Purchase
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    # It has a couple of public variables
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        # Initiates classes variable
        self.property_list = []

    def display_properties(self):
        # Prints classes variables
        for property in self.property_list:
            property.display()

    def add_property(self):
        # Function for adding property
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

    def display(self):
        # Prints info
        print('My name is {0}'.format(self.name))
        print('I finished {0}'.format(self.education))
        print('I\'ve been working for {0}'.format(self.experience))

    def _add_info(self):
        # Use it to add some info
        self.name = input('Enter your name: ')
        self.experience = input('Enter how long you\'ve been working(example - "2 years"): ')
        self.education = input('Enter best place you finished studying in(example - "UCU)": ')

    def get_agent_info(self):
        # Function to print info about agent
        try:
            Agent().display()
        except:
            Agent()._add_info()
            Agent().display()
