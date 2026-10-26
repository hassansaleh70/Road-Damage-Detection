# Road Damage Detection Using YOLOv10n

## Project Overview
This project uses YOLOv10n to detect and classify road damage in images.

## Supported Classes
- Alligator
- Block
- Crack
- Edge
- Longitudinal
- Pothole
- Transverse

## Dataset Summary

| Split | Images | Bounding Boxes |
|---|---:|---:|
| Training | 4930 | 15025 |
| Validation | 1146 | 3588 |
| Test | 681 | 2004 |
| Total | 6757 | 20617 |

## Model Information
- Architecture: YOLOv10n
- Model weights: weights/best.pt
- Model size: Approximately 5.54 MB
- Selection criterion: Validation performance

### Validation Metrics

| Metric | Score |
|---|---:|
| Precision | 61.5% |
| Recall | 42.5% |
| mAP@50 | 43.0% |
| mAP@50-95 | 25.2% |

## Application Features
- Upload road images.
- Detect and classify road damage.
- Display bounding boxes and confidence scores.
- Show detection counts by class.
- Adjust the confidence threshold.
- Select inference image size: 640 or 800.

## Project Structure
Road_Damage_Detection/
- app.py
- requirements.txt
- README.md
- model_comparison.csv
- hyperparameter_experiments.csv
- model_evaluation_report.md
- weights/best.pt

## Installation

Install the required dependencies:

    pip install -r requirements.txt

## Run the Application

    python app.py

The application will display a URL that you can open in your browser.

## Important Notes
- The model file must be available at weights/best.pt.
- GPU acceleration is used when CUDA is available.
- Detection results may vary depending on image quality and the confidence threshold.
- The predictions are intended to support road damage analysis, not replace professional inspections.

## Author
Hassan Saleh


## Evaluation Files

- `model_comparison.csv`: baseline validation comparison of YOLOv8n, YOLO11n, and YOLOv10n.
- `hyperparameter_experiments.csv`: recorded YOLOv10n tuning experiments.
- `model_evaluation_report.md`: evaluation methodology, results, limitations, and conclusion.

Review these files alongside the original training logs before final submission.
