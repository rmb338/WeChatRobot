#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import requests
from random import randint
import SparkApi


class Spark():
    def __init__(self, tbconf=None) -> None:
        self.LOG = logging.getLogger(__file__)
        self.appid = tbconf["appid"]
        self.Spark_url = tbconf["Spark_url"]
        self.domain = tbconf["domain"]
        self.api_secret = tbconf["api_secret"]
        self.api_key = tbconf["api_key"]
        self.text=[]
        self.fallback = ["我还不能理解你说了什么", "功能正在开发", "出BUG啦,开发被祭天了"]

    def getText(self,role,content):
        jsoncon = {}
        jsoncon["role"] = role
        jsoncon["content"] = content
        self.text.append(jsoncon)
        return self.text

    def get_answer(self, msg: str, sender: str = None) -> str:
        question = self.getText("user",msg)
        rsp = ""
        try:
            SparkApi.answer =""
            SparkApi.main(self.appid,self.api_key,self.api_secret,self.Spark_url,self.domain,question)
            rsp = SparkApi.answer
        except Exception as e:
            self.LOG.error(f"{e}: {question}\n{rsp}")
            idx = randint(0, len(self.fallback) - 1)
            rsp = self.fallback[idx]

        return rsp


if __name__ == "__main__":
    from configuration import Config
    c = Config()
    print("%s",c)
    sparkbot = Spark(c.SPARK)
    rsp = sparkbot.get_answer("你还活着？")
    print(rsp)
