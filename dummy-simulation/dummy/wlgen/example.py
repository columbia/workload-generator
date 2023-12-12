import typer

from pathlib import Path

from dummy.engine import DummyEngine
from dummy.wlgen.api import (
    DummyEngineHook,
    DummyTaskGenerator,
    DummyDataPartitionGenerator,
)
from wlgenlib.core import WLGen

app = typer.Typer()


@app.command()
def run_workload(
    omegaconf: str = "dummy-simulation/dummy/wlgen/config.json",
    loguru_level: str = "ERROR",
):
    # os.environ["LOGURU_LEVEL"] = loguru_level
    # os.environ["TUNE_DISABLE_AUTO_CALLBACK_LOGGERS"] = "1"

    dummy_engine = DummyEngine()

    dummy_engine_hook = DummyEngineHook(dummy_engine)
    dummy_task_generator = DummyTaskGenerator()
    dummy_data_partition_generator = DummyDataPartitionGenerator()
    WLGen(
        omegaconf,
        dummy_engine_hook,
        dummy_task_generator,
        dummy_data_partition_generator,
    ).run()


if __name__ == "__main__":
    app()
