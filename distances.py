import lang2vec.lang2vec as l2v
import numpy as np


def get_lang2vec_low_cov(lang_codes, threshold=0.95):
    syn_features = l2v.get_features(
        lang_codes,
        l2v.fs_concatenation(
            [l2v.fs_union(["syntax_wals", "syntax_sswl", "syntax_ethnologue"])]
        ),
    )

    low_cov = []
    for iso in lang_codes:
        syn_missing = syn_features[iso].count("--") / len(syn_features[iso])
        if syn_missing > threshold:
            low_cov.append(iso)

    return low_cov


def get_syn_dict(df, langs, norm=False):
    matrix = np.array(df.set_index("G_CODE").loc[langs].reset_index()[langs])
    np.fill_diagonal(matrix, np.nan)
    if norm:
        return np.nanmean(matrix) / len(matrix)
    else:
        return np.nanmean(matrix)


def get_gb_feature_cov(gb, treat_as_missing):
    max_coverage_per_feature = dict()
    for i, (feature_name, series) in enumerate(gb.items()):
        if not feature_name.startswith("GB"):
            continue
        max_coverage_per_feature[feature_name] = {
            i for i in series.unique() if i not in treat_as_missing
        }
    return max_coverage_per_feature
