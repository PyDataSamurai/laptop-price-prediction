import pandas as pd

def load_data(file_path):
    """بارگذاری داده‌ها"""
    return pd.read_csv(file_path)

def clean_data(df):
    """پاک‌سازی داده‌ها"""
    df = df.dropna()
    if 'RAM' in df.columns:
        df['RAM'] = df['RAM'].str.replace('GB','').astype(int)
    return df
