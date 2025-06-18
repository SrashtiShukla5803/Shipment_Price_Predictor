from setuptools import setup, find_packages

setup(
    name="shipment",
    version="0.0.1",
    author="Srashti Shukla",
    author_email="srashtishukla1111@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "scipy",
        "statsmodels",
        "plotly",
        "dash",
        "flask",
        "flask-cors",
        "gunicorn"
    ],
)