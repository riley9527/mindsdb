# -*- coding: utf-8 -*-
import json
from typing import Optional, Dict

import pandas as pd

from mindsdb.integrations.libs.base import BaseMLEngine
import requests


class AIOpsHandler(BaseMLEngine):
    name = "aiops"
    headers = {'Content-Type': 'application/json'}

    def create(self, target, args=None, **kwargs):
        args = args["using"]
        args['target'] = target

        model_name = args["model_name"]
        self.model_storage.json_set('args', args)

    def describe(self, attribute: Optional[str] = None) -> pd.DataFrame:
        args = self.model_storage.json_get('args')
        return pd.DataFrame([[args]])

    def predict(self, df: pd.DataFrame, args: Optional[Dict] = None) -> pd.DataFrame:
        args = self.model_storage.json_get('args')
        target = args["target"]
        intput_column = args['input_column']
        if intput_column not in df.columns:
            raise RuntimeError(f'Column "{intput_column}" not found in input data')
        input_list = df[intput_column]
        results = []
        for item in input_list:
            params = {
                "bkdata_authentication_method": "token",
                "bkdata_data_token": "xxx",
                "bk_app_code": "data",
                "bk_app_secret": "xxx",
                "bk_ticket": "xxx",
                "data": {
                    "inputs": [
                        {
                            "timestamp": 1681181734000,
                            "input": f"\"{item}\"",
                            "action": "create",
                            "object": "Completion"
                        }
                    ]
                },
                "config": {
                    "stream": False,
                    "passthrough_input": False,
                    "predict_args":  {
                        "service_name":"openai",
                        "service_params": "{\"temperature\": 0, \"max_tokens\": 1500, \"top_p\": 1.0, \"frequency_penalty\": 0.0, \"presence_penalty\": 0.0, \"stop\": [\";\"], \"model\": \"text-davinci-003\"}"
                    }
                }
            }
            r = requests.post("xxx_url",
                              data=json.dumps(params),
                              headers={'Content-Type': 'application/json'})
            re = json.loads(r.text)

            output = re["data"]["data"]["data"][0]["output"][0]["output"]
            results.append({target: output})
        return pd.DataFrame(results)

