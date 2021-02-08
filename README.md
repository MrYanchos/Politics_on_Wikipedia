# Politics on Wikipedia
This project is focused on detecting political controversy in online communities. We use a bag-of-words model and a party-embed model, trained on the ideological books corpus (Sim et al, 2013) as well as congressional record data (api.govinfo.gov), and attempt to generalize this to Wikipedia articles, validating it on edit comments which explicitly mention reverting bias.


## Usage

Building the Environment using Dockerfile...

To run, in terminal type:
```
python run.py *target*
```

## Description of Contents

### `run.py`

Main driver for running the project. The targets and their functions are:
* all : Runs the whole pipeline.
* test: Runs the pipeline with pre-loaded test data.

### `config/`

* get_ibc_params.json : Input parameters for running the ibc target.

* interpret_ibc_params.json : Input parameters for running the interpret_ibc target.

### `notebooks/`

* EDA.ipynb : Jupyter notebook for developing code to get Wikipedia article text.
* Partyembed+IBC_EDA.ipynb : Jupyter notebook for the exploratory data analysis on Party_embed and IBC.
* IBC_preprocessing.ipynb : Jupyter notebook for preprocessing IBC data.

### `src/`

* `libcode.py` : Library code.

### `src/etl/`

* `bias.py` : Insert description here.
* `get_anames.py` : Insert description here.
* `get_atexts.py` : Executes tasks for preparing data for ...
* `get_ibc.py` : Insert description here.
* `validation_extractor.py` : Insert description here.

### `src/models/`

* `get_gns_scores.py` : Insert description here.
* `get_x2_scores.py` : Insert description here.
* `loadIBC.py` : Insert description here.
* `partyembed-ibc.py` : Insert description here.
* `partyembed_ibc.py` : Insert description here.
* `treeUtil.py` : Insert description here.


### `src/data/`
Contains raw datasets.


## Sources

Papers Referenced
* https://siepr.stanford.edu/sites/default/files/publications/16-028.pdf

* https://www.cs.toronto.edu/~gh/2528/RheaultCochraneOct2018.pdf

Data
* https://people.cs.umass.edu/~miyyer/ibc/index.html

* https://data.stanford.edu/congress_text

* https://dumps.wikimedia.org

