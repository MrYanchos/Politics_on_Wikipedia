# Politics on Wikipedia
This project is focused on detecting political controversy in online communities. We use a bag-of-words model and a party-embed model, trained on the ideological books corpus (Sim et al, 2013) as well as congressional record data (api.govinfo.gov), and attempt to generalize this to Wikipedia articles, validating it on edit comments which explicitly mention reverting bias.


## Usage

This code is intended to be run with the dockerfile vasyasha/pow_docker

It relies on data from the ideological books corpus (Sim et al., 2013) with sub-sentential annotations (Iyyer et al., 2014). To download this data please visit https://people.cs.umass.edu/~miyyer/ibc/index.html where you can send an email to the address in order to obtain the full dataset.

Once obtained, please extract the dataset to **/data/full_ibc/**

Once this is done, please alter the config in **config/get_ibc_params** accordingly.

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

* `bias.py` : Preliminary function for extracting bias from Rheault and Cochrane model.
* `get_anames.py` : Insert description here.
* `get_atexts.py` : Executes tasks for preparing data for ...
* `get_ibc.py` : Downloads sample IBC data. For the full dataset, please see **Usage** above.
* `validation_extractor.py` : Preliminary code for extracting a validation set from Wikipedia edits.

### `src/models/`

* `get_gns_scores.py` : Insert description here.
* `get_x2_scores.py` : Insert description here.
* `loadIBC.py` : This project uses code from (Sim et al., 2013) and (Iyyer et al., 2014). As this was written in a previous version of python, these updated versions replace downloads made during the building process.
* `partyembed_ibc.py` : This file extracts from the partyembed .issue() function the ideological leanings of each word in each sentence of the ideological books corpus. After applying an aggregate function on this data, it writes this to a csv.
* `treeUtil.py` : This project uses code from (Sim et al., 2013) and (Iyyer et al., 2014). As this was written in a previous version of python, these updated versions replace downloads made during the building process.


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

