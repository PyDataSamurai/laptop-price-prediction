def create_features(df):
    """ایجاد یا تبدیل ویژگی‌ها"""
    if 'CPU_Score' in df.columns and 'RAM' in df.columns:
        df['CPU_RAM_ratio'] = df['CPU_Score'] / df['RAM']
    return df
