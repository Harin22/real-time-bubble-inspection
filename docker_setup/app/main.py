from fastapi import FastAPI
import onnxruntime as ort

app = FastAPI(title="Bubble Model API")

session = ort.InferenceSession("models/best_segmentation0.1v_int8.onnx")

@app.get("/")
def home():
    return {
        "message": "Dockerized bubble segmentation model is running",
        "model": "best_segmentation0.1v_int8.onnx"
    }