
class VendingMachine:
    def __init__(self) -> None:
        pass

class TextMachine(VendingMachine):
    def __init__(self, text_1, text_2) -> None:
        self.text_1 = text_1
        self.text_2 = text_2
        self.money_given = 0
        self.short_fee = text_1[1]
        self.long_fee = text_2[1]

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, TextMachine):
            return self.__dict__ == __o.__dict__
        return False
    
    def __hash__(self) -> int:
        return hash(f"{self.text_1} {self.text_2}")
    def __str__(self) -> str:
        texts1 = f"<{self.text_1[0]} texts; ₴{round(self.text_1[1]/100, 2):.2f} each>"
        texts2 = f" <{self.text_2[0]} texts; ₴{round(self.text_2[1]/100, 2):.2f} each>" if self.text_2[0] else ""
        sep = ";" if texts1!="" and texts2!="" else ""
        return f"Text Machine:{texts1}{sep}{texts2}"
    
    def is_empty(self):
        if self.text_1[0] == 0 and self.text_2[0] == 0:
            return True
        return False
    
    def texts_count(self):
        return (self.text_1[0], self.text_2[0])
    
    def still_owe(self):
        return (self.text_1[1], self.text_2[1])
 
    def insert_money(self, money):
        if money[1] == "short":
            self.money_given += money[0]
            if self.text_1[0] == 0:
                return ("Machine is empty", money[0])
            self.text_1 = (self.text_1[0], self.text_1[1] - money[0])
            if self.text_1[1] <= 0:
                self.text_1 = (self.text_1[0] - 1, self.short_fee)
                money_left = self.money_given
                self.money_given -= self.short_fee
                return ("Got a text!", money_left)

            else:
                owe = f"{round(self.text_1[1]/100, 2):.2f}"
                # txt = f"Still owe ₴{owe}" 
                return (f"Still owe ₴{owe}", self.money_given)

        elif money[1] == "long":
            self.text_2 = (self.text_2[0], self.text_2[1] - money[0])
            self.money_given += money[0]
            if self.text_2[1] <= 0:
                self.text_2 = (self.text_2[0] - 1, self.long_fee)
                txt = "Got a text!"
                self.money_given -= self.long_fee
                return ("Got a text!", self.money_given, f"You can buy {self.money_given//self.long_fee} long text or {self.money_given//self.short_fee} short text")
            owe = f"{round(self.text_2[1]/100, 2):.2f}"
            return (f"Still owe ₴{owe}", self.money_given)
    def stock_machine(self, add):
        self.text_1 = (self.text_1[0] + add[0], self.text_1[1])
        self.text_2 = (self.text_2[0] + add[0], self.text_2[1])
    def railway_station_machine():
        return TextMachine((200, 225), (200, 345))
    
