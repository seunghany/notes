# Implement a class country that represents country with a name, population and an area

class Country():
    
    def __init__(self, name: str, population: int, area: int) -> None:
        """
            Args
                name [string]: [name of the country]
                population [int]: [population of the country]
                area [int]: [area of the country]
        
        """

        self.name = name
        self.population = population
        self.area = area
        
    def larger(self, country_a, country_b) -> bool:
        """
            Recieves two country object
            Returns true if area of country A is bigger than Country B
            return country_A.area > country_B.area
        """
        return country_a > country_b

    def population_density(self) -> float:
        population_density = self.population/self.area
        return population_density

    def __str__(self):
        return "{} has a population of {} and is {} square km".format(self.name, self.population, self.area)


if __name__ == "__main__":
    canada = Country("Canada", 34482779, 9984670)
    print(canada.name)
    print(canada.population)
    print(canada.area)
    print(canada.population_density())
    print(canada)