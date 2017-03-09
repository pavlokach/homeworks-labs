from classroom import Classroom


class Building:
    # Parent class for House and AcademicBuilding
    def __init__(self, address):
        # Initialises address
        self.address = address


class House(Building):
    # House with address and apartments

    def __init__(self, address, apartments):
        # Initialises address from class Building
        super().__init__(address)
        self.apartments = apartments


class AcademicBuilding(Building):
    # Academic building with address and equipment

    def __init__(self, address, classrooms):
        # Initialises equipment and address from class Building
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        # Sums equipment from all the classrooms
        out = []
        all_equipment = {}
        for room in self.classrooms:
            for element in room.equipment:
                if element not in all_equipment:
                    all_equipment[element] = 1
                else:
                    all_equipment[element] += 1
        for key in all_equipment:
            out.append((key, all_equipment[key]))
        return sorted(out)

    def __str__(self):
        # Displays address and info about classrooms
        print(self.address)
        for room in self.classrooms:
            print(room)
        return ''


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
