import sys

from src.main.deployment.execution import DockerScale
from src.main.deployment.planning import DockerPlanning
sys.path.insert(0, "./src")
def main():
    plan = DockerPlanning()
    execution = DockerScale()
    plan.attach(execution)
if __name__ == "__main__":
    main()
