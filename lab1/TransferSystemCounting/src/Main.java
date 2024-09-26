import java.util.Scanner;

public class Main {
    static String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static int TranslateNFromATo10(String N, int A){
        int result = 0;
        for (int i = 0; i < N.length(); i++){
            result += (int) (Math.pow(A, (N.length() - i - 1)) * alphabet.indexOf(N.charAt(i)));
        }
        return result;
    }

    public static String TranslateNFromAToB(String N, int A, int B){
        int N10 = TranslateNFromATo10(N, A);
        String result = "";
        do {
            int remainder = N10 % B;
            N10 /= B;
            if (remainder < 0){
                remainder = remainder + Math.abs(B);
                N10++;
            }
            result = alphabet.charAt(remainder) + result;
        }
        while (N10 != 0);
        return result;
    }

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        while (true){
            System.out.println("Введите ЧИСЛО СТАРАЯ_СС НОВАЯ_СС без запятых через пробел: ");
            String n = reader.next();
            int a = reader.nextInt(), b = reader.nextInt();

            if (n.contains(",") || n.contains(".")){
                System.out.println("Неверный ввод");
                continue;
            }

            String result = TranslateNFromAToB(n, a, b);

            System.out.println("Результат: " + result);
        }
    }
}