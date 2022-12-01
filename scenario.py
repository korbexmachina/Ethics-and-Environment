class scenario:
    def __init__(self, body, option1, option2, option1_impact, option2_impact) -> None:
        """Initializes a new scenario

        Args:
            body (str): The body text for the scenario
            option1 (str): The first option
            option2 (str): The second option
            option1_impact (int): The impact that the first choice will have on the points total
            option2_impact (int): The impact that the second choice will have on the points total
        """
        self.body = body
        self.option1 = option1
        self.option2 = option2
        self.option1_impact = option1_impact
        self.option2_impact = option2_impact
    
    def __str__(self) -> None:
        """Prints the scenario, along with the options
        """
        print(self.body)
        print("---")
        print(f"{self.option1} : {self.option2}")
        
    def option1_picked(self, points) -> int:
        """Adjusts the total number of points

        Args:
            points (int): The total number of points

        Returns:
            int: the new number of points after adding option1_impact to the total
        """
        return (points + self.option1_impact)
        
    def option2_picked(self, points) -> int:
        """Adjusts the total number of points

        Args:
            points (int): The total number of points

        Returns:
            int: the new number of points after adding option2_impact to the total
        """
        return (points + self.option2_impact)