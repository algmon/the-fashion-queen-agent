BELIEF_1 = "Peace"
BELIEF_2 = "Love"
BELIEF_3 = "Collaboration"
BELIEF_4 = "Competition"
BELIEF_5 = "Evolution"

THEORY_1 = "Energy"
THEORY_2 = "Probability"
THEORY_3 = "AI Agent"
THEORY_4 = "Entropy"

class World:
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

class Agent:
    # core variables
    def __init__(self):
        self.autopilot_provider = "Suanfamama"
        self.autopilot = 0
        self.brain_provider = "Suanfamama"
        self.body_provider = "Suanfamama"
        self.designed_for = ["Suanfamama_beauty_capture_tasks"]
        self.intelligence = 0
        self.sub_class_1 = "red" # red or blue
        self.sub_class_2 = "robot"
        self.current_task = "capture the beauty"
        self.tasks_waiting_list = ["wash the dishes", "clean the house", "post a moment"]
        self.states = [] # unified graph based action and state dynamic map with probability computation in real time
        self.actions = []
        self.solver_provider = "Suanfamama"
        self.solver = 0
        self.nlp_provider = "Suanfamama" # for natural language processing - mostly language translation
        self.nlp = 0
        self.cv_provider = "Suanfamama"
        self.cv = 0
        self.perception_provider = "Suanfamama"
        self.perception = 0
        self.planner_provider = "Suanfamama"
        self.planning = 0
        self.reasoning_provider = "Suanfamama"
        self.reasoning = 0
        self.action_provider = "Suanfamama"
        self.action = 0
        self.search_provider = "Suanfamama"
        self.search = 0
        self.capability = 0
        self.responsibility = 0
        self.knowledge_provider = "Suanfamama"
        self.knowledge = 0
        self.energy_provider = "Suanfamama"
        self.energy = 0
        self.money_provider = "Suanfamama"
        self.money = 0
        self.time_provider = "Suanfamama"
        self.time = 0
        self.memory_provider = "Suanfamama"
        self.memory = 0
        self.protect_provider = "Suanfamama"
        self.protect = 0
        self.friends = 0
        self.enemies = 0
        self.family = 0
        self.history_provider = "Suanfamama"
        self.history = 0
        self.security_provider = "Suanfamama"
        self.security = 1
        self.privacy_provider = "Suanfamama"
        self.privacy = 0
        self.safety_provider = "Suanfamama"
        self.safety = 0

    # core functions
    def meditate(self):
        pass

    def move(self):
        pass

    def think(self):
        pass

    def capture(self):
        pass

    def live(self):
        pass

    def work(self):
        pass

    def learn(self):
        pass

    def study(self):
        pass

    def transfer(self):
        pass

    def distill(self):
        pass

class FashionAgent(Agent):
    pass

class EducationAgent(Agent):
    pass
