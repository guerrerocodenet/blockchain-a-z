# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:55:22 2022

@author: guerrerocodenet
"""

# Module 1. Create blockchain
# Install Flask; pip install Flask==0.12.2
# Install Postman

# Import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Create blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_Block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
        
# Part 2 - Mining blockchain

