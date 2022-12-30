import json

class Individual:
    __slots__ = ('chromosome', 'fitness')

    def __init__(self, chromosome=None, fitness=None) -> None:
        self.chromosome = chromosome
        self.fitness = fitness

    @staticmethod
    def from_json(json_str: str) -> 'Individual':
        print(f"Parsing json: {json_str}")
        return json.loads(json_str)

    @staticmethod
    def from_dict(obj: dict[str]) -> 'Individual':
        return Individual(obj['chromosome'], obj['fitness'])
