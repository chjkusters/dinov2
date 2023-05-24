import os
from dinov2.data.datasets import ImageNet

# Specify dataroot
dataroot = '/share/medical/Vault/datasets_working/GastroNet5MDino'

# Create labels.txt file in dataroot
with open(os.path.join(dataroot, 'labels.txt'), 'w') as f:
    for root, dirs, files in os.walk(dataroot):
        for dir in dirs:
            if dir != 'train' and dir != 'val' and dir != 'test':
                f.write('{},{}\n'.format(dir, dir))

for split in ImageNet.Split:
    if 'TRAIN' in '{}'.format(split):
        dataset = ImageNet(split=split, root=dataroot, extra=dataroot)
        dataset.dump_extra()