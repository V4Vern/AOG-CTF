/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Vernon Tay
 */
public class generate {
    public static void main(String args[]) {
        
         System.out.println("Hello, World!");

        int decimalArray[] = {118,97,95,33,36,95,38,117,78,74,97};
        int[] result = new int[decimalArray.length];
        
        // Rotate right by one element of array
        for(int i = 0; i < decimalArray.length; i++){
            result[(i+2) % decimalArray.length] = decimalArray[i];
        }
        String flagContent = "";

        for(int i = 0; i < result.length; i++){
            flagContent += (char)(result[i]);
        }
        
       
        String flag = "19C4{" + flagContent + "}";
    }
}