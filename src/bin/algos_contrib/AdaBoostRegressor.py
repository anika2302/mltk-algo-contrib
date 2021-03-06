#!/usr/bin/env python

from pandas import DataFrame
from sklearn.ensemble import AdaBoostRegressor as _AdaBoostRegressor

from base import RegressorMixin, BaseAlgo
from util.param_util import convert_params
from util.algo_util import handle_max_features
from codec import codecs_manager


class AdaBoostRegressor(RegressorMixin, BaseAlgo):
    def __init__(self, options):
        self.handle_options(options)
        params = options.get('params', {})
        out_params = convert_params(
            params,
            strs=['loss', 'max_features'],
            floats=['learning_rate'],
            ints=['n_estimators'],
        )

        self.estimator = _AdaBoostRegressor(**out_params)


    @staticmethod
    def register_codecs():
        from codec.codecs import SimpleObjectCodec, TreeCodec

        codecs_manager.add_codec('algos.AdaBoostRegressor', 'AdaBoostRegressor', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.ensemble.classes', 'AdaBoostRegressor', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.tree.tree', 'DecisionTreeRegressor', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.ensemble.weight_boosting', 'AdaBoostRegressor', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.tree._tree', 'Tree', TreeCodec)
