# Iris Classifier API

A simple machine learning web app that predicts the class of an iris flower using a trained model and Flask.

## How to Run

1. Train the model:
```bash
python train_model.py
```

2. Run the app:
```bash
python app.py
```

3. Open your browser and go to: `http://127.0.0.1:5000`

## Deployment

You can deploy this to:
- Render (https://render.com)
- Railway (https://railway.app)
- Heroku (deprecated free tier)

Just make sure to include `requirements.txt` and use `gunicorn` if needed for production.
