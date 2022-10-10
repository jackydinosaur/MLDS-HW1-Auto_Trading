# MLDS-HW1-Auto_Trading

## Environment setup
1.Use the Anaconda
```bash
conda create -n HW1 python=3.9
conda activate HW1
```
2.This code has been tested on Ubuntu 18.04, Python 3.9.13. 
Please install related libraries before running this code: 
```bash
pip install -r requirements.txt
```


## Data Preparation
Put the training_data and testing_data in ./. It should look like:
 ```
   ${HW1_ROOT}
    training_data.csv
    testing_data.csv
    ...
  ```   
  
## Usage
### Train models for predicting trend of stock the next day.
```sh
python trader.py --training training_data.csv -- testing testing_data.csv --output output.csv
```
### Calculate profit
```sh
# python profit_calculator.py [-h] stock action
python profit_calculator.py  ./testing_data.csv  ./output.csv
```
