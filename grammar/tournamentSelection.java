import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.List;

public class tournamentSelection {

    private static Random rand = new Random();

    public static String tournamentSelection(List<String> population, int tournamentSize) {
        List<String> tournament = new ArrayList<>();

        for (int i = 0; i < tournamentSize; i++) {
            tournament.add(population.get(rand.nextInt(population.size())));
        }

        String best = tournament.get(0);
        double bestFitness = fitnessEvaluator.fitness(best);
        for (String individual : tournament) {
            double currentFitness = fitnessEvaluator.fitness(individual);
            if (currentFitness > bestFitness) {
                best = individual;
                bestFitness = currentFitness;
            }
        }

        return best;
    }
}

