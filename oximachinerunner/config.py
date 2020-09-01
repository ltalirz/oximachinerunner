# -*- coding: utf-8 -*-
"""Configures paths, the available models and the default models"""
import os

LIB_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(LIB_DIR, 'assets')

METAL_CENTER_FEATURES = [
    'column',
    'row',
    'valenceelectrons',
    'diffto18electrons',
    'sunfilled',
    'punfilled',
    'dunfilled',
]
GEOMETRY_FEATURES = ['crystal_nn_fingerprint', 'behler_parinello']
CHEMISTRY_FEATURES = ['local_property_stats']

FEATURES_ALL = CHEMISTRY_FEATURES + METAL_CENTER_FEATURES + ['crystal_nn_fingerprint', 'behler_parinello']

MODEL_DEFAULT_MAPPING = {'all': 'all_20200830', 'mof': 'mof_chemarxiv'}
MODEL_CONFIG = {
    'all_20200830': {
        'scaler': {
            'md5': 'aa0e86464ec3ac60449d872097f54c05',
            'url': 'https://www.dropbox.com/s/qz8c06iupx7cy5h/scaler.joblib?dl=1',
            'path': os.path.join(ASSETS_DIR, 'all_202000830', 'scaler.joblib')
        },
        'classifier': {
            'md5': 'dc0dc74b860878a53fd0f5edf5d1ba57',
            'url': 'https://www.dropbox.com/s/lc2z4abaycjbbe1/classifier.joblib?dl=1',
            'path': os.path.join(ASSETS_DIR, 'all_202000830', 'classifier.joblib')
        },
        'features': FEATURES_ALL
    },
    'mof_chemarxiv': {
        'scaler': {
            'md5': 'c5c22e22137afaa7d815b0162753b424',
            'url': 'https://www.dropbox.com/s/e2x0oqo4id61iff/scaler.joblib?dl=1',
            'path': os.path.join(ASSETS_DIR, 'mof_chemarxiv', 'scaler.joblib')
        },
        'classifier': {
            'md5': '2fee4c35f475fa2f8123e7451f6a2f74',
            'url': 'https://www.dropbox.com/s/jr22xflk5qeddcy/classifier.joblib?dl=1',
            'path': os.path.join(ASSETS_DIR, 'mof_chemarxiv', 'classifier.joblib')
        },
        'features': ['local_property_stats'] + [
            'column',
            'row',
            'valenceelectrons',
            'diffto18electrons',
            'sunfilled',
            'punfilled',
            'dunfilled',
        ] + ['crystal_nn_no_steinhardt']
    }
}
