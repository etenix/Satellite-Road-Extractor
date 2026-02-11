import segmentation_models_pytorch as smp

def get_model():
    # ResNet34をエンコーダーとして使用したU-Net
    model = smp.Unet(
        encoder_name="resnet34",        
        encoder_weights="imagenet",     
        in_channels=3,                  # RGB 图像
        classes=1,                      # 道路抽出は2値分類（道路／非道路）です
        activation='sigmoid'
    )
    return model