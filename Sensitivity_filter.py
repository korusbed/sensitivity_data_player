#!/usr/bin/env python
# coding: utf-8



import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



node_ui_mapping = {1:1, 2:2, 3:3, 4:4, 5:7, 6:8, 7:9, 8:10, 9:13, 10:14, 11:15, 12:16, 13:19, 14:20, 15:21, 16:22, 
                   17:25, 18:26, 19:27, 20:28, 21:31, 22:32, 23:33, 24:34, 25:37, 26:38, 27:39, 28:40}


# input parameters which depend on the mattress size
# length*width = no. of nodes
length = 7
width = 4


fsr_list = []
# Opening JSON file
f = open('modified_face_left.json')
# f = open('fake_data_3.json')
# returns JSON object as a dictionary
data = json.load(f)


max_fsr = float('-inf')
min_fsr = float('inf')



for j in range(1,length*width + 1):
    l_node = []
    for i in range(len(data)):
        if data[i]['num'] == node_ui_mapping[j]:
            l = []
            for fsr_value in data[i]['fsr']:
                l.append(fsr_value)
            node = np.array(l)
            # finding the maximum and minimum fsr values to adjust the sensitivity
            max_value = np.amax(node) 
            min_value = np.amin(node)
            if max_value > max_fsr:
                max_fsr = max_value
            if min_value < min_fsr:
                min_fsr = min_value
            node = node.reshape((6,6))
            l_node.append(node)
    
    fsr_list.append(l_node)

print(max_fsr)
print(min_fsr)

min_length = len(min(fsr_list, key = len))
# print(min_length)
# condition to check if all the node data is present in the JSON file
if min_length == 0:
    print('Data of all the nodes is not uploaded in the JSON file')
else:
    for k in range(10):
        gs = gridspec.GridSpec(length, width, wspace=0.05, hspace=0.025, top=0.95, bottom=0.05, left=0.17, right=0.5) 
        for i in range(length):
            for j in range(width):
                ax= plt.subplot(gs[i,j])
        #         im = ax.imshow(fsr_list[i*4 + j][0] ,cmap=blue_red1, interpolation = "none",vmin = 140, vmax = 200)
                ax = sns.heatmap(fsr_list[i*width + j][k], linewidths=1, vmin = min_fsr, vmax= max_fsr ,
                                 cmap='jet', cbar=False)
                ax.axis('off')
        #plt.tight_layout() # do not use this!!
        plt.savefig('data_player_images/face_left{}.png'.format(k))
        plt.show()





