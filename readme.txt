# downloading files from github and installing locally.
Type on cmd those commands to retrieve and install locally the deepcocrystal app:

git clone https://github.com/Chimele94/dc
cd deep-cocrystal
conda create -n dc python=3.10.13
conda activate dc
conda install -c conda-forge -–file requirements.txt
pip install .

# prepare the compound pairs file:
Once you have finished the installation, you need to prepare a CSV file containing the list of two compounds for which you want to predict cocrystallisation.
The file is so structurated:

SMILES1,SMILES2
smilesstringcomp1,smilesstringcomp2
...,...
smilesstringcompn,smilesstringcompm

and saved as cc.csv inside the main deepcocrystal directory (can use also another name, but then you need to change the predict.py file at the 6th line: df = pd.read_csv("YOURFILENAME.csv").

# run on the prediction
First navigate to the dc main directory. Open cmd and type those commands:
cd PATH/TO/deep-cocrystal (the path depends on where you have decided to install the app and if you stick with the above instructions should be in the home directory, so cd deep-cocrystal should be enough)
python predict.py

DONE.
the output is saved as result.csv inside main deep-cocrystal directory.


