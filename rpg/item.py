class Item:
    def __init__(self, name, value):
        self.name = name
        self.description = None
        self.value = value

    def set_value(self, value):
        self.name = name

    def get_value(self):
        return self.value

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def describe(self):
        print("There is %s \nIt is worth %d gold." % (self.description, self.value))
