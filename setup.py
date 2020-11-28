# -*- coding: utf-8 -*-
import codecs
from setuptools import setup

packages = \
['colour_hdri',
 'colour_hdri.calibration',
 'colour_hdri.calibration.tests',
 'colour_hdri.exposure',
 'colour_hdri.exposure.tests',
 'colour_hdri.generation',
 'colour_hdri.generation.tests',
 'colour_hdri.models',
 'colour_hdri.models.datasets',
 'colour_hdri.models.tests',
 'colour_hdri.plotting',
 'colour_hdri.process',
 'colour_hdri.process.tests',
 'colour_hdri.recovery',
 'colour_hdri.recovery.tests',
 'colour_hdri.sampling',
 'colour_hdri.sampling.tests',
 'colour_hdri.tonemapping',
 'colour_hdri.tonemapping.global_operators',
 'colour_hdri.tonemapping.global_operators.tests',
 'colour_hdri.utilities',
 'colour_hdri.utilities.tests']

package_data = \
{'': ['*'],
 'colour_hdri': ['examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_absolute_luminance_calibration_and_photometric_exposure_conversion.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_adobe_dng_sdk_colour_processing.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_global_tonemapping_operators.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_ldr_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_using_rawpy.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_merge_from_raw_files_with_post_demosaicing.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'examples/examples_variance_minimization_light_probe_sampling.ipynb',
                 'resources/colour-hdri-examples-datasets/*',
                 'resources/colour-hdri-tests-datasets/*']}

install_requires = \
['colour-science>=0.3.16,<0.4.0', 'recordclass']

extras_require = \
{'development': ['biblib-simple',
                 'coverage',
                 'coveralls',
                 'flake8',
                 'invoke',
                 'jupyter',
                 'mock',
                 'nbformat>=4,<5',
                 'nose',
                 'pre-commit',
                 'pytest',
                 'restructuredtext-lint',
                 'sphinx<=3.1.2',
                 'sphinx_rtd_theme',
                 'sphinxcontrib-bibtex',
                 'toml',
                 'twine',
                 'yapf==0.23'],
 'optional': ['colour-demosaicing', 'rawpy'],
 'plotting': ['backports.functools_lru_cache', 'matplotlib'],
 'read-the-docs': ['mock', 'numpy', 'sphinxcontrib-bibtex']}

setup(
    name='colour-hdri',
    version='0.1.8',
    description='HDRI / Radiance image processing algorithms for Python',
    long_description=codecs.open('README.rst', encoding='utf8').read(),
    author='Colour Developers',
    author_email='colour-developers@colour-science.org',
    maintainer='Colour Developers',
    maintainer_email='colour-developers@colour-science.org',
    url='https://www.colour-science.org/',
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
)
