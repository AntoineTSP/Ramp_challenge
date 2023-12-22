import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold

import rampwf as rw

problem_title = "Urban trees: towards a clinical study"


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

score_types_1 = rw.score_types.BalancedAccuracy(
        name="bal_acc", precision=3, adjusted=False
    )

score_types_2 = rw.score_types.Accuracy(name="acc", precision=3)

score_types_3 = rw.score_types.ROCAUC(name='auc')

score_types = [
    # The official score combines the two scores with weights 2/3 and 1/3.
    rw.score_types.Combined(
        name='combined', score_types=[score_types_1,
                                      score_types_2,
                                      score_types_3],
        weights=[0.7, 0.2, 0.1], precision=3),
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
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    return cv.split(X, y)
