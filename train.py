import torch
import segmentation_models_pytorch as smp
from torch.utils.data import DataLoader
from utils.dataset import RoadDataset

# 配置
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = smp.Unet(
    encoder_name="resnet34", 
    encoder_weights="imagenet", 
    in_channels=3, 
    classes=1
).to(DEVICE)

# 针对道路提取的损失函数：结合二元交叉熵与Dice系数
loss_fn = smp.losses.DiceLoss(mode='binary')
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

def train():
    # 这里假设你已经有了 DataLoader
    # loader = DataLoader(dataset, batch_size=8, shuffle=True)
    model.train()
    # 训练循环代码...
    print("Training started on", DEVICE)

if __name__ == "__main__":
    train()
