# 🏏 Cricket Predictor

An advanced machine learning-powered web application that predicts outcomes for various cricket matches including:

✅ ODI Men Winner
✅ ODI Women Winner
✅ IPL Match Winner  
✅ IPL Toss Winner
✅ PSL Match Winner  

Built with Python and Streamlit, the app delivers intuitive match-winning probabilities based on live or hypothetical match scenarios.

## 🚀 Features

- Match formats supported:
  - International Men’s & Women’s ODI
  - Indian Premier League (IPL)
  - Pakistan Super League (PSL)
- Predict:
  - Match winner probability
  - IPL toss winner
- Real-time calculations using features like:
  - Batting team, Bowling team, City
  - Runs left, Balls left, Wickets in hand
  - Target score, Current Run Rate (CRR), Required Run Rate (RRR)
- User-friendly interface with dynamic input widgets


  ## 🎥 Screen Recording

- [📺 Source Code](https://youtu.be/DNCX2eMaeeU)
 
- [📺 Live Demo](https://youtu.be/h7CiaXpHkFI)

---

## 🧠 Model Details

- Algorithm: Logistic regression & Random Forest Classifier
- Trained using hand-engineered cricket features
- Separate models for:
  - ODI Winner Prediction
  - IPL Winner Prediction
  - IPL Toss Prediction
  - PSL Winner Prediction

---

## 🛠️ Tech Stack

- Python 3.10+
- Pandas, NumPy, scikit-learn(1.7.1)
- Streamlit for web UI

---

## 🔧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/itsBabuaa/cricket-predictor.git
   cd cricket-predictor
````

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Launch the app:

   ```bash
   streamlit run app.py
   ```

---

## 🚧 Roadmap

* Add T20 World Cup support
* Live match scraping
* Enhanced model accuracy with neural networks
* Visual analytics dashboards

---

## 🙏 Acknowledgments

- Dataset source:
[ODI cricket dataset (Jan 2003-Aug 2023)](https://www.kaggle.com/datasets/sritata/odi-dataset-jan-2002-aug-2023?select=ODI_match_data.csv)
[IPL Complete Dataset (2008-2024)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
[PSL Complete Dataset (2016-2025)](https://www.kaggle.com/datasets/zeeshanahmad124586/psl-complete-dataset-2016-2025)
- Inspired by beauiful MS Dhoni innings and ICT matches.
- Thanks to the open-source community for the amazing tools and libraries.

---
👨‍💻 Developed by [@itsBabuaa](https://github.com/itsBabuaa)
⭐ If you found this project helpful, please consider giving it a star!

