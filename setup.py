# -*-coding:utf-8-*-
# cython:language_level=3
import os
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np


def build_ext():
    ext = Extension(name="_sampler",
                    sources=[
                        "learnable_primitives/fast_sampler/_sampler.pyx",
                        "learnable_primitives/fast_sampler/sampling.cpp"
                    ],
                    language="c++11",
                    include_dirs=[np.get_include()],
                    )
    setup(ext_modules=cythonize(ext))


if __name__ == "__main__":
    build_ext()
