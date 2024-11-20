public class fitnessEvaluator {

    public static double fitness(String program) {
        if (program.contains("output(1);")) {
            return 1.0; // Idealny program
        } else {
            return 0.0; // Niewłaściwy program
        }
    }
}
