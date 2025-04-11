# 💳 Credit Card Fraud Detection using Decision Tree

## 📌 Overview
This project is focused on detecting fraudulent credit card transactions using a Decision Tree Classifier. The model is trained on a real-world anonymized dataset and aims to accurately classify transactions as fraudulent or legitimate.

## 📂 Dataset
The dataset contains credit card transactions made in September 2013 by European cardholders. It has features that are the result of a PCA transformation due to confidentiality issues.

- Features: V1, V2, ..., V28 (anonymized)
- Additional columns: `Time`, `Amount`, `Class` (0 = Not Fraud, 1 = Fraud)

## ⚙️ Tools & Libraries
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

## 🔄 Workflow
1. **Data Exploration & Cleaning**
2. **Preprocessing** (Scaling, train-test split)
3. **Model Training** (Decision Tree Classifier)
4. **Evaluation** (Confusion Matrix, Accuracy, Precision, Recall, F1 Score)
5. **Feature Importance Visualization**

## 📊 Results
The model was evaluated using standard classification metrics and performed well in detecting fraud cases, considering the imbalanced nature of the dataset.

## 🖼️ Screenshots
![image](https://github.com/user-attachments/assets/22a6435e-84a1-49e0-895c-00b34ee99452)
![image](https://github.com/user-attachments/assets/b5a528e1-80e9-4f48-85bf-a55b3c212ed2)




## 🚀 How to Run
1. Clone the repository  
2. Install dependencies:
   ```
   pip install nltk
   pip install scikit-learn
   pip install streamlit
   pip install pandas
   ```  
4. Run the notebook: `python3 -m streamlit run app.py`

## 📬 Contact
For any questions or suggestions, feel free to reach out!
