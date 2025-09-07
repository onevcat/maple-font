import source.py.feature.ast as ast


def cv97_subst():
    return ast.subst_map(
        "…",
        target_suffix=".full",
    )


cv97_name = "Full width ellipsis (`…`)"
cv97_feat_cn = ast.CharacterVariant(
    id=97, desc=cv97_name, content=cv97_subst(), version="7.0", example="……"
)
