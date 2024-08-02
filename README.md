Car Price Estimate App

Welcome to the Car Price Estimate App! 
This project leverages various machine learning models to predict car prices based on several features. The app is built using Streamlit, providing an interactive and user-friendly interface.


Features:

Interactive Interface: Built with Streamlit for easy interaction.

Robust Model Implementation: Uses advanced algorithms like XGBoost, CatBoost, LGBM, and RandomForest.

In-Depth Analysis: Thorough evaluation of each model’s performance.

Stacking Regressor: Combines multiple models with CatBoost as the meta learner for enhanced performance.


Models Used:

XGBoost,
CatBoost,
LGBM (LightGBM),
RandomForest,
The final model is a Stacking Regressor with CatBoost as the meta learner and the other models as base learners.


Usage:

Open the app in your browser.
Select the car features such as year, engine size, mileage, brand, and model.
The app will provide an estimated price based on the input features.


Dataset:

The dataset used for training the models includes features like the year of manufacture, engine size, mileage, brand, and model of the car. Ensure your dataset is clean and preprocessed before training the models.


Performance:

Through extensive testing, the CatBoost model demonstrated the best performance. Although the Stacking Regressor model was tested with CatBoost as the meta learner, CatBoost alone provided the most accurate predictions.

Contributing:

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project’s style and passes all tests.

License:

This project is licensed under the MIT License. See the LICENSE file for details.


Contact:
For any questions or suggestions, please open an issue or contact me at [ismayilzademrah@gmail.com].

Thank you for checking out the Car Price Estimate App! Feel free to share your feedback and suggestions.
