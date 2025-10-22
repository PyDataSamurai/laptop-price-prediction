from data_preprocessing import load_data, clean_data
from feature_engineering import create_features
from model import train_model

def main():
    df = load_data("../data/laptop_data.csv")
    df = clean_data(df)
    df = create_features(df)
    model = train_model(df)
    
if __name__ == "__main__":
    main()
