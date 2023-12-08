import numpy as np

class DummyEngine:
    def __init__(self):
        self.partitions = {}
        self.dummy_budget_accountant = {}

    def add_data_partition(self, partition_id):
        self.partitions[partition_id] = np.array(1000)
        self.dummy_budget_accountant[partition_id] = 10

    def evaluate(self, queries):
        "Evaluating query/queries..."


def main():

    engine = DummyEngine()
    engine.add_partition(0)

    # task = Task(0, "linear", None, 1, ["0"])
    # dp_engine.evaluate(task)


if __name__ == "__main__":
    main()
