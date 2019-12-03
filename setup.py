import setuptools

setuptools.setup(
      name='nbaudit',
      version='0.0.3',
      description='Audit Logging Extension for the Jupyter Notebook Server',
      author='cccs',
      author_email='',
      license="BSD 3-Clause",
      packages=setuptools.find_packages(),
      install_requires=['notebook'],
      python_requires='>=3.6',
      classifiers=[
        'Framework :: Jupyter',
      ], 
      url='',
      include_package_data = True,
      data_files = [
        ("etc/jupyter/jupyter_notebook_config.d", [
          "jupyter-config/jupyter_notebook_config.d/nbaudit.json"
        ])
      ]
     )
