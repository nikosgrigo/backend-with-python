import converter as m

def test_is_valid_convertion():
    #Valid units
    assert m.is_valid_convertion("meters","feet") == True
    assert m.is_valid_convertion("METERS","feet") == True
    assert m.is_valid_convertion("meter PEr second","feet per second") == True
    assert m.is_valid_convertion("pascal","BAR") == True
    assert m.is_valid_convertion("pascal","pound per square inch") == True

    #Invalid units
    assert m.is_valid_convertion("m","feet") == False
    assert m.is_valid_convertion("axax","feet per second") == False
    assert m.is_valid_convertion("pascal","skoko") == False
    assert m.is_valid_convertion("258","bar") == False
    assert m.is_valid_convertion("kilogram","6") == False
    assert m.is_valid_convertion("","acre") == False
    assert m.is_valid_convertion("celsius","") == False
    assert m.is_valid_convertion("","") == False

# Driver code
if __name__ == "__main__":
    test_is_valid_convertion()
     