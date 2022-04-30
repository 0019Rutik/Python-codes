public class ErrrHandeling1 {

    public static void main(String[] args) {
        try {
            throw new myException(5);
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println(e);
        }
    }

}

class myException extends Exception {
    int a;

    myException(int b) {
        a = b;
    }

    public String toString() {
        return ("Eexception number  :" + a);
    }
}
