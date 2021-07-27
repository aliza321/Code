public class Solution {
    public int reverseBits(int n) {
        int a=0;
        for(int i=0;i<32;i++){
            a=a|(n&1);
            n=n>>1;
            if(i<31)
                a=a<<1;
        }
        return a;
    }
}
