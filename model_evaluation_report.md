# Road Damage Detection — Model Evaluation Report

## 1. Project Objective

The objective is to detect and classify road damage in images using YOLO object detection models and provide an interactive application for inference.

## 2. Dataset

| Split | Images | Bounding Boxes |
|---|---:|---:|
| Training | 4,930 | 15,025 |
| Validation | 1,146 | 3,588 |
| Test | 681 | 2,004 |
| Total | 6,757 | 20,617 |

The dataset contains seven classes: alligator, block, crack, edge, longitudinal, pothole, and transverse.

The edge class has only one validation instance and no test instances. Its generalization performance therefore cannot be reliably assessed using these splits.

## 3. Baseline Model Comparison

The following baseline results are from the validation set.

| Model | Precision | Recall | mAP@50 | mAP@50-95 | Inference (ms) | Size (MB) |
|---|---:|---:|---:|---:|---:|---:|
| YOLOv8n | 57.1% | 39.6% | 40.2% | 23.6% | 2.0 | 6.5 |
| YOLO11n | 61.6% | 39.2% | 41.3% | 24.0% | 4.6 | 5.5 |
| YOLOv10n | 62.4% | 38.5% | 40.6% | 23.7% | 2.8 | 5.8 |

Among these baseline runs, YOLO11n had the highest mAP@50 and mAP@50-95, while YOLOv10n had the highest precision. Inference times and model sizes are reported from the recorded experiments and may depend on the execution environment.

## 4. Hyperparameter Experiments

The detailed experiment table is available in `hyperparameter_experiments.csv`.

| Experiment | Learning Rate | Image Size | Batch Size | Precision | Recall | mAP@50 | mAP@50-95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| AdamW | 0.001 | 640 | 16 | 59.10% | 38.80% | 40.00% | 23.40% |
| AdamW | 0.0005 | 640 | 16 | 61.18% | 40.14% | 41.76% | 24.37% |
| Fine-tuned | 0.0005 | 800 | 8 | 61.40% | 42.00% | 42.60% | 24.40% |
| Fine-tuned | 0.0003 | 640 | 16 | 61.50% | 42.50% | 43.00% | 25.20% |
| Fine-tuned | 0.0003 | 800 | 8 | 62.00% | 42.10% | 42.80% | 24.70% |

The selected checkpoint is `weights/best.pt`, copied from the YOLOv10n run using a learning rate of 0.0003 and image size 640.

It achieved the highest recorded mAP@50-95 among the listed tuning experiments on validation (25.2%).

## 5. Application

The Gradio application supports:
- Uploading a road image.
- Displaying predicted bounding boxes and labels.
- Showing confidence scores for detections.
- Summarizing detections by class.
- Adjusting the confidence threshold.
- Selecting an inference image size of 640 or 800.

## 6. Limitations

- The edge class is underrepresented in validation and test data.
- Validation metrics do not guarantee the same performance on unseen real-world images.
- Inference speed depends on hardware and runtime configuration.
- The recorded baseline and tuning results should be checked against original training logs before final submission.
- Test-set results are not used here to select hyperparameters.

## 7. Conclusion

The project compares YOLOv8n, YOLO11n, and YOLOv10n and documents multiple YOLOv10n tuning experiments. Based on the recorded validation results, the tuned YOLOv10n checkpoint was selected for the application because it achieved the highest mAP@50-95 among the listed tuning runs.

## Author

Hassan Saleh
