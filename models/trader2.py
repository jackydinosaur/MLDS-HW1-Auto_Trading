import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
import joblib

class Trader:

    def train(self, df):

        df.columns = ['open', 'high', 'low', 'close']
        df['target'] = np.where(df['open'].shift(-1) > df['open'], 1, 0)
        features = df[['open', 'high', 'low', 'close']]
        target = df['target']

        scaler = StandardScaler()
        features = scaler.fit_transform(features)

        x_train, x_valid, y_train, y_valid = train_test_split(
            features, target, test_size=0.1, random_state=2022)

        models = SVC(kernel='poly', probability=True)
        models.fit(x_train, y_train)
        print(f'{models} : ')
        print('Training Accuracy : ', metrics.roc_auc_score(
            y_train, models.predict(x_train)))
        print('Validation Accuracy : ', metrics.roc_auc_score(
            y_valid, models.predict(x_valid)))

        predict = pd.DataFrame(models.predict(x_valid))
        predict.to_csv('output_train.csv', index=False, header=False, encoding='utf-8_sig')

        print("training_R^2 = {:.3f}".format(models.score(x_train, y_train)))
        print("testing_R^2 = {:.3f}".format(models.score(x_valid, y_valid)))

        joblib.dump(models, 'trader2.pkl')

    def predict_action(self, day, df_row, position):
        # load trained_model for predict
        df_row = df_row.reshape(1, -1)
        trader1 = joblib.load('trader2.pkl')
        predict = trader1.predict(df_row)[0].tolist()

        day = day + 1

        if position<-1 or position >1:
            print('day =', day)
            print('predict =', predict)
            print('position =', position)

        # action with predicted result
        if day == 1:
            if predict == 0:
                action = 1
                position += 1
            else:
                action = 1
                position += 1
            return str(action), position
        else:
            if position == 1:
                if predict == 1:
                    action = 0
                    position = position
                else:
                    action = -1
                    position -= 1
            elif position == -1:
                if predict == 1:
                    action = 1
                    position += 1
                else:
                    action = 0
                    position = position
            else:
                if predict == 0:
                    action = -1
                    position -= 1
                else:
                    action = 1
                    position += 1

            return str(action), position

