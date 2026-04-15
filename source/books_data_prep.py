import pandas as pd

def convert_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df[['times_borrowed', 'page_count']] = df[['times_borrowed', 'page_count']].astype('Int16')
    df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce')
    df['total_copies'] = df['total_copies'].astype('Int16')
    df['year_published'] = pd.to_numeric(df['year_published'], errors='coerce')
    df['year_published'] = df['year_published'].astype('Int16')
    return df


def convert_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], errors='coerce', format='%d_%b_%y')
    return df


def convert_to_category(df: pd.DataFrame) -> pd.DataFrame:
    df['genre'] = df['genre'].astype('category')
    df['section'] = df['section'].astype('category')
    df['language'] = df['language'].astype('category')
    return df


def parse_ratings(df: pd.DataFrame) -> pd.DataFrame:

    def parse_rating(text):
        if pd.isna(text) or str(text).strip().lower() == "no rating available":
            return None
        
        parts = str(text).split()

        try:
            return float(parts[0])
        except (ValueError, IndexError):
            return None

    df['rating'] = df['rating'].apply(parse_rating)

    return df


def parse_ratings_count(df: pd.DataFrame) -> pd.DataFrame:

    def parse_rating_count(text):
        if pd.isna(text) or str(text).strip().lower() == "no reviews":
            return None

        parts = str(text).replace(',', '').split()

        try:
            return int(parts[0])
        except (ValueError, IndexError):
            return None

    df['ratings_count'] = df['ratings_count'].apply(parse_rating_count)

    return df


def split_dimensions_to_separate_columns(df: pd.DataFrame) -> pd.DataFrame:
    df[['dimensions_width', 'dimensions_depth', 'dimensions_height']] = df['dimensions'].str.replace("inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)
    df.drop('dimensions', axis=1, inplace=True)
    return df




def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.pipe(convert_to_numeric).pipe(convert_to_datetime).pipe(convert_to_category).pipe(parse_ratings).pipe(parse_ratings_count).pipe(split_dimensions_to_separate_columns)