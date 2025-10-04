import pandas as pd
import gzip
from functools import lru_cache
from app.core.config import settings

@lru_cache(maxsize=None)
def load_data():
    try:
        with gzip.open(settings.DATA_FILE_PATH, 'rt', encoding='utf-8') as f:
            df = pd.read_json(f, lines=True)
        return df
    except FileNotFoundError:
        # En un escenario real, aquí se podría registrar el error o manejarlo de forma más robusta.
        return pd.DataFrame()

