# Auto_Legion/task_manager.py
class TaskManager:
    def __init__(self):
        self.ai_agents = []

    def create_ai_agent(self, local_model, superagi_api_key):
        ai_agent = local_model.create_ai_agent(superagi_api_key)
        if ai_agent:
            self.add_ai_agent(ai_agent)
        return ai_agent

    def destroy_ai_agent(self, ai_agent):
        self.remove_ai_agent(ai_agent)

    def add_ai_agent(self, ai_agent):
        self.ai_agents.append(ai_agent)

    def remove_ai_agent(self, ai_agent):
        self.ai_agents.remove(ai_agent)
