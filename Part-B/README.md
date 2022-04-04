# PartB

Git clone the whole repo cs6910_assignment2 for it to function

please pip install the packages required.

```
#from the parent directory
python -m pip install -r requirements.txt
```

Place the Inaturalist Dataset in the parent folder. 

to run the code, transferLearning.py does not sweep, values are hardcoded 
```
python transferLearning.py
```


Following is the sweep parameters used in transferLearning.ipynb file. you can use the colab [link](https://colab.research.google.com/drive/1bFKf4cjHT0EoXD-2Z_7SgleythTpac5W?authuser=1#scrollTo=GjxdxEnsZU2y)

```
sweepMethod ='bayes' #['grid','bayes','random']

if isSweep:

  sweepConfig = {'name': sweepMethod + '-PartB-fine-tuning-sweep',
                'method': sweepMethod,
                'metric' : {'name': 'val_acc', 
                            'goal': 'maximize'}
                }

  parameters = {
      
      'modelName'  : {'values': ['ResNet50','InceptionV3','Xception','InceptionResNetV2']},
      'denseSize'  : {'values': [64,128]},
      'num_epochs' : {'values': [4,8]},
      'dropOut'    : {'values': [0.2,0.4]},
      'batchNorm'  : {'values': [0,1]},
      'isDataAug'  : {'values': [0,1]},
      'optimizer'  : {'values': ['adam']},
  }

  sweepConfig['parameters'] = parameters
  sweepID = wandb.sweep(sweepConfig, project="cs6910_assignment2", entity="cs6910_assignment")
```




