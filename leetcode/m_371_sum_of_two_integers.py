class Solution:
    def getSum(self, a: int, b: int) -> int:
        # since python has no 32-bits limit
        mask = 0xFFFFFFFF # bitmask of 32 1-bits
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF # bitmask of 31 1-bits

        if a < max_int:
            return a
        else:
            return ~(a ^ mask)

# java version
class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
            
        return a;
    }
}