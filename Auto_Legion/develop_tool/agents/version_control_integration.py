# Auto_Legion/develop_tool/agents/version_control_integration.py
class VersionControlIntegration:
    def __init__(self, version_control_agent):
        self.version_control_agent = version_control_agent

    def initialize_repository(self):
        self.version_control_agent.initialize_repository()

    def create_branch(self, branch_name):
        self.version_control_agent.create_branch(branch_name)

    def switch_branch(self, branch_name):
        self.version_control_agent.switch_branch(branch_name)

    def commit_changes(self, message):
        self.version_control_agent.commit_changes(message)

