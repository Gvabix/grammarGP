import java.util.Random;

public class programGenerator {

    private static Random rand = new Random();

    // Generowanie losowego programu
    public static String generateRandomProgram() {
        int type = rand.nextInt(3);
        switch (type) {
            case 0:
                return "output(" + (rand.nextInt(100) + 1) + ");";
            case 1:
                return "int x = " + (rand.nextInt(100) + 1) + ";";
            case 2:
                return "if (x > 10) { output(1); } else { output(0); }";
            default:
                return "output(0);";
        }
    }

    // Generowanie programu i sprawdzanie poprawności składniowej
    public static String generateValidProgram() {
        String program = generateRandomProgram();
        if (programParser.parseProgram(program)) {
            return program;
        } else {
            return generateValidProgram();  // Rekursja w przypadku błędnego programu
        }
    }
}

