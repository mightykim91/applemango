package com.project.model.restaurant;
import lombok.*;

import javax.persistence.*;

//@ToString
//@NoArgsConstructor
@Getter @Setter
// @Builder
@Entity
@Table(name = "menu")
public class Menu {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int mid;
    private int mrid;
    private String missig;
    private String mname;
    private int mprice;
    private String mimage;
    
    public Menu() {}

    public Menu(int mid, int mrid, String missig, String mname,int mprice, String mimage) {
        this.mid = mid;
        this.mrid = mrid;
        this.missig = missig;
        this.mname = mname;
        this.mprice = mprice;
        this.mimage = mimage;
    }

    public String toSring() {
        return "mid= "+this.mid+
               " mrid= "+this.mrid+
               " missig= "+this.missig+
               " mname= "+this.mname+
               " mprice= "+this.mprice+
               " mimage= "+this.mimage;
    }
}//end of class