import numpy as np
from sklearn.utils.testing import assert_array_almost_equal

import scanpy as sc


def test_umap_init_dtype():
    pbmc = sc.datasets.pbmc68k_reduced()
    pbmc = pbmc[:100, :].copy()
    sc.tl.umap(pbmc, init_pos=pbmc.obsm["X_pca"][:, :2].astype(np.float32))
    embed1 = pbmc.obsm["X_umap"].copy()
    sc.tl.umap(pbmc, init_pos=pbmc.obsm["X_pca"][:, :2].astype(np.float64))
    embed2 = pbmc.obsm["X_umap"].copy()
    assert_array_almost_equal(embed1, embed2)
    assert_array_almost_equal(embed1, embed2)


def test_umap_init_paga():
    pbmc = sc.datasets.pbmc68k_reduced()
    pbmc = pbmc[:100, :].copy()
    sc.tl.paga(pbmc)
    sc.pl.paga(pbmc, show=False)
    sc.tl.umap(pbmc, init_pos="paga")

    sc.tl.paga(pbmc, key_added='some_key')
    sc.pl.paga(pbmc, show=False, key='some_key')
    sc.tl.umap(pbmc, init_pos="paga", init_pos_paga_key='some_key')