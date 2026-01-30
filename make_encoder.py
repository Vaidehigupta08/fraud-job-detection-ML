import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
import pickle

# dataset load
df = pd.read_csv("cleaned_dataset.csv")

# target hata do
X = df.drop("fraudulent", axis=1)

# wahi categorical columns jo notebook me the
categorical_cols = [
    "location",
    "employment_type",
    "required_experience",
    "required_education",
    "industry",
    "function"
]

# SAME encoder settings
enc = OrdinalEncoder(
    handle_unknown="use_encoded_value",
    unknown_value=-1
)

# fit encoder
enc.fit(X[categorical_cols])

# save encoder
pickle.dump(enc, open("ordinal_encoder.pkl", "wb"))

print("✅ Encoder created and saved")
