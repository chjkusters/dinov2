"""IMPORT PACKAGES"""
import os
import re
import matplotlib.pyplot as plt

"""READ LOGS"""

# Specify path of logs file
file_path = os.path.join(os.getcwd(), 'output', 'logs', 'log.txt')
save_path = os.path.join(os.getcwd(), 'output')

# Read file
with open(file_path, 'r') as f:
    contents = f.readlines()

# Initialize lists for saving values
iteration, total_loss, local_crops_loss, global_crops_loss, koleo_loss, ibot_loss = [], [], [], [], [], []

# Extract useful lines
for line in contents:
    if 'helpers.py' in line:

        # Define segment start and end: Iteration
        start = 'Training '
        end = ' eta'
        iteration_val = line[line.find(start)+len(start):line.find(end)]
        iteration.append(float(re.findall('\d+', iteration_val)[0]))

        # Define segment start and end: lr
        start = 'lr:'
        end = ' wd:'
        lr_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: wd
        start = 'wd:'
        end = ' mom:'
        wd_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: mom
        start = 'mom:'
        end = ' last_layer_lr:'
        mom_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: last_layer_lr
        start = 'last_layer_lr:'
        end = ' current_batch_size:'
        last_layer_lr_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: current_batch_size
        start = 'current_batch_size:'
        end = ' total_loss:'
        batch_size_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: total_loss
        start = 'total_loss:'
        end = ' dino_local_crops_loss:'
        total_loss_val = line[line.find(start) + len(start):line.find(end)]
        total_loss.append(float(re.findall('\d+\.\d+', total_loss_val)[0]))

        # Define segment start and end: dino_local_crops_loss
        start = 'dino_local_crops_loss:'
        end = ' dino_global_crops_loss:'
        local_crops_loss_val = line[line.find(start) + len(start):line.find(end)]
        local_crops_loss.append(float(re.findall('\d+\.\d+', local_crops_loss_val)[0]))

        # Define segment start and end: dino_global_crops_loss
        start = 'dino_global_crops_loss:'
        end = ' koleo_loss:'
        global_crops_loss_val = line[line.find(start) + len(start):line.find(end)]
        global_crops_loss.append(float(re.findall('\d+\.\d+', global_crops_loss_val)[0]))

        # Define segment start and end: koleo_loss
        start = 'koleo_loss:'
        end = ' ibot_loss:'
        koleo_loss_val = line[line.find(start) + len(start):line.find(end)]
        koleo_loss.append(float(re.findall('\d+\.\d+', koleo_loss_val)[0]))

        # Define segment start and end: ibot_loss
        start = 'ibot_loss:'
        end = ' time:'
        ibot_loss_val = line[line.find(start) + len(start):line.find(end)]
        ibot_loss.append(float(re.findall('\d+\.\d+', ibot_loss_val)[0]))

        # Define segment start and end: time
        start = 'time:'
        end = ' data:'
        time_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: data
        start = 'data:'
        end = ' max mem:'
        data_val = line[line.find(start) + len(start):line.find(end)]

        # Define segment start and end: max mem
        start = 'max mem:'
        memory_val = line[line.find(start) + len(start):]

"""GENERATE LOSS PLOTS"""

# Plot for Total Loss
plt.plot(iteration, total_loss)
plt.grid()
plt.title('Total Loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.savefig(os.path.join(save_path, 'total_loss.png'))
plt.close()

# Plot for Local Crops Loss
plt.plot(iteration, local_crops_loss)
plt.grid()
plt.title('Local Crops Loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.savefig(os.path.join(save_path, 'local_crops_loss.png'))
plt.close()

# Plot for Global Crops Loss
plt.plot(iteration, global_crops_loss)
plt.grid()
plt.title('Global Crops Loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.savefig(os.path.join(save_path, 'global_crops_loss.png'))
plt.close()

# Plot for Koleo Loss
plt.plot(iteration, koleo_loss)
plt.grid()
plt.title('Koleo Loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.savefig(os.path.join(save_path, 'koleo_loss.png'))
plt.close()

# Plot for IBot Loss
plt.plot(iteration, ibot_loss)
plt.grid()
plt.title('IBot Loss')
plt.ylabel('Loss')
plt.xlabel('Iteration')
plt.savefig(os.path.join(save_path, 'ibot_loss.png'))
plt.close()

