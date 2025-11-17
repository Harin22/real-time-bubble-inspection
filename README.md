# Real-Time Bubble Detection Using Machine Learning for Quality Control in Advanced Manufacturing​

The project will Detect, count, measure, and track bubbles in a reactor flow for **quality control in advanced manufacturing**.  
Trained with **YOLOv8 segmentation**, working towards The model to optimized for real-time deployment and can be deployed on a Raspberry Pi 5.

---

### Pipeline Overview

<img src="https://github.com/user-attachments/assets/27afd1dc-7303-49c0-ad04-40e3bc9e5d3d" width="100%">

---

## Features
- Bubble **detection + segmentation** (YOLOv8-S / YOLOv8-M)
- Bubble **counting** in video streams
- Bubble **size measurement** in pixels (mm conversion possible with calibration)
- **Tracking** across frames (Centroid Tracker / OC-SORT)
- Export to **ONNX** for Raspberry Pi deployment

---

## Files
- `Bubble_model_training.ipynb` → Train YOLOv8 segmentation model on your dataset  
- `Bubble_model_testing_image.ipynb` → Test on a single image  
- `Bubble_model_testing_video.ipynb` → Test on videos. To detect count + measure bubbles  
- `MaskRCNN_OCSORT_experiments.ipynb` → Experimental advanced approach (Working towards it)

---

## The ver 1 result
<img width="816" height="380" alt="res1" src="https://github.com/user-attachments/assets/1a814e24-b0d0-4397-84e3-c0c4fd8bfc33" />


---

 Current Version: bubble_insp_ver0.2 — actively maintained and deployed in the repository.

---

### contribute by Clone & Install this project 
```bash
git clone https://github.com/Harin22/real-time-bubble-inspection.git
cd real-time-bubble-inspection
pip install -r requirements.txt

