from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *
import pytest
def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize(
    "test_input,key,decrypted",
     [("Anas",8,"Ivia"),
      ("Hello World",6,'Nkrru Cuxrj'),
      ("Nice to meet you", 42,'Dysu je cuuj oek')]
     )

def test_encrypting(test_input,key,decrypted):
    actual=encrypt(test_input,key)
    assert actual == decrypted
 

@pytest.mark.parametrize(
    "test_input,key,decrypted",
     [("Anas",8,"Ivia"),
      ("Hello World",6,'Nkrru Cuxrj'),
      ("Nice to meet you", 42,'Dysu je cuuj oek')]
     )

def test_decrypting(test_input,key,decrypted):
 actual=decrypt(decrypted,key)
 assert  actual == test_input



@pytest.mark.parametrize(
    "test_input,decrypted",
     [(("Good man",8),"Owwl uiv"),
      (("Hello World",6),'Nkrru Cuxrj'),
      (("Nice to meet you", 16),'Dysu je cuuj oek')]
     )


def test_crack(test_input,decrypted):
    actual=crack(decrypted)
    assert actual == test_input