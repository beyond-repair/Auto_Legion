# Auto_Legion/main.py
from local_model_integration import LocalModelIntegration
from superagi_integration import SuperAgiIntegration
from task_manager import TaskManager

def run_example():
    task_manager = TaskManager()
    local_model = LocalModelIntegration(model_path="/path/to/local_model.gguf")
    local_model.deploy_local_model()

    # Create and manage up to three AI agents
    for key in ["superagi_api_key1", "superagi_api_key2", "superagi_api_key3"]:
        ai_agent = task_manager.create_ai_agent(local_model, superagi_api_key=key)

    # Try to create another agent (will print a message indicating the limit is reached)
    ai_agent4 = task_manager.create_ai_agent(local_model, superagi_api_key="superagi_api_key4")

    # Destroy AI agents when tasks are completed
    for ai_agent in [ai_agent1, ai_agent2, ai_agent3]:
        task_manager.destroy_ai_agent(ai_agent)

    # Enhance: Add a message to indicate the completion of the example
    print("Example run completed successfully.")

# Enhance: Add a guard to run the example only when this script is executed directly
if __name__ == "__main__":
    run_example()
