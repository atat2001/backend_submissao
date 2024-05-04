/*
Sample program for testing. Receives an integer as an input and prints that
input + 1.
*/

import java.util.Scanner;


public class program {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        System.out.println(number + 1);
    }
}
