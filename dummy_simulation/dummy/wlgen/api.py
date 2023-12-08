import random

from typing import List, Any
from wlgen.api import TaskGenerator, DataPartitionGenerator, EngineHook

class DummyTask:
    def __init__(
        self,
        id: int,
        query: Any,
        data_partitions: List[str],
    ):
        self.id = id
        self.query = query
        self.data_partitions = data_partitions

class DummyDataPartition:
    def __init__(
        self,
        id: int,
        data: Any,
    ):
        self.id = id
        self.data = data

class DummyTaskGenerator(TaskGenerator):
    def __init__(self,) -> None:
        self.counter = 0
        self.query_pool = ["query1", "query2", "query3"]

    def create_task(self,):
        query = self.query_pool[random()%3]
        task = DummyTask(self.counter, 0, "some_type", query, 1, [0])
        self.counter += 1
        return task

class DummyDataPartitionGenerator(DataPartitionGenerator):
    def __init__(self,) -> None:
        self.counter = 0

    def create_data_partition(self,):
        block = DummyDataPartition(self.counter, "random_data")
        self.counter += 1
        return block
    
class DummyEngineHook(EngineHook):
    def __init__(
        self,
    ):
        pass

    def evaluate(self, query: Any):
        print("Evaluating query", query)

    def add_data_partition(self, partition: Any):
        print("Adding partition", partition)