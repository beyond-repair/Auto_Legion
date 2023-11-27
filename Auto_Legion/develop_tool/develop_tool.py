# Auto_Legion/develop_tool/develop_tool.py
from task_manager import TaskManager
from local_model_integration import LocalModelIntegration
from develop_tool.develop_tool import create_and_manage_ai_agents, destroy_ai_agents
from develop_tool.agents.version_control_agent import VersionControlAgent
from develop_tool.agents.version_control_integration import VersionControlIntegration

def run_example():
    # Create and manage up to three AI agents
    task_manager = TaskManager()
    local_model = LocalModelIntegration(model_path="/path/to/local_model.gguf")
    local_model.deploy_local_model()

    # Initialize agents and version control integration
    github_details = {
        'repo_owner': "your_username",
        'repo_name': "your_repository",
        'token': "your_github_token"
    }

    version_control_agent = VersionControlAgent(repository_path="/path/to/your/repository")
    version_control_integration = VersionControlIntegration(version_control_agent)

    ai_agents = create_and_manage_ai_agents(task_manager, local_model, ["superagi_api_key1", "superagi_api_key2", "superagi_api_key3"])

    # Try to create another agent (will print a message indicating the limit is reached)
    ai_agent4 = task_manager.create_ai_agent(local_model, superagi_api_key="superagi_api_key4")

    # Destroy AI agents when tasks are completed
    destroy_ai_agents(task_manager, ai_agents)

    # Enhance: Add a message to indicate the completion of the example
    print("Example run completed successfully.")
