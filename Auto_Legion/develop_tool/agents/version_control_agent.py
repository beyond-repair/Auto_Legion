# Auto_Legion/develop_tool/agents/version_control_agent.py
import subprocess

class VersionControlAgent:
    def __init__(self, repository_path):
        """
        Initializes a VersionControlAgent with the specified repository path.
        :param repository_path: The path to the repository on which version control operations will be performed.
        """
        self.repository_path = repository_path

    def _run_git_command(self, command, *args):
        """
        Helper method to run Git commands.
        :param command: The Git command to be executed.
        :param args: Additional arguments for the Git command.
        """
        try:
            subprocess.run(['git', command, *args], cwd=self.repository_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error with git {command}: {e}")

    def initialize_repository(self):
        """Initializes a new Git repository."""
        self._run_git_command('init')

    def create_branch(self, branch_name):
        """Creates a new Git branch."""
        self._run_git_command('branch', branch_name)

    def switch_branch(self, branch_name):
        """Switches to the specified Git branch."""
        self._run_git_command('checkout', branch_name)

    def commit_changes(self, message):
        """
        Commits changes to the Git repository.
        :param message: The commit message.
        """
        self._run_git_command('add', '.')
        self._run_git_command('commit', '-m', message)
