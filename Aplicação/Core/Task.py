class Task:
    def __init__(self, task_id, name, task_type, dataset, time_frame):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type
        self.dataset = dataset
        self.time_frame = time_frame

    def execute(self, model, parameters):
        return Run(run_id=1, task=self, model=model, dataset=self.dataset, parameters=parameters)