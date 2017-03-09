class AcademicBuilding:
    # Academic building with address and equipment

    def __init__(self, address, classrooms):
        # Initialises address and all the classrooms
        self.address = address
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
