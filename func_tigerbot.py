#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import requests
from random import randint


class TigerBot():
    def __init__(self, tbconf=None) -> None:
        self.LOG = logging.getLogger(__file__)
        self.tburl = "https://api.tigerbot.com/bot-service/ai_service/gpt"
        self.tbheaders = {"Authorization": "Bearer " + tbconf["key"]}
        self.tbmodel = tbconf["model"]
        self.fallback = ["我还不能理解你说了什么", "功能正在开发", "出BUG啦,开发被祭天了"]

    def get_answer(self, msg: str, sender: str = None) -> str:
        payload = {
            "text": msg,
            "modelVersion": self.tbmodel
        }
        rsp = ""
        try:
            rsp = requests.post(self.tburl, headers=self.tbheaders, json=payload).json()
            rsp = rsp["data"]["result"][0]
        except Exception as e:
            self.LOG.error(f"{e}: {payload}\n{rsp}")
            idx = randint(0, len(self.fallback) - 1)
            rsp = self.fallback[idx]

        return rsp


if __name__ == "__main__":
    from configuration import Config
    c = Config()
    tbot = TigerBot(c.TIGERBOT)
    rsp = tbot.get_answer("你还活着？")
    print(rsp)
