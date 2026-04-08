# Real-Time Bubble Detection for Advanced Manufacturing

Lightweight computer vision pipeline for detecting, counting, measuring, and tracking bubbles in continuous reactor flow systems.

Built using **YOLOv8 instance segmentation** and optimized for **edge deployment on Raspberry Pi 5**.

---

## Pipeline Overview

<img src="https://github.com/user-attachments/assets/27afd1dc-7303-49c0-ad04-40e3bc9e5d3d" width="100%">

---

## Features

- Instance segmentation (YOLOv8s-seg / YOLOv8n-seg)
- Per-frame bubble counting
- Bubble radius measurement
- Tracking using Centroid Tracker / OC-SORT
- ONNX export for cross-platform inference
- INT8 dynamic quantization for embedded deployment

--- 

## Model Comparison

| Model | Precision | mAP@0.5 | FPS |
|--------|------------|----------|------|
| YOLOv8n-seg | 0.775 | 0.876 | 65 |
| YOLOv8s-seg | 0.797 | 0.869 | 35 |
| Mask R-CNN + OC-SORT | 0.83 | 0.880 | 12 |

**YOLOv8n-seg selected** for best speed–accuracy tradeoff for real-time edge inference.

---

## Edge Optimization: ONNX + INT8 Quantization

The optimized YOLOv8n-seg model was exported to ONNX (FP32) and dynamically quantized to INT8 using ONNX Runtime.

### Quantization Results

| Format | Size | Precision | mAP@0.5 | FPS |
|--------|------|------------|----------|------|
| FP32 | 7 MB | 0.775 | 0.876 | 32 |
| INT8 | 3.5 MB | 0.770 | 0.870 | 65 |

**Results:**
- 50% model size reduction  
- ~2× inference speed improvement  
- Minimal accuracy drop  

Optimized for CPU-based inference on Raspberry Pi 5.

---

## Example Output

<img width="816" height="380" src="https://github.com/user-attachments/assets/1a814e24-b0d0-4397-84e3-c0c4fd8bfc33" />

---
## Dockerized Inference Service

Containerized ONNX Runtime inference service for the INT8-optimized bubble segmentation model.

**Location:** `docker_setup/`

**Files included:**

---

## Repository Structure

- `baseline_bubble_training.ipynb` → YOLOv8 training pipeline  
- `bubble_model_testing_v1.ipynb` → Image inference  
- `bubble_model_testing_v2.ipynb` → Video + tracking pipeline  
- `onnx_quantization.ipynb` → ONNX export and INT8 optimization  

---

## Installation

```bash
git clone https://github.com/Harin22/real-time-bubble-inspection.git
cd real-time-bubble-inspection
pip install -r requirements.txt
```

---

## Deployment Target

- Raspberry Pi 5  
- Pi Camera Module  
- Real-time monitoring in continuous reactor flow systems  

---

## License

MIT License
