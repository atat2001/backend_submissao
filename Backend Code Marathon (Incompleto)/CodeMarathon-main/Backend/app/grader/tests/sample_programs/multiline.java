/*
Sample program for testing. Receiving and outputting multiple lines. It
receives 2 numbers, prints their adition and their multiplication.
*/

import java.util.Scanner;


public class multiline {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int number1 = input.nextInt();
        int number2 = input.nextInt();
        System.out.println(number1 + number2);
        System.out.println(number1 * number2);
    }
}
