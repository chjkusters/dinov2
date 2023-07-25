### SETUP WANDB LOGGING ###
export WANDB_API_KEY=86058605d2baf0f71d91c52b865cb2ad2482fbc1
export WANDB_DIR=/share/medical/chjkusters/dinov2/
export WANDB_CONFIG_DIR=/share/medical/chjkusters/dinov2/
export WANDB_CACHE_DIR=/share/medical/chjkusters/dinov2/
export WANDB_START_METHOD="thread"
export HOME=/share/medical/chjkusters/dinov2/
wandb login

### SETUP DIRECTORY TO WORK IN ###
cd /share/medical/chjkusters/dinov2/

### EXECUTE setup.py ###
export HOME=/share/medical/chjkusters/dinov2install/
python3 setup.py install --user

### RUN DINOV2 ON GASTRONET ###
torchrun --nnodes 1 --nproc_per_node 8 dinov2/train/train.py \
    --config-file dinov2/configs/train/vits16.yaml \
    --output-dir '/share/medical/chjkusters/dinov2/output/Experiment 8' \
    train.dataset_path=ImageNet:split=TRAIN:root='/share/medical/Vault/datasets_working/GastroNet5MDino':extra='/share/medical/Vault/datasets_working/GastroNet5MDino'
