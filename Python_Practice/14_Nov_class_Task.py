class While1:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        if not (a > 0 and b > 0 and a > b):
            raise ValueError("All arguments must be positive integers, and 'a' must be greater than 'b'.")

    def emty_A(self):
        temp_a = self.a

        while temp_a >= self.b:
            temp_a -= self.b
        return temp_a

# print(While1(18,5).emty_A())

class While2:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        if not (a > 0 and b > 0 and a > b):
            raise ValueError("All arguments must be positive integers, and 'a' must be greater than 'b'.")

    def how_much_B(self):
        temp_a = self.a
        result = 0

        while temp_a >= self.b:
            temp_a -= self.b
            result += 1

        return result


# print(While2(26,5).how_much_B())

class While3:
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        if not (n > 0 and k > 0):
            raise ValueError("Both 'n' and 'k' must be greater than 0.")

    def residual(self):
        residuals = self.n
        wholes = 0

        while residuals >= self.k:
            residuals -= self.k
            wholes += 1

        return {'residual': residuals, 'whole': wholes}


# print(While3(13,3).residual())

class While4:
    def __init__(self, n: int):
        self.n = n
        if not (n > 0):
            raise ValueError("Argument 'n' must be greater than 0.")

    def threes_power(self):
        if self.n == 1:
            return 0

        current_power = 1
        power = 0
        while current_power < self.n:
            power += 1

            old_value = current_power
            current_power+= old_value
            current_power+= old_value

            if current_power > self.n:
                return "Not a power of 3"

        if current_power == self.n:
            return power
        else:
            return "Not a power of 3"

print(While4(81).threes_power())


class While5:
    def __init__(self, n: int):
        self.n = n
        if not (n > 0):
            raise ValueError("Argument 'n' must be greater than 0.")
    def twos_power(self):
        if self.n == 1:
            return 0
        current_power = 1
        power = 0
        while current_power < self.n:
            power += 1
            old_value = current_power
            current_power+= old_value
            current_power+= old_value
            if current_power > self.n:
                return "Not a power of 2"