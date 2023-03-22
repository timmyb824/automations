from pyinfra.operations import server
from pyinfra import host
from pyinfra.facts.files import Directory
from pyinfra.api.exceptions import DeployError
from pyinfra.api.deploy import deploy

nvmVersion = "0.39.2"
nodeVersion = "node"
userName = os.environ['SSH_USER']

@deploy("Deploy node with nvm")
def deploy_node():
    if host.get_fact(Directory, path=f"/home/{userName}/.nvm") is not None:
        raise DeployError(
            (
                "nvm already exists on this machine"
            ),
        )
    server.shell(
        name="Install node version manager",
        commands=[
            f"curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v{nvmVersion}/install.sh | bash"
        ],
    )

    server.shell(
        name="Install node latest",
        commands=[
            f"bash -c '. ~/.nvm/nvm.sh && nvm install {nodeVersion} && nvm use {nodeVersion}'"
        ],
    )