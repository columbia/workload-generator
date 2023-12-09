import numpy as np
from typing import List, Any
from wlgen.api import TaskGenerator, DataPartitionGenerator, EngineHook


class DummyTask:
    def __init__(self, id: int, query: Any, data_partitions: List[str]):
        self.id = id
        self.query = query
        self.data_partitions = data_partitions


class DummyDataPartition:
    def __init__(self, id: int, data: Any):
        self.id = id
        self.data = data


# Integrating with wlgen by implementing its abstract classes
class DummyTaskGenerator(TaskGenerator):
    def __init__(self, config):
        self.counter = 0
        self.query_pool = ["query1", "query2", "query3"]
        rng = (
            np.random.default_rng()
            if config.enable_random_seed
            else np.random.default_rng(config.global_seed)
        )

    def create_task(self):
        query = self.query_pool[self.rng.randint(0, 2)]
        task = DummyTask(self.counter, query, [0])
        self.counter += 1
        return task


class DummyDataPartitionGenerator(DataPartitionGenerator):
    def __init__(self):
        self.counter = 0

    def create_data_partition(self):
        data_partition = DummyDataPartition(self.counter, "random_data")
        self.counter += 1
        return data_partition


class DummyEngineHook(EngineHook):
    def __init__(self, dummy_engine):
        self.dummy_engine = dummy_engine

    def evaluate(self, queries: Any):
        self.dummy_engine.run(queries)

    def add_data_partition(self, partition_id, partition: Any):
        self.dummy_engine.add_data_partition(partition_id, partition)
