class Cat:
    def __init__(self, id, name, colour):
        self.id = id
        self.name = name
        self.colour = colour

    def __str__(self):
        return f"id = {self.id}, name = {self.name}, colour = {self.colour}"

    def to_json(self):
        return "{\"id\" = " + str(self.id) + ", \"name\" = \"" + str(self.name) + "\", \"colour\" = \"" + str(self.colour) + "\"}"
