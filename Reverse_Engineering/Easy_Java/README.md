
# Easy_Java

Difficulty Level: Warmup

I am new to Java programming so I made a simple program to play with it. However, I have lost the source code.

### Hints

- No hints


## Deployment

Compile the java program: javac generate/generate.java  and upload generate.class in distrib to static file server.

- generate.class
    - SHA1: 9ab3dabb0aee650e3d2fb76fdbb9dd7b343777c2
    - Java bytecode file


## Solution

Using a decompiler, such as [JD-GUI](http://java-decompiler.github.io/), we can translate the bytecode back to Java code as shown below: 


```java
public class generate
{
  public static void main(String[] paramArrayOfString) {
    System.out.println("Hello, World!");
    
    int[] arrayOfInt1 = { 104, 114, 51, 51, 95, 98, 49, 108, 108, 49, 48, 110, 95, 100, 51, 118, 49, 99, 51, 53, 55 };
    int[] arrayOfInt2 = new int[arrayOfInt1.length];

    for (byte b1 = 0; b1 < arrayOfInt1.length; b1++) {
      arrayOfInt2[(b1 + true) % arrayOfInt1.length] = arrayOfInt1[b1];
    }

    String str1 = "";
    
    for (byte b2 = 0; b2 < arrayOfInt2.length; b2++) {
      str1 = str1 + (char)arrayOfInt2[b2];
    }
    
    String str2 = "19C4{" + str1 + "}";
  }
}
```

We can see that the flag contents are generated from the variable `str1`, we can attain the flag by adding a print statement to print the contents of `str1`.

### Flag
`19C4{Java_!$_&uN}`
