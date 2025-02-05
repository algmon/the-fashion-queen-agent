BELIEF_1 = "Peace"
BELIEF_2 = "Love"
BELIEF_3 = "Collaboration"
BELIEF_4 = "Competition"
BELIEF_5 = "Evolution"

THEORY_1 = "Energy"
THEORY_2 = "Probability"
THEORY_3 = "AI Agent"
THEORY_4 = "Entropy"

class Env:
    # core variables
    def __init__(self):
        self.provider = ""
        self.intelligence = 0
        self.sub_class = "env"
        self.geo_location_region = "north america"
        self.complex_level = 0
        self.time = 0
        self.time_for_each_play = 0
        self.space = 0
        self.things = 0
        self.knowledge = 0
        self.energy = 0
        self.energy_for_each_play = 0
        self.security_provider = ""
        self.security = 0
        self.privacy_provider = ""
        self.privacy = 0
        self.history = 0

    # core functions
    def reward(self):
        pass

    def punish(self):
        pass

    def give(self):
        pass

    def take(self):
        pass
