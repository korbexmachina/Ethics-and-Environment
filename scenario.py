class scenario:
    def __init__(self, body, option1, option2, option1_impact, option2_impact) -> None:
        self.body = body
        self.option1 = option1
        self.option2 = option2
        self.option1_impact = option1_impact
        self.option2_impact = option2_impact
    
    def __str__(self) -> None:
        print(self.body)
        print("---")
        print(f"{self.option1} : {self.option2}")
        
    def option1_picked(self, points) -> int:
        return (points -= self.option1_impact)
        
    def option2_picked(self, points) -> int:
        return (points -= self.option2_impact)