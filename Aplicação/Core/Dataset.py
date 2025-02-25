class Dataset:
    def __init__(self, dataset_id, name, target_feature, features = []):
        self.dataset_id = dataset_id
        self.name = name
        self.target_feature = target_feature
        self.features = features