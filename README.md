# Title: Tuberculosis (TB) Detection from Chest X-ray using Deep Transfer Learning (PyTorch)

## Domain: Medical Imaging

![image](https://user-images.githubusercontent.com/46085301/227527871-be1da2c3-b6f9-47d4-82a0-5a9529054f38.png)

## Introduction:

### Background

Tuberculosis (TB) is a communicable disease which is a major public health problem in Nepal. It is one of
the top 10 causes of death worldwide and in Nepal, and the leading cause of death from a single infectious
agent (ranking above HIV/AIDS).

In Nepal, an estimated 69,000 fell ill with TB during FY 2077/78. National Tuberculosis Programme (NTP)
registered 28,677 (nearly 58% missing vs. the projection) all forms of TB cases (38% female and 62% male).
Out of 28,677 all forms of TB cases, 28,182 incident TB cases.

> Source : Department of Health Services
> 2077/78 (2020/21) | Annual Report

### Goal and Objective

The goal of this project is to develop an AI-based solution for detecting tuberculosis from chest X-ray images using transfer learning approach. The solution aims to improve the accuracy and efficiency of TB diagnosis. We aim to use the pre-trained model to detect the signs of TB in chest X-ray images and fine-tune the model to improve the performance. Our solution aims to assist healthcare providers and help in addressing the TB epidemic, particularly in under-served areas where access to healthcare is limited.

### Dataset:

We have used Tuberculosis (TB) Chest X-ray Database to train and evaluate our model.

#### [Tuberculosis (TB) Chest X-ray Database](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset)

A team of researchers from Qatar University, Doha, Qatar, and the University of Dhaka, Bangladesh along with their collaborators from Malaysia in collaboration with medical doctors from Hamad Medical Corporation and Bangladesh have created a database of chest X-ray images for Tuberculosis (TB) positive cases along with Normal images. In our current release, there are 700 TB images publicly accessible and 2800 TB images can be downloaded from NIAID TB portal[3] by signing an agreement, and 3500 normal images.

> Tawsifur Rahman, Amith Khandakar, Muhammad A. Kadir, Khandaker R. Islam, Khandaker F. Islam, Zaid B. Mahbub, Mohamed Arselene Ayari, Muhammad E. H. Chowdhury. (2020) "Reliable Tuberculosis Detection using Chest X-ray with Deep Learning, Segmentation and Visualization". IEEE Access, Vol. 8, pp 191586 - 191601. DOI. 10.1109/ACCESS.2020.3031384. Paper Link

### Run Locally

Step 1. Clone the repository

```bash
git clone https://github.com/bhimrazy/voyage-imaging.git
```

Step 2. Go to the project directory

```bash
cd voyage-imaging
```

Step 3. Start Backend Server

```bash
cd backend

# create virtual environment
python -m venv venv # or python3 -m venv venv
# activate virtual environment
source venv/bin/activate  # source venv/Scripts/activate (for windows)

# install dependencies
pip install -r dev-requirements.txt

# start server
python app.py

```

Step 4. Start Frontend Server

```bash
cd frontend

# install dependencies
npm install

# copy env file
cp .env.example .env.local

# start server
npm run dev

# open browser and go to http://localhost:3000
```
