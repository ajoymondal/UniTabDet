# UniTabDet
UniTabBank: A Large Scale Multi-Lingual, Multi-Layout, Multi-Type, Multi-Format Dataset for Table Detection || WACV 2026

# UniTabDet: Table Detection using YOLOv11

UniTabDet is a table detection framework built using **Ultralytics YOLOv11** for detecting tables in documents.  
The project supports training, fine-tuning, and inference using the **UniTabBank dataset**, a large-scale multilingual dataset for table detection.

---

## Environment Setup

Follow the steps below to set up the environment.

```bash
conda create --name unitabdet python=3.10
conda activate unitabdet
pip install -r requirements.txt
```

---

## Dataset Structure

Organize the dataset using the following directory structure:

```
datasets/
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
└── labels/
    ├── train/
    ├── val/
    └── test/
```

---

## Pretrained Model

Place the pretrained model in the following path:

```
runs/detect/train/weights/best.pt
```

---

## Prediction

Run the following command to perform inference:

```bash
python3 test.py
```

---

## Finetuning

Run the following command to finetune the model:

```bash
python3 tune.py
```

---

## Training

Run the following command to train the model from scratch:

```bash
python3 train.py
```

---

## Dataset

The **UniTabBank dataset** can be downloaded from Hugging Face:

https://huggingface.co/datasets/ajoymondal/UniTabBank

---

## Trained Models

Pretrained models are available at:

https://huggingface.co/ajoymondal/UniTabBank-Model

---

## Acknowledgement

UniTabDet is built using **Ultralytics YOLOv11**.

https://docs.ultralytics.com/tasks/detect/#val

---

## Citation

If you use this dataset or code in your research, please cite:

```bibtex
@inproceedings{mondal2026unitabbank,
  author    = {Ajoy Mondal and Saumya Mundra and Avijit Dasgupta and C. V. Jawahar},
  title     = {UniTabBank: A Large Scale Multi-Lingual, Multi-Layout, Multi-Type, Multi-Format Dataset for Table Detection},
  booktitle = {WACV},
  year      = {2026},
}
```

---

## License

This project is released for research purposes.
