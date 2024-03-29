import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold

import rampwf as rw

problem_title = "Urban trees: Towards a Clinical Study"


_event_label_names = ['C2', 'C1', 'C3', 'C4', 'NaN', 'C5']

description_features_cat = ['type_sol',
                            'classe_age',
                            'classe_hauteur',
                            'classe_circonference',
                            'vigueur_pousse',
                            'plaie_collet',
                            'fissure_tronc',
                            'plaie_tronc',
                            'fissure_houppier',
                            'bois_mort_houppier',
                            'plaie_houppier',
                            'prescription_1',
                            'prescription_2',
                            'prescription_3',
                            'type_delai_1',
                            'type_delai_2']
description_features_string = ["ID_ARBRE",
                               'commune',
                               'quartier',
                               'site',
                               'cote_voirie',
                               'genre_arbre',
                               'espece_arbre',
                               'situation',
                               'port_arbre',
                               'champignon_collet',
                               'insecte_collet',
                               'observation_collet',
                               'champignon_tronc',
                               'insecte_tronc',
                               'rejet_tronc',
                               'tuteurage_arbre',
                               'canisse_arbre',
                               'observation_tronc',
                               'champignon_houppier',
                               'insecte_houppier',
                               'ecorce_incluse_houppier',
                               'observation_houppier',
                               'contrainte',
                               'date_diagnostic',
                               'observation_travaux'
                               ]
description_features_num = ['matricule_arbre',
                            'controle',
                            'surf_permeable',
                            'date_plantation',
                            'hauteur',
                            'diametre',
                            'circonference (en cm)',
                            'esperance_maintien',
                            'Long',
                            'Lat'
                            ]
target_features = ['classification_diagnostic']

# Correspondence between categories and int8 categories
# Mapping int to categories
int_to_cat = {
    -1: "NaN",
    0: "C2",
    1: "C1",
    2: "C3",
    3: "C4",
    4: "C5"
}

# Mapping categories to int
cat_to_int = {v: k for k, v in int_to_cat.items()}

_event_label_int = list(int_to_cat)

Predictions = rw.prediction_types.make_multiclass(label_names=_event_label_int)
workflow = rw.workflows.Classifier()

score_types = [
    rw.score_types.BalancedAccuracy(
        name="bal_acc", precision=3, adjusted=False
    ),
    rw.score_types.Accuracy(name="acc", precision=3),
]


def _get_data(path=".", specification=None):
    # Load data from csv files into pd.DataFrame
    #
    # returns X (input) and y (output) arrays

    if specification is not None:
        data = pd.read_csv(
            os.path.join(path, "data", "sgl-arbres-urbains-wgs84.csv"))
    else:
        data = pd.read_csv(
            os.path.join(path, "data", specification + ".csv"))
    # Dataset
    X_cat = data[description_features_cat]
    X_string = data[description_features_string]
    X_num = data[description_features_num]
    X = pd.concat([X_cat, X_string, X_num], axis=1)

    # Labels
    y = data[target_features]
    y_encoded = np.array(
        y['classification_diagnostic'].map(cat_to_int).fillna(-1).astype(
            'int8'))
    return X, y_encoded


def get_train_data(path="."):
    f_name = 'train'
    return _get_data(path, f_name)


def get_test_data(path="."):
    f_name = 'test'
    return _get_data(path, f_name)


def get_cv(X, y):
    # using 5 folds as default
    k = 3
    # up to 10 fold cross-validation based on 5 splits, using two parts for
    # testing in each fold
    n_splits = 5
    cv = StratifiedKFold(n_splits=n_splits)
    splits = list(cv.split(X, y))
    # 5 folds, each point is in test set 4x
    # set k to a lower number if you want less folds
    pattern = [
        ([2, 3, 4], [0, 1]),
        ([0, 1, 4], [2, 3]),
        ([0, 2, 3], [1, 4]),
        ([0, 1, 3], [2, 4]),
        ([1, 2, 4], [0, 3]),
        ([0, 1, 2], [3, 4]),
        ([0, 2, 4], [1, 3]),
        ([1, 2, 3], [0, 4]),
        ([0, 3, 4], [1, 2]),
        ([1, 3, 4], [0, 2]),
    ]
    for ps in pattern[:k]:
        yield (
            np.hstack([splits[p][1] for p in ps[0]]),
            np.hstack([splits[p][1] for p in ps[1]]),
        )
