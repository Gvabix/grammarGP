import com.google.gson.Gson;

public class programSerialization {

    public static String serializeProgram(String program) {
        Gson gson = new Gson();
        return gson.toJson(program);
    }

    public static String deserializeProgram(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, String.class);
    }
}
