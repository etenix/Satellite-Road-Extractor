# Satellite-Road-Extractor

本プロジェクトは、ディープラーニング技術（U-Net）を用いて、高解像度の衛星画像から道路ネットワークを自動的にセグメンテーション・抽出することを目的としています。

## 🚀 主な機能
* **モデルアーキテクチャ**: ResNetバックボーンを採用したU-Net構造。
* **損失関数**: 道路ピクセルの不均衡問題に対応するため、Dice Loss + BCE Lossを最適化。
* **地理空間データのサポート**: 地理座標を持つGeoTIFF形式の処理に対応。
* **後処理**: 確率マップを線状の要素に変換するための二値化および骨架化（Skeletonization）スクリプトを同梱。

## 📦 環境構築
```bash
git clone [https://github.com/YourUsername/Satellite-Road-Extractor.git](https://github.com/etenix/Satellite-Road-Extractor.git)
cd Satellite-Road-Extractor
pip install -r requirements.txt