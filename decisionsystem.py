class AutonomousAgent:

    def __init__(self):
        self.state = {}
        self.conflicts = {"activate_cooling": ["activate_heating"],"activate_heating": ["activate_cooling"]}
        self.priorities = {
            "activate_cooling": 3,
            "reduce_activity": 2,
            "do_nothing": 0
        }
        self.last_action = None

    def observe(self, observation):
        self.state.update(observation)
        return observation

    def analyze_state(self):

        temp = self.state.get("temperature", 0)

        if temp >= 82:
            environment = "hot"

        elif temp <= 78:
            environment = "normal"

        else:
            environment = "stable"

        return {"environment": environment}
    
    def generate_options(self, state_analysis):

        env = state_analysis["environment"]

        options = []

        if env == "hot":
            options.append("activate_cooling")

        elif env == "normal":
            options.append("do_nothing")

        elif env == "stable":
            if self.last_action:
                options.append(self.last_action)

        return options
    
    def score_option(self, option):

        scores = {
            "activate_cooling": 0.9,
            "reduce_activity": 0.6,
            "do_nothing": 0.1,
        }

        return scores.get(option, 0)
    
    def resolve_conflicts(self, options):

        filtered = []

        for option in options:

            conflict_list = self.conflicts.get(option, [])

            conflict_found = False

            for existing in filtered:
                if existing in conflict_list:
                    conflict_found = True
                    break

            if not conflict_found:
                filtered.append(option)

        return filtered
    
    def choose_action(self, options):
    
        best_action = None
        best_priority = -1
        best_score = -1
    
        for option in options:
        
            priority = self.priorities.get(option, 0)
            score = self.score_option(option)
    
            if priority > best_priority:
                best_priority = priority
                best_score = score
                best_action = option
    
            elif priority == best_priority and score > best_score:
                best_score = score
                best_action = option
    
        return best_action
    
    def execute(self, action):

        self.last_action = action

        if action == "activate_cooling":
            return "Cooling system activated"

        elif action == "reduce_activity":
            return "Activity reduced"

        else:
            return "No action taken"
        
    def run_cycle(self, observation):

        observation = self.observe(observation)

        state_analysis = self.analyze_state()

        options = self.generate_options(state_analysis)

        options = self.resolve_conflicts(options)

        action = self.choose_action(options)

        result = self.execute(action)

        return result
    
agent = AutonomousAgent()

observations = [
    {"temperature": 83},
    {"temperature": 81},
    {"temperature": 80},
    {"temperature": 79},
    {"temperature": 77}
]

for observation in observations:

    result = agent.run_cycle(observation)

    print(observation, "→", result)
