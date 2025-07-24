import pandas as pd
import tensorflow as tf
from deepcocrystal.smiles_preprocessing import clean_smiles_batch, space_separate_smiles_list

# Load your CSV
df = pd.read_csv("cc.csv")

# Clean API and coformer SMILES individually
apis = clean_smiles_batch(
    df["SMILES1"].tolist(),
    uncharge=True,
    remove_stereochemistry=True,
    to_canonical=True,
)

coformers = clean_smiles_batch(
    df["SMILES2"].tolist(),
    uncharge=True,
    remove_stereochemistry=True,
    to_canonical=True,
)

# Filter out pairs where either cleaning failed
valid_pairs = [(a, c) for a, c in zip(apis, coformers) if a and c]
apis_cleaned, coformers_cleaned = zip(*valid_pairs)

# Tokenize separately
api_input = space_separate_smiles_list(apis_cleaned)
cof_input = space_separate_smiles_list(coformers_cleaned)

# Load trained model
model = tf.keras.models.load_model("deepcocrystal-trained")

# Predict
predictions = model.predict(
    x=[api_input, cof_input],
    batch_size=512,
    verbose=1
)

# Save results
df_result = pd.DataFrame({
    "SMILES1": apis_cleaned,
    "SMILES2": coformers_cleaned,
    "CocrystalProbability": predictions.flatten()
})
df_result.to_csv("predictions.csv", index=False)
