import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

FILES = {
    'income': 'data/income.csv',
    'muni': 'data/municipal.csv',
    'school': 'data/schools.csv',
    'results': [
        'data/results_2016K.csv',
        'data/results_2016S.csv',
        'data/results_2017K.csv',
        'data/results_2017S.csv',
        'data/results_2018K.csv'
    ]
}
# https://www.ylioppilastutkinto.fi/tietopalvelut/tilastot/koulukohtaisia-tunnuslukuja
TRANSLATE_RESULT_COLUMNS = {
    'tutkintokerta': 'round',
    'koulun_nro': 'school_id',
    'hyvaksytty': 'pass',
    'ylioppilas': 'graduated',
    'ka_pak': 'mean_ob',  # Obligatory subject
    'ka': 'mean',
    'n': 'n',
    'ka_pkr': 'mean_pkr',  # Advanced subjects, languages and old real exam
    'n_pkr': 'n_pkr'
}
