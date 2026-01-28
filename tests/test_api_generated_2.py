import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "https://ocapicep-internal-qa.netgear.com/api/v2"

COMMON_HEADERS = {"Content-Type": "application/json"}

# ==================== TEST FUNCTIONS ====================
import requests

COMMON_HEADERS = {"Content-Type": "application/json", "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34", "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq- Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp 2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor- jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt"}

def test_tc001_ocregister_mfa():
    """Test ID: TC001, Name: unnamed, Expected: 200 status code"""
    url = "/ocRegister_MFA"
    headers = {
        **COMMON_HEADERS,
    }
    payload = {"firstName": "fnamedemo", "lastName": "lnamedemo", "email": "aqdassss12s22@yopmail.com", "password": "Pass@1", "country": "IN", "language": "en", "receiveCommunications": "0", "mailProgram": "1"}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert 'meta' in response.json()
    assert 'data' in response.json()

import requests

COMMON_HEADERS = {
    "Content-Type": "application/json",
    "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
    "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq- Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp 2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor- jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt"}

def test_tc002_ocregister_mfa():
    """Test ID: TC002, Name: unnamed, Expected: 200 status code"""
    url = "/ocRegister_MFA"
    headers = {
        **COMMON_HEADERS
    }
    payload = {
        "firstName": "fnamedemo",
        "lastName": "lnamedemo",
        "email": "aqdassss12s22@yopmail.com",
        "password": "Pass@1"
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert 'meta' in response.text

import requests

COMMON_HEADERS = {
    "Content-Type": "application/json",
    "x-dreamfactory-api-key": "175208f843081dc7d9addad1e372c51c04c4c3dd54834a500d85955f71742a34",
    "x-dreamfactory-session-token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNlYXJjaGJsb3hAbmV0Z2Vhci5jb20iLCJleHAiOjE2OTE0NzgxNzQsImlhdCI6MTY5MTQ3Nzg3NH0.AYmd5-ya1OH6G-ap95Z2Ju_zCO8at2YRNxn62K5HfuplSfAdI1bJYUcRfH_GRtvIWcI8Ev2CEWaGYwKRFco21vYMeL9RsNkIG3eZx4w6b23El9stsBbAWbI7uj0UA5419_xmi miTza7U9HWEkhsfiprdu5H6FithbXx9t4YUGUj3uNC_mczEq- Kl_ZAeTp_075ArG3gGC7YjzHfa2pT2kp7gp4fIsp6saewvfjYeo6DKluW9PvkpWjHXW0aTLQTx3G7mnY42Z3vBApWJeBmYa5FHAgOsFN4bqSeGfjtCQecp 2_K2j4WnKN2iKgxFrKS2Mi5H894-G1rhs7lMmxRQK1nj1ns_pRNKazXkJJAaPYTYIIskfHabjmD9lTpiCf3qNTeNiCQ_DqG59MbBs-TtIZuXGor- jZ1h9rEfaoVt3eF_2gz_PFJgkWSHtmJZWkYcYTNGv5v582hkSaz4g_09Sl3Zb0ICGxTf9eeGL6XEOEjhG3UjCcvm-5ddeemvYErt"
}

def test_tc003_ocregister_mfa():
    """Test ID: TC003, Name: unnamed, Expected: 200 status code"""
    url = "/ocRegister_MFA"
    headers = {
        **COMMON_HEADERS
    }
    payload = {"firstName": "fnamedemo", "lastName": "lnamedemo", "password": "Pass@1"}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert 'meta' in response.text