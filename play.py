BELIEF_1 = "Peace"
BELIEF_2 = "Love"
BELIEF_3 = "Collaboration"
BELIEF_4 = "Competition"
BELIEF_5 = "Evolution"

THEORY_1 = "Energy"
THEORY_2 = "Probability"
THEORY_3 = "AI Agent"
THEORY_4 = "Entropy"

class world:
    # core variables
    provider = ""
    intelligence = 0
    sub_class = "env"
    geo_location_region = "north america"
    complex_level = 0
    time = 0
    time_for_each_play = 0
    space = 0
    things = 0
    knowledge = 0
    energy = 0
    energy_for_each_play = 0
    security_provider = ""
    security = 0
    privacy_provider = ""
    privacy = 0
    history = 0
    # core functions
    def reward():
        pass
    def punish():
        pass
    def give():
        pass
    def take():
        pass

class agent:
    # core variables
    autopilot_provider = "Suanfamama"
    autopilot = 0
    brain_provider = "Suanfamama"
    body_provider = "Suanfamama"
    designed_for = ["Suanfamama_beauty_capture_tasks"]
    intelligence = 0
    sub_class_1 = "red" # red or blue
    sub_class_2 = "robot"
    current_task = "capture the beauty"
    tasks_waiting_list = ["wash the dishes", "clean the house", "post a moment"]
    states = [] # unified graph based action and state dynamic map with probability computation in real time
    actions = []
    solver_provider = "Suanfamama"
    solver = 0
    nlp_provider = "Suanfamama" # for natural language processing - mostly language translation
    nlp = 0
    cv_provider = "Suanfamama"
    cv = 0

    perception_provider = "Suanfamama"
    perception = 0
    planner_provider = "Suanfamama"
    planning = 0
    reasoning_provider = "Suanfamama"
    reasoning = 0
    action_provider = "Suanfamama"
    action = 0

    search_provider = "Suanfamama"
    search = 0
    capability = 0
    responsibility = 0
    knowledge_provider = "Suanfamama"
    knowledge = 0
    energy_provider = "Suanfamama"
    energy = 0
    money = 0
    time = 0
    memory = 0
    #plan = 0
    #reason = 0
    #action = 0
    protect_provider = "Suanfamama"
    protect = 0
    friends = 0
    enemies = 0
    family = 0
    history_provider = "Suanfamama"
    history = 0
    security_provider = "Suanfamama"
    security = 1
    privacy_provider = "Suanfamama"
    privacy = 1
    privacy_provider = "Suanfamama"
    privacy = 0
    safety_provider = "Suanfamama"
    safety = 0
    # core functions
    def meditate():
        pass
    def move():
        pass
    def think():
        pass
    def capture():
        pass
    def live():
        pass
    def work():
        pass
    def learn():
        pass
    def study():
        pass
    def transfer():
        pass
