class BitManipulation:
    def __init__(self, n):
        self.n = n
    
    def set_count_bit(self, bit):
        return self.n | (1 << bit)

    def reset_count_bit(self, bit):
        return self.n & ~(1 << bit)
    
    def toggle_count_bit(self, bit):
        return self.n ^ (1 << bit)
    
    def check_count_bit(self, bit):
        return self.n & (1 << bit)
    
    def count_set_bits(self):
        return bin(self.n).count('1')
    
    def count_reset_bits(self):
        return bin(self.n).count('0')
        
    def is_power_of_two(self):
        return self.n & (self.n - 1) == 0
    
    def is_even(self):
        return self.n & 1 == 0
    
    def is_odd(self):
        return self.n & 1 == 1
    
    def is_prime(self):
        return self.n & 1 == 1
        
bit_manipulation = BitManipulation(10)
print("set_count_bit: ", bit_manipulation.set_count_bit(1))
print("reset_count_bit: ", bit_manipulation.reset_count_bit(1))
print("toggle_count_bit: ", bit_manipulation.toggle_count_bit(1))
print("check_count_bit: ", bit_manipulation.check_count_bit(1))
print("count_set_bits: ", bit_manipulation.count_set_bits())
print("count_reset_bits: ", bit_manipulation.count_reset_bits())
print("is_power_of_two: ", bit_manipulation.is_power_of_two())
print("is_even: ", bit_manipulation.is_even())
print("is_odd: ", bit_manipulation.is_odd())
print("is_prime: ", bit_manipulation.is_prime())