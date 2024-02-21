# Dataset Legend - Urban Tree Allocation Scheme for the Commune of Saint-Germain-en-Laye 
For use with the "sgl-arbres-urbains-wgs84.csv" or "sgl-arbres-urbainswgs84.geojson" files available on the "data.gouv.fr" platform.

## Variables dictionary
| Attribute                    | Type        | Description                                          |
|------------------------------|-------------|------------------------------------------------------|
| type_sol                     | Categorical | Ground type where the tree is planted                |
| classe_age                   | Categorical | Age classification of the tree                       |
| classe_hauteur               | Categorical | Height classification of the tree                    |
| classe_circonference         | Categorical | Circumference classification of the tree             |
| port_arbre                   | Categorical | Tree canopy shape                                    |
| vigueur_pousse               | Categorical | Vigor of tree growth                                 |
| plaie_collet                 | Categorical | Condition of the tree collar                         |
| fissure_tronc                | Categorical | Presence and type of trunk fissure                   |
| plaie_tronc                  | Categorical | Condition of the trunk                               |
| fissure_houppier             | Categorical | Presence and type of canopy fissure                  |
| bois_mort_houppier           | Categorical | Presence and distribution of deadwood in the canopy  |
| plaie_houppier               | Categorical | Condition of the canopy                              |
| esperance_maintien           | Categorical | Estimated remaining lifespan of the tree             |
| classification_diagnostic    | Categorical | Diagnosis classification of the tree's health status |
| prescription_1               | Categorical | Recommended actions for tree maintenance, phase 1    |
| prescription_2               | Categorical | Recommended actions for tree maintenance, phase 2    |
| prescription_3               | Categorical | Recommended actions for tree maintenance, phase 3    |
| type_delai_1                 | Categorical | Type of deadline for phase 1 recommendations         |
| type_delai_2                 | Categorical | Type of deadline for phase 2 recommendations         |
| delai_preconisation_2        | Categorical | Timeframe for phase 2 recommendations                |
| delai_saison_programmation_2 | Categorical | Season for scheduling phase 2 recommendations        |
| ID_ARBRE                     | String      | Unique identifier for the tree                       |
| commune                      | String      | Name of the commune where the tree is located        |
| quartier                     | String      | Name of the neighborhood or district                 |
| site                         | String      | Site description                                     |
| cote_voirie                  | String      | Side of the road where the tree is located           |
| genre_arbre                  | String      | Tree genus                                           |
| espece_arbre                 | String      | Tree species                                         |
| situation                    | String      | Tree situation or condition                          |
| champignon_collet            | String      | Fungi presence at the collar of the tree             |
| insecte_collet               | String      | Insect presence at the collar of the tree            |
| observation_collet           | String      | Observations about the collar of the tree            |
| champignon_tronc             | String      | Fungi presence on the trunk of the tree              |
| insecte_tronc                | String      | Insect presence on the trunk of the tree             |
| rejet_tronc                  | String      | Shoot presence on the trunk of the tree              |
| tuteurage_arbre              | String      | Tree staking information                             |
| canisse_arbre                | String      | Tree cane information                                |
| observation_tronc            | String      | Observations about the trunk of the tree             |
| champignon_houppier          | String      | Fungi presence in the canopy of the tree             |
| insecte_houppier             | String      | Insect presence in the canopy of the tree            |
| ecorce_incluse_houppier      | String      | Bark inclusion in the canopy of the tree             |
| observation_houppier         | String      | Observations about the canopy of the tree            |
| contrainte                   | String      | Constraints or limitations                           |
| date_diagnostic              | String      | Date of the tree diagnostic                          |
| observation_travaux          | String      | Observations about the tree works                    |
| matricule_arbre              | Numeric     | ???                                                  |
| controle                     | Numeric     | ???                                                  |
| surf_permeable               | Numeric     | Permeable surface                                    |
| date_plantation              | Numeric     | Date of tree plantation                              |
| hauteur                      | Numeric     | Height of the tree (in meters)                       |
| diametre                     | Numeric     | Diameter of the tree (in centimeters)                |
| circonference (en cm)        | Numeric     | Circumference of the tree (in centimeters)           |
| esperance_maintien           | Numeric     | Estimated remaining lifespan of the tree             |
| Long                         | Numeric     | Longitude of the tree's location                     |
| Lat                          | Numeric     | Latitude of the tree's location                      |


##  Value class abels

