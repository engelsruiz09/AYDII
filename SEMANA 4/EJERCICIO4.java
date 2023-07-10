//mi solucion para este problema es Interfaz para los comportamientos (WeaponBehavior) con el metodo useWeapon() con esto hago que cada implementacion 
// concreta de esta interfaz
//representara un comportamiento diferente, para las clases character y sus subclases Queen , king, Troll, Knight,  el comportamiento WeaponBehavior
//puede cambiar. Para el metodo setWeapon() debe estar en la clase Character por que le permite cambiar el comportamiento del arma en tiempo de
//ejecucion.

public interface WeaponBehavior {   // Interfaz de estrategia
    void useWeapon();
}

// Implementao las estrategia
public class AxeBehavior implements WeaponBehavior {
    public void useWeapon() {}
}
public class SwordBehavior implements WeaponBehavior {
    public void useWeapon() {}
}

public class KnifeBehavior implements WeaponBehavior {
    public void useWeapon() {}
}

public class BowAndArrowBehavior implements WeaponBehavior {
    public void useWeapon() {}
}


public abstract class Character {  // utilizo la estrategia
    protected WeaponBehavior weapon;

    public void setWeapon(WeaponBehavior w) {
        this.weapon = w;
    }

    public void fight() {
        weapon.useWeapon();
    }
}

public class King extends Character {  // Subclases de Character
    public King() {
        weapon = new SwordBehavior(); 
    }
}

public class Queen extends Character {  
    public Queen() {
        weapon = new KnifeBehavior(); 
}

public class Knight extends Character {
    public Knight() {
        weapon = new BowAndArrowBehavior(); 
    }


public class Troll extends Character {
    public Troll() {
        weapon = new AxeBehavior(); 
}

}
