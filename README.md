<h1 align="center">🏠 House Price Prediction Web Application</h1>

<p align="center">
A Machine Learning Web Application built using <b>Python, Flask, and Linear Regression</b>  
<br>
Deployed on <b>Render</b> with Gunicorn
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project predicts house prices using 19 property features such as size, location,
quality indicators, and temporal factors.
</p>

<ul>
<li>✔ Real-time price prediction</li>
<li>✔ Custom Linear Regression (Normal Equation)</li>
<li>✔ User-friendly web interface</li>
<li>✔ Production-ready deployment</li>
</ul>

<hr>

<h2>📊 Dataset Information</h2>

<ul>
<li><b>Dataset:</b> House Sales in King County, USA</li>
<li><b>Source:</b> Kaggle</li>
<li><b>Total Features:</b> 19</li>
<li><b>Target Variable:</b> Price</li>
</ul>

<hr>

<h2>🧠 Model Development</h2>

<p><b>Algorithm Used:</b> Custom Linear Regression</p>

<p><b>Normal Equation:</b></p>

<pre>
θ = (XᵀX)⁻¹ Xᵀy
</pre>

<p><b>Evaluation Metrics:</b></p>
<ul>
<li>Mean Squared Error (MSE)</li>
<li>Root Mean Squared Error (RMSE)</li>
<li>R² Score</li>
</ul>

<hr>

<h2>💻 Technology Stack</h2>

<h3>Backend</h3>
<ul>
<li>Python 3.x</li>
<li>Flask</li>
<li>NumPy</li>
<li>Pandas</li>
<li>Pickle</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>HTML5</li>
<li>CSS3</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>GitHub</li>
<li>Gunicorn</li>
<li>Render</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
House-Price-Prediction/
│
├── app.py
├── Mini_model.pkl
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── static/
└── README.md
</pre>

<hr>

<h2>🚀 Installation & Setup</h2>

<pre>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
</pre>

<p>Open in browser:</p>

<pre>
http://127.0.0.1:5000/
</pre>

<hr>

<h2>🌍 Live Demo</h2>

<p>
🔗 <a href="https://mini-project-1-aram.onrender.com/" target="_blank">
Live Application
</a>
</p>

<p>
💻 <a href="https://github.com/Indhira025/MINI_PROJECT_1" target="_blank">
GitHub Repository
</a>
</p>

<hr>

<h2>📈 Sample Prediction</h2>

<ul>
<li>Bedrooms: 3</li>
<li>Bathrooms: 1.5</li>
<li>Sqft Living: 1340</li>
<li>Year Built: 1955</li>
</ul>

<p><b>Predicted Price:</b> 355285.28</p>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
<li>Random Forest / XGBoost implementation</li>
<li>User authentication system</li>
<li>Export results to CSV/PDF</li>
<li>Interactive visualization charts</li>
<li>Docker deployment</li>
</ul>

<hr>

<h2>👩‍💻 Author</h2>

<p>
<b>R. Indhira</b><br>
Machine Learning & Python Developer<br>
Last Updated: 10/02/2026
</p>
