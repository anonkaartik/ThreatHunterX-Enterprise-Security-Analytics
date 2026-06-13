import java.util.ArrayList;
import java.util.List;

public class CorrelationEngine {

    public static void main(String[] args) {

        List<String> events = new ArrayList<>();

        events.add("Failed Login");
        events.add("Failed Login");
        events.add("Failed Login");
        events.add("Successful Login");
        events.add("Privilege Escalation");

        if (
                events.contains("Successful Login")
                        &&
                        events.contains("Privilege Escalation")
        ) {

            System.out.println("================================");
            System.out.println("THREAT ALERT");
            System.out.println("Possible Account Compromise");
            System.out.println("Severity: HIGH");
            System.out.println("================================");
        }

        else {

            System.out.println("No correlated threats detected.");

        }
    }
}