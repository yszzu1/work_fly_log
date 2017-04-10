

````
public class CopyOnWriteArrayListTest {

    public static void main(String[] args) {

        // List<BB> ls = new CopyOnWriteArrayList();
        List<BB> ls = new ArrayList<BB>();
        ls.add(new BB("1", "aa"));
        ls.add(new BB("1", "bb"));
        ls.add(new BB("1", "cc"));
        ls.add(new BB("2", "aa"));
        ls.add(new BB("2", "bb"));
        ls.add(new BB("2", "cc"));
        ls.add(new BB("3", "aa"));
        ls.add(new BB("3", "bb"));
        ls.add(new BB("3", "cc"));

        ListIterator<BB> it = ls.listIterator();
        String preId = null;
        while (it.hasNext()) {
            BB b = it.next();
            if (preId == null || !b.getClassId().equals(preId)) {
                preId = b.getClassId();
                it.previous();
                it.add(new BB(b.getClassId()));
                it.next();
            }
        }

        for (BB bb : ls) {
            System.out.println(bb.getClassId() + "==>" + bb.getName());
        }
    }
}

class BB {

    private String classId;
    private String name;

    public BB(String classId, String name){
        this.classId = classId;
        this.name = name;
    }

    public BB(String classId){
        this.classId = classId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getClassId() {
        return classId;
    }

    public void setClassId(String classId) {
        this.classId = classId;
    }

}
````
