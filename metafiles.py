import os
from dinov2.data.datasets import ImageNet

dataroot = '/share/medical/Vault/datasets_working/GastroNet5MDino'

for split in ImageNet.Split:
    dataset = ImageNet(split=split, root=dataroot, extra='')
    dataset.dump_extra()