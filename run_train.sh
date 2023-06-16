cd /share/medical/chjkusters/dinov2/

export HOME=/share/medical/chjkusters/dinov2install/
python3 setup.py install --user

#### GastroNet Implementation ###
#python3 dinov2/train/train.py \
#    --config-file dinov2/configs/train/vits16.yaml \
#    --output-dir '/share/medical/chjkusters/dinov2/output/' \
#    train.dataset_path=ImageNet:split=TRAIN:root='/share/medical/Vault/datasets_working/GastroNet5MDino':extra='/share/medical/Vault/datasets_working/GastroNet5MDino'

### ImageNet Implementation ###
python3 dinov2/train/train.py \
    --config-file dinov2/configs/train/vitl16_short.yaml \
    --output-dir '/share/medical/chjkusters/dinov2/output/' \
    train.dataset_path=ImageNet:split=TRAIN:root='/share/medical/Vault/datasets_working/Imagenet':extra='/share/medical/Vault/datasets_working/Imagenet'