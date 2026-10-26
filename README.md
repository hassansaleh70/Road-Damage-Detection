# Road Damage Detection Using YOLOv10n

## Project Overview
This project uses YOLOv10n to detect and classify road damage in images.
<img width="1098" height="907" alt="Screenshot 2026-10-26 210232" src="https://github.com/user-attachments/assets/60570095-a1b1-451e-a096-4b63a1be6689" />

<img width="1023" height="903" alt="Screenshot 2026-10-26 210402" src="https://github.com/user-attachments/assets/4af12b02-e960-4c38-b21e-6fc668ffbf9e" />

<img width="1125" height="914" alt="Screenshot 2026-10-26 210154" src="https://github.com/user-attachments/assets/a5a36e86-b306-46a4-a80d-aabc9866e52c" />

<img width="1165" height="906" alt="Screenshot 2026-10-26 210513" src="https://github.com/user-attachments/assets/55be92c9-fc4b-4342-a5c3-dfe0e8444548" />
<img width="1029" height="923" alt="Screenshot 2026-10-26 210611" src="https://github.com/user-attachments/assets/a94e5b80-9773-435b-97b1-4cf642d87f72" />






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
