# -*- coding: utf-8 -*-

import os, sys
import requests
from locust import HttpUser, between, task
class MultiPost(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post('https://visit.lsmnq.com/live/?id=9994')
    
    @task
    def index(self):
        self.client.get('/')
        self.client.get('/static/assets.js')
    
    @task
    def abort(self):
        self.client.get("/about/")
        