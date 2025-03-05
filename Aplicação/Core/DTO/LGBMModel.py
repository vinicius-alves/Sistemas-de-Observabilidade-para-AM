from .Model import Model 
import lightgbm as lgb
from .Dataset import Dataset

class LGBMModel(Model):

    def set_parameters(self):
        pass
    
    def fit(self,data: Dataset):

        d_train = lgb.Dataset(data.df, label=data.targetFeature)
        params = {
            'objective': 'binary',  # Classificação binária
            'metric': 'binary_error',
            'boosting_type': 'gbdt',
            'learning_rate': 0.1,
            'num_leaves': 31,
            'verbose': -1
        }
        self.clf = lgb.train( params = params,train_set = d_train)

    def predict(self, data: Dataset):
        y_pred_proba = self.predict_proba(data)
        return [1 if prob > 0.5 else 0 for prob in y_pred_proba]

    def predict_proba(self, data: Dataset):
        return self.clf.predict(data.df)