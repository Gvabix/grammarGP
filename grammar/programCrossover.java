import java.util.Random;

public class programCrossover {

    private static Random rand = new Random();

    public static String crossover(String program1, String program2) {
        int splitPoint1 = rand.nextInt(program1.length());
        int splitPoint2 = rand.nextInt(program2.length());

        String newProgram = program1.substring(0, splitPoint1) + program2.substring(splitPoint2);
        return newProgram;
    }
}
