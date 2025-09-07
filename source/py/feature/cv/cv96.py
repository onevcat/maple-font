import source.py.feature.ast as ast


def cv96_subst():
    return ast.subst_map(
        [
            "“",
            "”",
            "‘",
            "’",
        ],
        target_suffix=".full",
    )


cv96_name = "Full width quotes (`“` / `”` / `‘` / `’`)"
cv96_feat_cn = ast.CharacterVariant(
    id=96, desc=cv96_name, content=cv96_subst(), version="7.0", example="“‘’”"
)
