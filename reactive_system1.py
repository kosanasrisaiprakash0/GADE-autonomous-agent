class AutonomousAgent:
    def __init__(self):
        self.state = {}
        self.memory = []

    def observe(self, observation):
        return observation

    def update_state(self, observation):
        self.state["cycle_count"] += 1
        self.memory.append(observation)

    def decide(self):
        return {"action": "log_only"}

    def act(self, decision):
        print(decision)

    def run_cycle(self, observation):
        obs = self.observe(observation)
        self.update_state(obs)
        decision = self.decide()
        self.act(decision)

agent = AutonomousAgent(config={"max_memory": 5})

observations = [
    {"metric": 10},
    {"metric": 20},
    {"metric": 30}
]

for obs in observations:
    agent.run_cycle(obs)

print(agent.get_state_snapshot())
print(agent.get_memory_snapshot())

#If we run 5 agents simultaneously in different threads,
#what architectural concern appears first in this design?