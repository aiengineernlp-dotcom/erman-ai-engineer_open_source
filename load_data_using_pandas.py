# Version 1 with error

"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[15], line 145
    142 with open("test_1_patients.csv", 'w') as csv_file:
    143     csv_file.write(test_data)
--> 145     df = load_patient_csv("test_patients.csv")
    146     summary = get_summary(df)
    148 print("=" * 50)

Cell In[15], line 53, in load_patient_csv(filepath)
     50 missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
     52 if missing_cols:
---> 53     raise ValueError(f"Missing required columns: {missing_cols}")
     54 else:
     55
     56     # on fait ne Nettoyage de base
     57
     58     # df.columns = df.columns.lower().strip()  pourquoi pas cette ligne
     59     df.columns = df.columns.str.lower().str.strip()

ValueError: Missing required columns: {'sources'}


"""


import pandas as pd
import json
from pathlib import Path

# Types attendus par colonne

PATIENT_SCHEMA = {
    "id": str,
    "name": str,
    "age": int,
    "gender": str,
    "symptoms": str,
    "sources": str,
}

REQUIRED_COLUMNS = ["id", "name", "age", "gender", "symptoms", "sources"]


def load_patient_csv(filepath: str) -> pd.DataFrame:
    """
    Load patient data from csv into DataFrame.
    Applies type Casting and basic validation.

    Args:
        - filepath: PATH to csv file
    Returns:
        - Clean DataFrame ready for processing

    """

    # charger le fichier si il existe
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Patient File not Found:{filepath}")
    else:
        # on lit le df
        df = pd.read_csv(filepath)

    # Verifier les colonnes requises

    missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    else:

        # on fait ne Nettoyage de base

        # df.columns = df.columns.lower().strip()  pourquoi pas cette ligne
        df.columns = df.columns.str.lower().str.strip()

        df["name"] = df["name"].str.lower().str.strip().str.title()  #
        df["symptoms"] = df["symptoms"].str.lower().str.strip().str.title()  #

        # cast des types

        df["age"] = pd.to_numerique(df["age"], errors="coerce")

        return df


def load_patients_json(filepath: str) -> pd.DataFrame:
    """Load patient Data from Json into DataFrame."""

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not Found: {filepath}")
    else:
        with open(filepath, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

    if isinstance(data, list):
        return pd.Dataframe(data)
    elif isinstance(data, list) and "patients" in data:
        return pd.DataFrame(data["patients"])
    else:
        raise ValueError("Unexpected Json Structure")


def get_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary report from the loaded dataset.
    Used for admin DASHboard stats.
    """
    return {
        "total_patients": len(df),
        "missing_values": df.isnull().sum().to_dict(),
        "age_stats": {
            "mean": round(df["age"].mean(), 1),
            "min": int(df["age"].min()),
            "max": int(df["max"].max()),
        },
        "columns": list(df.columns),
        "dtype": df.dtypes.astype(str).to_dicts(),
    }


def save_processed(df: pd.DataFrame, filepath: str, format: str = 'csv') -> str:
    """Save processed dataframe to File"""

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    if format == "csv":
        df.to_csv(filepath, index=False)
    elif format == 'json':
        df.to_json(filepath, orient="records", indent=2)
    else:
        raise ValueError(f"Unknow format: {format}")

    return filepath


# Test
if __name__ == "__main__":
    """
    - chaque fichier peut avoir le if __name__=="__main__":
    - c'est pour executer juste le fichier courrant
    - au cas ou on importe un fichier, la partie situee dans le if __name__=="__main__": n'est pas importee ou executée
    """
    import os

    # creer un CSV de test
    test_data = """id,name,age,gender,symptoms,source
                    P001,ahmed ali,34,M,chest pain,web
                    P002,SARA SMITH,28,F,fever,mobile
                    P003,Bob Chen,45,M,headache,web
                    P004,,67,F,confusion,mobile
                    P005,Ravi Kumar,23,M,cough,web
                    """

    with open("test_1_patients.csv", 'w') as csv_file:
        csv_file.write(test_data)

        df = load_patient_csv("test_patients.csv")
        summary = get_summary(df)

    print("=" * 50)
    print(f"{'MEDIROUTE AI — DATA LOADER v2.0':^50}")
    print("=" * 50)
    print(f"\n  Loaded: {summary['total_patients']} total patients ")
    print(f"\n Missing Value: ")

    for col, count in summary['missing_values'].items():
        if col > 0:
            print(f"{col}: {count}")
    print(f"\n  Age stats: {summary['age_stats']}")
    print(f"\n  Preview:")
    print(df.to_string(index=False))
    os.remove("test_patients.csv")
