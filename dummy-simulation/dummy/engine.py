import numpy as np


class DummyEngine:
    def __init__(self):
        self.partitions = {}

    def add_data_partition(self, partition_id, partition):
        self.partitions[partition_id] = partition

    def run(self, queries):
        print("Evaluating query/queries...")
