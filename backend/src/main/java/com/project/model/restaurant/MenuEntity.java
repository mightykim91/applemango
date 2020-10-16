package com.project.model.restaurant;
import lombok.*;

import javax.persistence.*;

//@ToString
//@NoArgsConstructor
@Getter @Setter
// @Builder
@Entity
@Table(name = "menu")
public class MenuEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int mid;
    private int mrid;
    private boolean missig;
    private String mname;
    private int mprice;
    private String mimage;
    
    public MenuEntity() {}

    public MenuEntity(int mrid, boolean missig, String mname,int mprice, String mimage) {
        this.mrid = mrid;
        this.missig = missig;
        this.mname = mname;
        this.mprice = mprice;
        this.mimage = mimage;
    }

   
    public boolean getmissig() {
        return this.missig;
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