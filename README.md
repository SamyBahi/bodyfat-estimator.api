This Flask app is the back end part of an AI Based bodyfat estimator. It is coupled with a NextJS frontend that you can find [here](https://github.com/SamyBahi/bodyfat-estimator.web) The web app uses Machine Learning to estimate your density taking your mensurations as an input, and computes your bodyfat according to Siri's formula (1956).

You can find my approach to predicting density from mensurations (that led to the model that is currently used on the backend) on [this notebook](https://github.com/SamyBahi/bodyfat-estimation).

## Getting Started

Create a virtual environement :

```bash
python3 -m venv .venv/[env_name]

or

python -m venv .venv/[env_name]
```

Activate venv :

```bash
. .venv/[env_name]/bin/activate
```

Install packages :

```bash
pip3 install -r requirements.txt

or

pip install -r requirements.txt
```

Run the development server:

```bash
python run.py
```

Send requests to `http://localhost:5000/[route]` with your browser to see the result.
