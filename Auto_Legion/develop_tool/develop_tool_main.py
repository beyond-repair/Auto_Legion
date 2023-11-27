# Auto_Legion/develop_tool/main.py
from task_manager import TaskManager
from local_model_integration import LocalModelIntegration
from superagi_integration import SuperAgiIntegration
from develop_tool.develop_tool import WriteTestTool
from config import Config  # Import the configuration

def run_example():
    # Create and manage up to three AI agents
    task_manager = TaskManager()
    local_model = LocalModelIntegration(model_path=Config.MODEL_PATH)
    local_model.deploy_local_model()

    # Initialize agents and version control integration
    github_details = {
        'repo_owner': "your_username",
        'repo_name': "your_repository",
        'token': "your_github_token"
    }

    version_control_agent = VersionControlAgent(repository_path="/path/to/your/repository")
    version_control_integration = VersionControlIntegration(version_control_agent)

    ai_agents = create_and_manage_ai_agents(task_manager, local_model, Config.SUPERAGI_API_KEYS)

    # Try to create another agent (will print a message indicating the limit is reached)
    ai_agent4 = task_manager.create_ai_agent(local_model, superagi_api_key="superagi_api_key4")

    # Destroy AI agents when tasks are completed
    destroy_ai_agents(task_manager, ai_agents)

    # Enhance: Add a message to indicate the completion of the example
    print("Example run completed successfully.")
