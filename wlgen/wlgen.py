import random
from pathlib import Path

import numpy as np
import simpy
import typer
from omegaconf import OmegaConf

from dpgen.core.tasks import Tasks
from dpgen.core.blocks import Blocks
from dpgen.core.resourcemanager import ResourceManager

REPO_ROOT = Path(__file__).parent
DEFAULT_CONFIG_FILE = REPO_ROOT.joinpath("config/config.json")

app = typer.Typer()


class DPGen:
    def __init__(self, omegaconf, dp_engine_hook):
        self.env = simpy.Environment()

        # Initialize configuration
        default_config = OmegaConf.load(DEFAULT_CONFIG_FILE)
        omegaconf = OmegaConf.create(omegaconf)
        self.config = OmegaConf.merge(default_config, omegaconf)
        # logger.info(f"Configuration: {self.config}")

        if self.config.enable_random_seed:
            random.seed(None)
            np.random.seed(None)
        else:
            random.seed(self.config.global_seed)
            np.random.seed(self.config.global_seed)

        # Start the block and tasks consumers
        self.rm = ResourceManager(self.env, dp_engine_hook, self.config)
        self.env.process(self.rm.start())

        # Start the block and tasks producers
        Blocks(self.env, self.rm)
        Tasks(self.env, self.rm)

    def run(self):
        self.env.run()



# @app.command()
# def run_simulation(
#     omegaconf: str = "turbo/config/turbo.json",
#     loguru_level: str = "ERROR",
# ):
#     os.environ["LOGURU_LEVEL"] = loguru_level
#     os.environ["TUNE_DISABLE_AUTO_CALLBACK_LOGGERS"] = "1"

#     omegaconf = OmegaConf.load(omegaconf)
#     dp_engine = DPEngine()
#     logs = Simulator(omegaconf, dp_engine).run()
#     return logs


# if __name__ == "__main__":
#     app()
