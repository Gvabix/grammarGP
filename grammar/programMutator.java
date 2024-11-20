import java.util.Random;

public class programMutator {

    private static Random rand = new Random();

    // Mutacja: zmiana losowej części programu
    public static String mutate(String program) {
        int mutatePoint = rand.nextInt(program.length());
        String mutatedProgram = program.substring(0, mutatePoint) + (rand.nextInt(100) + 1) + program.substring(mutatePoint);
        return mutatedProgram;
    }
}
