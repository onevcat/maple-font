import source.py.feature.ast as ast


def cv98_subst():
    return ast.subst_map(
        "—",
        target_suffix=".full",
    )


cv98_name = "Full width emdash (`—`)"
cv98_feat_cn = ast.CharacterVariant(
    id=98, desc=cv98_name, content=cv98_subst(), version="7.0", example="——"
)
