
from pathlib import Path
import gradio as gr
import pandas as pd
from PIL import Image
from collections import Counter
import torch
from ultralytics import YOLO

MODEL_PATH = str(Path(__file__).resolve().parent / "weights" / "best.pt")

model = YOLO(MODEL_PATH)
CLASS_NAMES = model.names

def detect_damage(image, confidence_threshold, image_size):
    if image is None:
        return None, pd.DataFrame(columns=["Damage Type", "Confidence"]), "Please upload a road image."

    results = model.predict(
        source=image,
        conf=confidence_threshold,
        imgsz=int(image_size),
        device=0 if torch.cuda.is_available() else "cpu",
        verbose=False
    )

    result = results[0]
    annotated_image = Image.fromarray(result.plot()[:, :, ::-1])

    detections = []

    if result.boxes is not None:
        for box in result.boxes:
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            detections.append({
                "Damage Type": CLASS_NAMES[class_id],
                "Confidence": round(confidence * 100, 2)
            })

    detections_df = pd.DataFrame(
        detections,
        columns=["Damage Type", "Confidence"]
    )

    if not detections:
        summary = (
            "No damage detected above the selected confidence threshold. "
            "Try lowering the threshold."
        )
    else:
        counts = Counter(item["Damage Type"] for item in detections)
        summary_lines = [
            f"Total detections: {len(detections)}",
            "",
            "Detections by class:"
        ]
        summary_lines += [
            f"- {name}: {count}"
            for name, count in sorted(counts.items())
        ]
        summary = "\n".join(summary_lines)

    return annotated_image, detections_df, summary


with gr.Blocks(title="Road Damage Detection") as demo:
    gr.Markdown("""
    # Road Damage Detection
    ### AI-powered road damage detection using YOLOv10n

    Upload a road image to detect damage types, visualize bounding boxes,
    and review the confidence score for each detection.
    """)

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Road Image", type="pil")
            confidence = gr.Slider(
                minimum=0.10, maximum=0.90, value=0.25,
                step=0.05, label="Confidence Threshold"
            )
            image_size = gr.Radio(
                choices=[640, 800], value=640,
                label="Inference Image Size"
            )
            detect_button = gr.Button(
                "Detect Road Damage", variant="primary"
            )

        with gr.Column():
            output_image = gr.Image(label="Detection Results")
            output_summary = gr.Textbox(
                label="Detection Summary", lines=8
            )

    detections_table = gr.Dataframe(
        headers=["Damage Type", "Confidence"],
        label="Detected Damage Details",
        interactive=False
    )

    detect_button.click(
        fn=detect_damage,
        inputs=[input_image, confidence, image_size],
        outputs=[output_image, detections_table, output_summary]
    )

    gr.Markdown("""
    <div style="text-align: center; margin-top: 30px; padding: 15px;
                color: #9CA3AF; font-size: 14px;">
        Developed by <strong style="color: #F97316;">Hassan Saleh</strong>
    </div>
    """)

if __name__ == "__main__":
    demo.launch(share=True, debug=True)
