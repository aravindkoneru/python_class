class Car:
    def __init__(self, make, model, year, color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color


    def info(self):
        print(f"make: {self._make}, model: {self._model}, year: {self._year}, color: {self._color}")

    # getters
    def get_make(self):
        return self._make

    # setters
    def set_model(self, new_model):
        self._model = new_model




ford = Car("ford", "tundra", 2016, "red")
ford.info()

# we would call 'ford' an instance of 'Car'

ford.set_model("escape")
ford.info()
