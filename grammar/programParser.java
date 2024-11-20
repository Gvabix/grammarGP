import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class programParser {

    // Parsowanie programu
    public static boolean parseProgram(String programText) {
        try {
            // Tworzymy strumień wejściowy z tekstu programu
            CharStream input = CharStreams.fromString(programText);

            // Tworzymy leksykalizator
            grammarGPLexer lexer = new grammarGPLexer(input);
            CommonTokenStream tokens = new CommonTokenStream(lexer);

            // Tworzymy parser
            grammarGPParser parser = new grammarGPParser(tokens);

            // Parsujemy program
            ParseTree tree = parser.program();  // Zakładając, że masz regułę 'program'

            // Jeśli drzewo jest poprawnie sparsowane, zwrócimy true
            System.out.println("Program is valid!");
            return true;
        } catch (Exception e) {
            // Jeśli wystąpi błąd podczas parsowania, program jest niepoprawny
            System.out.println("Error parsing program: " + e.getMessage());
            return false;
        }
    }
}
