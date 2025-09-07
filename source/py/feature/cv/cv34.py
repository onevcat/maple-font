import source.py.feature.ast as ast


def cv34_subst():
    return ast.subst_map(["k", "kcommaaccent"], target_suffix=".cv34")


cv34_name = "Alternative Italic `k` without center circle"
cv34_feat_italic = ast.CharacterVariant(
    id=34, desc=cv34_name, content=cv34_subst(), version="7.0", example="k"
)
