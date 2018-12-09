import pandas as pd
import config


def lowercase_inplace(df):
    df.columns = df.columns.str.lower()


def load_2018():
    """Load exam results, join with municipality_code"""
    # Join results.school_id <-> shools.municipality_id
    df_school = pd.read_csv(
        config.FILES['school'],
        encoding="ISO-8859-1",
        usecols=[0, 1, 4],  # only read number(school_id), school name and municipality
        sep=";")
    df_school.rename(
        columns={
            'number': 'school_id',
            'name': 'school_name',
            'municipality': 'municipality_code'},
        inplace=True)

    df_results = pd.DataFrame()
    result_file = 'data/results_2018S.csv'
    df_result_raw = pd.read_csv(
        result_file, encoding="ISO-8859-1", sep=";", decimal=",")

    # Translate finnish column names
    df_result_raw.rename(columns=config.TRANSLATE_RESULT_COLUMNS, inplace=True)
    df_result = pd.merge(df_result_raw, df_school, on="school_id")
    df_results = pd.concat([df_results, df_result], ignore_index=True, sort=False)
    
    # Split "round" column values, eg. 2016K -> 2016, K
    groups = r'(?P<year>\d{4})(?P<season>[SK])'
    df_results[['year', 'season']] = df_results['round'].str.extract(
        groups, expand=True)
    df_results["year"] = pd.to_numeric(df_results["year"])

    return df_results
