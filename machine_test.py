from machine import VendingMachine
from machine import TextMachine

def test_TextMachineClass():
    """
    Print Done if all tests passed
    """
    print("Testing TextMachine class...", end="")
    # Text machines have four main properties:
    # how many text of two type they contain and the price of each type text.
    # A new text machine starts with two texts type.
    tm1 = TextMachine((75, 125), (25, 245))
    assert (str(tm1) == "Text Machine:<75 texts; ₴1.25 each>; "
                        "<25 texts; ₴2.45 each>")
    assert not tm1.is_empty()
    assert tm1.texts_count() == (75, 25)
    assert tm1.still_owe() == (125, 245)

    # When the user inserts money and text type, the machine returns
    # a message about their status and any change they need as a tuple.
    assert tm1.insert_money((20, 'short')) == ("Still owe ₴1.05", 20)
    assert tm1.still_owe() == (105, 245)
    assert tm1.texts_count() == (75, 25)
    assert tm1.insert_money((5, 'short')) == ("Still owe ₴1.00", 25)

    # When the user has paid enough money, they get a text and
    # the money owed resets.
    assert tm1.insert_money((100, 'short')) == ("Got a text!", 125)
    assert tm1.texts_count() == (74, 25)
    assert tm1.still_owe() == (125, 245)
    assert (str(tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                        "<25 texts; ₴2.45 each>")

    # If the user pays too much money, they get their change back
    # with the text.
   
    assert tm1.insert_money((500, 'long')) == ("Got a text!", 255, 
                                    "You can buy 1 long text or 2 short text")
    assert tm1.texts_count() == (74, 24)
    assert tm1.still_owe() == (125, 245)
    assert (str(tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                        "<24 texts; ₴2.45 each>")

    # Machines can be placed in different places
    tmr = TextMachine.railway_station_machine()
    assert (str(tmr) == "Text Machine:<200 texts; ₴2.25 each>; "
                        "<200 texts; ₴3.45 each>")

    # Machines can become empty
    tm2 = TextMachine((1, 120), (0, 245))
    assert str(tm2) == "Text Machine:<1 texts; ₴1.20 each>"
    assert not tm2.is_empty()
    assert tm2.insert_money((120, "short")) == ("Got a text!", 120)
    assert tm2.texts_count() == (0, 0)
    assert tm2.is_empty()
    assert str(tm2) == "Text Machine:<0 texts; ₴1.20 each>"

    # Once a machine is empty, 
    # it should not accept money until it is restocked.
    assert tm2.insert_money((25, "short")) == ("Machine is empty", 25)
    assert tm2.insert_money((120, "short")) == ("Machine is empty", 120)
    assert tm2.still_owe() == (120, 245)
    tm2.stock_machine((20, 20))  # Does not return anything
    assert tm2.texts_count() == (20, 20)
    assert not tm2.is_empty()
    assert (str(tm2) == "Text Machine:<20 texts; ₴1.20 each>; "
                        "<20 texts; ₴2.45 each>")
    assert tm2.insert_money((25, "short")) == ("Still owe ₴0.95", 25)
    assert tm2.still_owe() == (95, 245)
    tm2.stock_machine((20, 0))
    assert tm2.texts_count() == (40, 20)

    # We should be able to test machines for basic functionality
    tm3 = TextMachine((25, 100), (25, 200))
    tm4 = TextMachine((25, 100), (25, 200))
    tm5 = TextMachine((20, 100), (15, 200))
    tm6 = TextMachine((25, 120), (25, 245))
    tm7 = "Text Machine"
    assert isinstance(tm3, TextMachine)
    assert isinstance(tm4, VendingMachine)
    assert tm3 == tm4
    assert tm3 != tm5
    assert tm3 != tm6
    assert tm3 != tm7  # should not crash!
    tm_set = set()
    assert tm3 not in tm_set
    tm_set.add(tm4)
    assert tm3 in tm_set
    tm_set.remove(tm4)
    assert tm3 not in tm_set
    assert tm4.insert_money((50, "short")) == ("Still owe ₴0.50", 50)
    assert tm3 != tm4

    print("Done!")

test_TextMachineClass()
