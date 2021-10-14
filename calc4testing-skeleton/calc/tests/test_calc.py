import unittest
import json
from flask import request, jsonify
from calc import app

app.testing = True

# TODO: Extend these component tests for the calc view
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):
    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "8")

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/div?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "DivisionByZeroError")

    
    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=3&n=3").get_json()
        self.assertEqual(reply["result"],"9" )    
    
        
   
    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=5&n=5").get_json()
        self.assertEqual(reply["result"],"0" )

    def test_sub2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=5&n=-5").get_json()
        self.assertEqual(reply["result"],"10" )