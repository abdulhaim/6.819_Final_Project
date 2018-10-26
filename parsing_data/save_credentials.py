#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'PaOanADKNrwjA55wuwqa2JUgx'
twitter_cred['CONSUMER_SECRET'] = 'VStbBAGzymIK47IyDZm3AGLluTK8aBd11eggvwGl9rppSEWoeo'
twitter_cred['ACCESS_KEY'] = '1054191426974683137-HvTYRViMB0kLrItcBRvFLsmeiTJsUr'
twitter_cred['ACCESS_SECRET'] = '5SXbJf6xgKFJPMXZit0uv1w9b82cn6FqzHVDRBDye6vp2'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)