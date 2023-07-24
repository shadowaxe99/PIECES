```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataProcessing:
    def __init__(self):
        self.numerical_features = ['age', 'travel_frequency', 'budget']
        self.categorical_features = ['preferred_airline', 'preferred_hotel', 'preferred_seat_class', 'preferred_amenities']

        self.numerical_transformer = StandardScaler()
        self.categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.numerical_transformer, self.numerical_features),
                ('cat', self.categorical_transformer, self.categorical_features)])

    def fit_transform(self, df):
        return self.preprocessor.fit_transform(df)

    def transform(self, df):
        return self.preprocessor.transform(df)

def process_user_data(userProfile):
    data_processor = DataProcessing()
    processed_data = data_processor.fit_transform(userProfile)
    return processed_data
```