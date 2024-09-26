import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static String codeHamming(String s) {
        int countControlDigits = 1;
        while (Math.pow(2, countControlDigits) < countControlDigits + s.length() + 1) {
            countControlDigits++;
        }

        int[] code = new int[(int) Math.pow(2, countControlDigits) - 1];
        int indexSkip = 1;
        int indexString = 0;
        for (int i = 0; i < code.length; i++) {
            if (i + 1 != indexSkip) {
                code[i] = indexString < s.length() ? s.charAt(indexString) - '0' : 0;
                indexString++;
            }
            else {
                indexSkip *= 2;
            }
        }

        int[] controlDigits = new int[countControlDigits];
        for (int i = 0; i < countControlDigits; i++) {
            int lenghtLine = (int) (Math.pow(2, i));
            int controlDigit = 0;
            for (int startLine = lenghtLine - 1; startLine < code.length; startLine += 2 * lenghtLine) {
                for (int posLine = 0; posLine < lenghtLine; posLine++) {
                    controlDigit ^= code[posLine + startLine];
                }
            }
            controlDigits[i] = controlDigit;
        }

        for (int i = 0; i < countControlDigits; i++) {
            code[(int) Math.pow(2, i) - 1] = controlDigits[i];
        }

        String res = "";
        for (int i = 0; i < code.length; i++) res = res + code[i];
        return res;
    }

    public static String decodeHamming(String s){
        int[] code = new int[s.length()];
        for (int i = 0; i < s.length(); i++){
            code[i] = s.charAt(i) - '0';
        }

        int countControlDigits = 1;
        while (Math.pow(2, countControlDigits) - 1 < code.length) {
            countControlDigits++;
        }
        if (Math.pow(2, countControlDigits) - 1 != code.length) {
                return "Error";
        }

        int[] syndromDigits = new int[countControlDigits];
        int[][] tableHamming = new int[code.length][countControlDigits];
        for (int i = 0; i < countControlDigits; i++) {
            int lenghtLine = (int) (Math.pow(2, i));
            int syndromDigit = 0;
            for (int startLine = lenghtLine - 1; startLine < code.length; startLine += 2 * lenghtLine) {
                for (int posLine = 0; posLine < lenghtLine; posLine++) {
                    syndromDigit ^= code[posLine + startLine];
                    tableHamming[posLine + startLine][i] = 1;
                }
            }
            syndromDigits[i] = syndromDigit;
        }

        for (int i = 0; i < code.length; i++) {
            if (Arrays.equals(syndromDigits, tableHamming[i])) {
                code[i] ^= 1;
                break;
            }
        }

        String res = "";
        int indexSkip = 1;
        for (int i = 0; i < code.length; i++) {
            if (i + 1 != indexSkip) {
                res = res + code[i];
            }
            else {
                indexSkip *= 2;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

//        String code = codeHamming(scanner.nextLine());
//        System.out.println(code);

        String s = decodeHamming(scanner.nextLine());
        System.out.println(s);
    }
}