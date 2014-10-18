package com.rawcoders.projecteuler;

/** 
 * Solution to Problem number 1 in 3 different approaches
 *
 * @author Psycho_Coder
 */
public class MultiplesOf3And5 {

    private final int limit;

    public MultiplesOf3And5() {
        limit = 999;
    }

    private void approach1() {
        int sum = 0;
        for (int i = 3; i <= limit; i++) {
            if (i % 3 == 0) {
                sum += i;
            } else if (i % 5 == 0) {
                sum += i;
            }
        }
        System.out.println(sum);
    }

    private void approach2() {
        int sum = 0;
        for (int i = 3; i <= limit; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        System.out.println(sum);
    }

    private void approach3() {
        System.out.println(divSum(3) + divSum(5) - divSum(15));
    }

    private int divSum(int n) {
        int quo = limit / n;

        return n * (quo * (quo + 1)) / 2;
    }

    public static void main(String[] args) {
        MultiplesOf3And5 obj = new MultiplesOf3And5();
        obj.approach1();
        obj.approach2();
        obj.approach3();
    }

}
