# **Analyzing Success Rate of Upcoming Smartphone Models Using Machine Learning**  

## **Project Description**  
This project leverages machine learning to predict the success of upcoming smartphone models based on key features such as **price**, **RAM**, **processor type**, and **brand**. The model, built using the **Random Forest algorithm**, analyzes historical data and identifies the most influential attributes driving consumer satisfaction and market performance. Additionally, a **web-based interface** is developed using **Flask**, **HTML**, and **CSS**, enabling users to input smartphone specifications and receive real-time success predictions.

## **Features**  
- **Predictive Model**: Uses a Random Forest model to forecast the success of smartphones.  
- **Feature Importance Analysis**: Identifies key factors influencing success, aiding manufacturers in product optimization.  
- **Web Interface**: A user-friendly interface for real-time predictions based on user inputs.  
- **Scalable and Modular**: Easily extendable for future enhancements, such as incorporating real-time data and additional features.  

## **Technologies Used**  
- **Programming Language**: Python  
- **Machine Learning Framework**: Scikit-learn  
- **Web Framework**: Flask  
- **Frontend**: HTML, CSS  
- **Data Analysis and Visualization**: Pandas, NumPy, Matplotlib, Seaborn  
- **Model Saving**: Joblib  

## **Dataset**  
The dataset includes features such as:  
- **Brand**  
- **Model**  
- **Price**  
- **RAM**  
- **Processor Type**  
- **Battery Capacity**  
- **Camera Quality**  
- **Review Scores** (Target Variable)  


## **Key Files**  
- **app.py**: The main Flask application file.  
- **random_forest_model.pkl**: The saved Random Forest model.  
- **scaler.pkl**: The saved scaler for data preprocessing.  
- **index.html**: The HTML template for the web interface.  
- **styles.css**: The CSS file for styling the web interface.  

## **Results**  
- The model achieved a high **R² score** of 0.87, indicating strong predictive accuracy.  
- **Feature importance analysis** revealed that **price**, **RAM**, and **processor type** are the most significant predictors of smartphone success.  

## **Future Improvements**  
- Incorporate additional features such as marketing data and regional preferences.  
- Explore advanced models like **Gradient Boosting** and **Neural Networks** for enhanced accuracy.  
- Implement real-time data integration to update predictions dynamically.  