| Attribute         | Class | Description                                         |
|-------------------|-------|-----------------------------------------------------|
| `type_sol`        |       | Ground type where the tree is planted               |
|                   | P     | Paillage / Mulching                                            |
|                   | G     | Gazon / Turf                                               |
|                   | S     | Stabilisé / Stabilized                                           |
|                   | Gr    | Grille / Grid                                           |
|                   | GR    | Grave / Gravel                                             |
|                   | MA    | Massifs                                             |
|                   | E     | Enrobé                                              |
|                   | CS    | Couvre-sol / Ground Couvre                                          |
| `classe_age`      |       | Age class of the tree                      |
|                   | A     | Adult, 20 to 40 years                               |
|                   | JA    | Jeune Adulte / Young adult, 10 to 20 years                         |
|                   | J     | Jeune / Young, less than 10 years                            |
|                   | AM    | Mature adult, 50 to 70 years                         |
| `classe_hauteur`  |       | Height class of the tree                    |
|                   | H1    | 0 to 5m                                             |
|                   | H2    | 5 to 10m                                            |
|                   | H3    | 10 to 15m                                           |
|                   | H4    | 15 to 20m                                           |
|                   | H5    | 20 to 25m                                           |
| `classe_circonference` |   | Circumference class of the tree          |
|                   | C1    | 0 to 0.5m                                           |
|                   | C2    | 0.51 to 1m                                          |
|                   | C3    | 1.01 to 1.5m                                        |
|                   | C4    | 1.51 to 2m                                          |
|                   | C5    | 2.01m to 2.5m                                       |
|                   | C6    | 2.51 to 3m                                          |
|                   | C7    | 3.01 to 3.5m                                        |
| `port_arbre`      |       | Tree canopy shape                                   |
|                   | SL    | Semi-Libre / Semi-free                                           |
|                   | L     | Libre / Free                                                |
|                   | R5    | 5-sided curtain                                     |
|                   | RR    | Reduced released                                    |
|                   | A     | Architectural                                       |
| `vigueur_pousse`  |       | Vigor of tree growth                                |
|                   | P     | Growing                                             |
|                   | PP    | Little growth                                       |
|                   | MP    | Moderate growth                                     |
|                   | D     | Declining                                           |
| `plaie_collet`    |       | Condition of the tree collar                         |
|                   | RCPPL | No wound                                            |
|                   | RCPLS | Healthy wound                                       |
|                   | RCPLNS| Necrotic wound oozing                               |
|                   | RCPLNC| Necrotic wound cavity                               |
|                   | RCPLC | Healed wound                                        |
| `fissure_tronc`   |       | Presence and type of trunk fissure                   |
|                   | TPF   | No fissure                                          |
|                   | TFO   | Open fissure                                        |
|                   | TFF   | Closed fissure                                      |
| `plaie_tronc`     |       | Condition of the trunk                              |
|                   | TPLS  | Healthy wound                                       |
|                   | TPLCF | Closed cavity wound                                 |
|                   | TPLNC | Necrotic cavity wound                               |
|                   | TPLC  | Healed wound                                        |
|                   | TPPL  | No wound                                            |
| `fissure_houppier`|       | Presence and type of canopy fissure                  |
|                   | HPF   | No fissure                                          |
|                   | HFO   | Open fissure                                        |
| `bois_mort_houppier` |    | Presence and distribution of deadwood in the canopy |
|                   | HBMI  | Isolated deadwood                                   |
|                   | HPBM  | No deadwood                                         |
|                   | HBMU  | Uniform deadwood                                    |
| `plaie_houppier`  |       | Condition of the canopy                             |
|                   | HPLC  | Healed wound                                        |
|                   | HPLS  | Healthy wound                                       |
|                   | HPPL  | No wound                                            |
|                   | HPLNC | Necrotic cavity wound                               |
| `esperance_maintien` |     | Estimated remaining lifespan of the tree            |
|                   | 1     | Greater than 15 years                               |
|                   | 2     | 10 to 15 years                                     |
|                   | 3     | 5 to 10 years                                      |
|                   | 4     | Less than 5 years                                   |
| `classification_diagnostic` | Diagnosis classification of the tree's health status |
|                   | C0    | Empty location                                      |
|                   | C1    | Healthy tree, good vigor                            |
|                   | C2    | Tree with minor lesions                             |
|                   | C3    | Tree with significant lesions                       |
|                   | C4    | Tree with significant and evolving lesions          |
|                   | C5    | Tree with irreversible lesions requiring removal    |
|                   | C6    | Stump                                               |
| `prescription_1`, `prescription_2`, `prescription_3` | Recommended actions for tree maintenance |
|                   | tfo   | Formation pruning                                   |
|                   | tdg   | Clearance pruning                                   |
|                   | tsbm  | Deadwood removal                                    |
|                   | RC    | Canopy reduction                                    |
|                   | RT    | Stake removal                                       |
|                   | RP    | Replacement                                         |
|                   | trg   | Sucker removal, vigorous                            |
|                   | tpa   | Tree base treatment                                 |
|                   | tr    | Canopy reduction                                    |
|                   | ab    | Felling                                             |
|                   | R     | Stump grinding                                      |
|                   | sl    | Ivy removal                                         |
|                   | rg    | Base grille removal                                 |
| `type_delai_1`, `type_delai_2` | Type of deadline for recommendation/scheduling    |
|                   | a     | Recommendation                                      |
|                   | b     | Scheduling                                          |
| `delai_preconisation_2` | Timeframe for phase 2 recommendations             |
|                   | a3    | 6 to 12 months                                     |
| `delai_saison_programmation_2` | Season for scheduling phase 2 recommendations  |
|                   | b1    | Autumn                                              |
|                   | b2    | Winter                                              |
|                   | b3    | Spring                                              |
|                   | b4    | Summer                                              |