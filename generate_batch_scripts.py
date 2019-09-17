import os
import itertools
import glob
import json


model_index = [0,1,2]
generator_index = [0,1]
low_shot_n = [1,2,5,10,20]
experiment_id = [1,2,3,4,5]
index = 0


for prod in itertools.product(model_index, generator_index, low_shot_n, experiment_id):
   listing = glob.glob('lowshot_results/*fileid_' + str(index) + '.json')
   print('model index', prod[0], ' gen index', prod[1], ' low shot n', prod[2], ' exp id', prod[3])
   for filename in listing:
       os.rename(filename, 'lowshot_results/ResNet10_sgm_lr_1.000_wd_0.001_expid_' + str(prod[3]) + '_lowshotn_' + str(prod[2]) + '_maxgen_5_' + 'g_type' + str(prod[1]) + '_mind_'+ str(prod[0]) + '.json')
   index += 1 

   


