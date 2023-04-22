from setuptools import setup, find_packages

setup(name="Diamond_Price_Analysis",
      version="0.0.1",
      author="Farshid",
      author_email="farshidhesami@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask","scikit-learn","seaborn","Matplotlib"]
      ) 