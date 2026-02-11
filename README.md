# Satellite-Road-Extractor

本プロジェクトは、ディープラーニング技術（U-Net）を用いて、高解像度の衛星画像から道路ネットワークを自動的にセグメンテーション・抽出することを目的としています。

## 🚀 機能特性
- モデル構造：ResNet をバックボーンとした U-Net 構造を採用
- 損失関数：道路ピクセルの不均衡に対応する Dice Loss + BCE Loss を使用
- 地理情報対応：GeoTIFF（地理座標付き）データの処理に対応
- 後処理：二値化およびスケルトン化により、線状道路データを生成

## 📦 動作環境
- Python 3.8+
- PyTorch 1.10+
- CUDA（GPU使用時・任意）

## 🔧 インストール
```bash
git clone https://github.com/YourUsername/Satellite-Road-Extractor.git
cd Satellite-Road-Extractor
pip install -r requirements.txt
```

## 🛠️ 使用方法

### 1️⃣ データ準備
- 衛星画像 → data/images
- マスク画像 → data/masks

- ※ ファイル名は対応させてください。

### 2️⃣ モデル学習

```python train.py --epochs 50 --batch_size 8
```

### 3️⃣ 推論・予測

```python predict.py --input test_image.tif
```

## 📚 主要ライブラリ（requirements.txt）

torch>=1.10.0
torchvision
segmentation-models-pytorch
rasterio
opencv-python
albumentations
matplotlib

## 🧩 データセット処理（utils/dataset.py）

衛星画像はサイズが大きいため、分割処理およびデータ拡張を行います。

主な処理内容：
- RGB変換
- 正規化（0〜1）
- Albumentationsによる拡張
- Tensor変換

## ⚙️ 学習処理（train.py）
- エンコーダ：ResNet34（ImageNet事前学習）
- 出力クラス数：1（二値分類）
- 最適化手法：Adam
- 学習率：0.0001

損失関数：
```bash
Dice Loss + Binary Cross Entropy
```
道路抽出のクラス不均衡問題に対応しています。

## 🧠 後処理（utils/post_process.py）

予測結果にはノイズが含まれるため、以下の処理を実施します：
- 二値化（Thresholding）
- スケルトン化（Skeletonization）

これにより、1ピクセル幅の道路ネットワークを生成します。

## 📈 応用例
- 都市道路マッピング
- 災害時の道路被害解析
- 自動地図生成
- スマートシティ分析

## 📄 ライセンス

本プロジェクトは MIT License の下で公開されています。