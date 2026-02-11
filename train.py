import torch
import segmentation_models_pytorch as smp
from torch.utils.data import DataLoader
from utils.dataset import RoadDataset


# 設定
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = smp.Unet(
    encoder_name="resnet34", 
    encoder_weights="imagenet", 
    in_channels=3, 
    classes=1
).to(DEVICE)

# 道路抽出向けの損失関数：二値交差エントロピーとDice係数を組み合わせる
loss_fn = smp.losses.DiceLoss(mode='binary')
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

def train():
    # loader = DataLoader(dataset, batch_size=8, shuffle=True)
    model.train()
    # 学習ループのコード...
    print("Training started on", DEVICE)

if __name__ == "__main__":
    train()