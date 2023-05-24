cd /share/medical/chjkusters/dinov2/run/train/

python3 train.py \
    --nodes 1 \
    --config-file dinov2/configs/train vits16.yaml \
    --output-dir '/share/medical/chjkusters/dinov2/output/' \
    train.dataset_path=ImageNet:split=TRAIN:root='/share/medical/Vault/datasets_working/GastroNet5MDino':extra='/share/medical/Vault/datasets_working/GastroNet5MDino'