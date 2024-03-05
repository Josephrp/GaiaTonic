# Agents Group Chat Finite State Machine
class GroupChatFSM:
    def __init__(self, teams_config):
        """
        Initialize with configurations for teams.
        """
        self.teams = {team_name: self.Team(team_agents) for team_name, team_agents in teams_config.items()}
        self.states = ["waiting", "interacting", "finalizing"]
        self.current_state = "waiting"

    def transition(self, to_state):
        """
        Transition the state of the group chat based on FSM rules.
        """
        if to_state in self.states:
            self.current_state = to_state
        else:
            raise ValueError("Invalid state transition attempted.")

    def broadcast(self, message):
        """
        Broadcast a message to all teams based on the current FSM state.
        """
        if self.current_state == "interacting":
            responses = {team_name: team.broadcast(message) for team_name, team in self.teams.items()}
            return responses
        else:
            return "The group chat is not in an interacting state."

    class Team:
        def __init__(self, agents_config):
            self.agents = [self.Agent(agent_config) for agent_config in agents_config]

        def broadcast(self, message):
            responses = [agent.respond(message) for agent in self.agents]
            return responses

        class Agent:
            def __init__(self, config):
                self.agent_name = config['agent_name']
                self.api_key = config['api_key']
                self.model = config['model']

            def respond(self, message):
                return f"{self.agent_name} responding with {self.model}"
