
import java.util.*;

public class RetainAll {

    public static void retainAll(Set<Integer> s1, Set<Integer> s2) {
        
        Iterator<Integer> iterator = set.iterator();
        while(iterator.hasNext()) {
            Integer setElement = iterator.next();
            if(!s2.contains(setElement)) {
                iterator.remove();
            }
    }

            while (iter.hasNext()) {
            Integer set1 = iter.next();
            System.out.println(set1);
            Integer set2 = iter2.next();
            System.out.println(set2);
            if (set1 != set2) {
                iter.remove();  
            }
        }
    }

    public static void main(String[] args) {
        // Write testing code here!
    }

}