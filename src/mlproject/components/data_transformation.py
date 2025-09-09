import os 
from mlproject import logger 
from sklearn.model_selection import train_test_split
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from mlproject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def preprocessing(self):

        df = pd.read_csv(self.config.data_path)
        df = df.drop(columns=['customerID'])
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# label encoding
        le = LabelEncoder()
        columns_to_encode = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']

        for col in columns_to_encode:
            df[col] = le.fit_transform(df[col])

# one hot encoding

        columns_to_onehot = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']

        for col in columns_to_onehot:
 
            df = pd.get_dummies(df, columns=[col], prefix=col, drop_first=False)

# ensuring all data is numerical 
        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info('Splitted the data into training and test sets')
        logger.info('train.shape')
        logger.info('test.shape')

        print(train.shape)
        print(test.shape)