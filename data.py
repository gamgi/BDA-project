import pandas as pd
import config


def lowercase_inplace(df):
    df.columns = df.columns.str.lower()


class Data:
    """Collection of data loading methods"""
    @staticmethod
    def _load_income():
        """Load income data, join with municipality_code"""
        df_income_raw = pd.read_csv(
            config.FILES['income'],
            encoding="ISO-8859-1",
            skiprows=1)
        lowercase_inplace(df_income_raw)

        df_muni = pd.read_csv(
            config.FILES['muni'],
            encoding="utf-8",
            skiprows=1,  # Skip row "SSS","WHOLE COUNTRY"
            header=None,
            names=[
                "code",
                "municipality"])
        df_muni.rename(columns={'code': 'municipality_code'}, inplace=True)
        # Join income.municipality_name <-> municipality.municipality_id
        df_income = pd.merge(df_income_raw, df_muni, on="municipality")
        return df_income

    @staticmethod
    def _load_results():
        """Load exam results, join with municipality_code"""
        # Join results.school_id <-> shools.municipality_id
        df_school = pd.read_csv(
            config.FILES['school'],
            encoding="ISO-8859-1",
            usecols=[0, 4],  # only read number(school_id) and municipality
            sep=";")
        df_school.rename(
            columns={
                'number': 'school_id',
                'municipality': 'municipality_code'},
            inplace=True)

        df_results = pd.DataFrame()
        for result_file in config.FILES['results']:
            df_result_raw = pd.read_csv(result_file, encoding="ISO-8859-1", sep=";")
            # Translate finnish column names
            df_result_raw.rename(columns=config.TRANSLATE_RESULT_COLUMNS, inplace=True)

            df_result = pd.merge(df_result_raw, df_school, on="school_id")
            df_results = pd.concat([df_results, df_result], ignore_index=True, sort=False)
        return df_results

    @staticmethod
    def load():
        """Load income data and exam results.

        Returns
        -------
        df_income
            Dataframe on income data per municipality, with municipality code
        df_results
            Dataframe on exam results per school, with municipality code
        """
        df_income = Data._load_income()
        df_results = Data._load_results()

        return df_income, df_results
