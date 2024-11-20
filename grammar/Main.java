import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<String> population = new ArrayList<>();

        // Generowanie początkowej populacji
        for (int i = 0; i < 10; i++) {
            population.add(programGenerator.generateValidProgram());
        }

        // Krzyżowanie dwóch programów
        String parent1 = population.get(0);
        String parent2 = population.get(1);
        String offspring = programCrossover.crossover(parent1, parent2);

        // Mutacja programu
        String mutatedProgram = programMutator.mutate(offspring);

        // Selekcja turniejowa
        String selectedProgram = tournamentSelection.tournamentSelection(population, 3);

        // Funkcja przystosowania
        double fitness = fitnessEvaluator.fitness(selectedProgram);
        System.out.println("Fitness of selected program: " + fitness);

        // Serializacja programu
        String serialized = programSerialization.serializeProgram(selectedProgram);
        System.out.println("Serialized program: " + serialized);

        // Deserializacja programu
        String deserialized = programSerialization.deserializeProgram(serialized);
        System.out.println("Deserialized program: " + deserialized);
    }
}
