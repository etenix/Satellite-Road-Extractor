from skimage.morphology import skeletonize
import cv2

def get_road_skeleton(prob_mask, threshold=0.5):
    """将预测的概率图转换为单像素宽的骨架"""
    binary_mask = (prob_mask > threshold).astype(np.uint8)
    skeleton = skeletonize(binary_mask)
    return skeleton