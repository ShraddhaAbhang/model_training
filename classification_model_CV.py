##### EDA & Preprocessing #####
'''
1. Data
2. Labelling the data correct
3. Pre-processing the Data 
4. Image filtering (for eg. Gray Scale, Change Resolution, Other filter)
'''

##### Model Training #####
'''
1. Selection of Model type (For eg. Classification, Object Detection, Segmentation, Image Generation, etc)
2. Base Model Train 
3. Fine tunning the Model (Hyper-parameter tunning, Training for more Epochs) 
'''

##### Model Evaluation #####

'''
1. Evaluate model based on Confusion Matrix (TP, TN, FP, FN)
2. Precision, Recall, F1
'''
'''
True Positive : I have symtoms, i thik i have covid, doc report also said I m covid positive. Sure
True Negative : I though i dont have covid, and doc report also said i was not hving covid. Clear
False Positive : I thought i have covid, report of doc showed I dont have covid
False Negatiuve : I thought i dont have covid, doc said I have covid.
'''


'''
        Ground truth(Label)     Predict
        
img_1 = No                     Yes         FP
img_2 = Yes                    No          FN
img_3 = No                     No          TN
img_4 = Yes                    Yes         TP
img_5 = Yes                    Yes         TP

Accuracy = Correct Prediction / Total Prediction 
Accuracy = 3/5 = 0.6

Precision = total(TP) / total (FP + TP) 
TP/ FP + TP = 2/3 = 0.66

Recall = TP / total (TP + FN)
2 / 3 = 0.66

F1 = (0.66 * 0.66 / 0.66 + 0.66) * 2 = (0.4356 / 1.32) * 2 = 0.66
'''

'''
##### Inference #####
Run predictions on Unseen data :

when driving car or any vehical, if the car/ vehicle is self driving, and any poll comes means that triangle thing car/vehical should understand
and yess or do what ever required according to that correct sign boards but the car should reduce speed and all as well 



Recall = TP / TP + FN = 40 / 40 + 20 = 40 / 60 = 2/3 = 0.66

40 positive really positive, 20 negative, bu real positive, 10 ppl weew negative & eallt negative
30 ppl positiv in relly they were not 
'''