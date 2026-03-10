class AutonomousAgent:
    def __init__(self, config=None):
        self._config = config or {}
        
        # Private state
        self._state = {
            "cycle_count": 0,
            "status": "initialized"
        }
        
        # Controlled memory store
        self._memory = []
        self._max_memory = self._config.get("max_memory", 100)
        
        self._running = False

    # ----------------------------
    # PUBLIC INTERFACE
    # ----------------------------
    
    def run_cycle(self, observation):
        try:
            self._log("---- New Cycle ----")
            
            processed_obs = self._observe(observation)
            self._update_state(processed_obs)
            decision = self._decide()
            self._act(decision)
            
            self._log(f"Cycle completed successfully.")
        
        except Exception as e:
            self._log(f"Cycle failed: {str(e)}")
    
    def get_state_snapshot(self):
        return self._state.copy()
    
    def get_memory_snapshot(self):
        return list(self._memory)

    # ----------------------------
    # INTERNAL PIPELINE
    # ----------------------------

    def _observe(self, observation):
        if not isinstance(observation, dict):
            raise ValueError("Observation must be a dictionary.")
        return observation

    def _update_state(self, observation):
        self._state["cycle_count"] += 1
        self._state["status"] = "active"
        
        record = {
            "cycle": self._state["cycle_count"],
            "observation": observation
        }
        
        self._store_memory(record)

    def _decide(self):
        # Placeholder deterministic decision
        decision = {
            "action": "noop",
            "reason": "Week 1 placeholder decision"
        }
        return decision

    def _act(self, decision):
        self._log(f"Action: {decision['action']}")
        self._log(f"Reason: {decision['reason']}")

    # ----------------------------
    # MEMORY CONTROL
    # ----------------------------

    def _store_memory(self, record):
        if len(self._memory) >= self._max_memory:
            self._memory.pop(0)
        self._memory.append(record)

    # ----------------------------
    # LOGGING
    # ----------------------------

    def _log(self, message):
        print(message)

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