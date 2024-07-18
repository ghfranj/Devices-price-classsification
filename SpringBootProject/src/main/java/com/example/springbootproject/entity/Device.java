package com.example.springbootproject.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Data;

@Data
@Entity
public class Device {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private int batteryPower;
    private boolean blue;
    private double clockSpeed;
    private boolean dualSim;
    private int fc;
    private boolean fourG;
    private int intMemory;
    private double mDep;
    private int mobileWt;
    private int nCores;
    private int pc;
    private int pxHeight;
    private int pxWidth;
    private int ram;
    private int scH;
    private int scW;
    private int talkTime;
    private boolean threeG;
    private boolean touchScreen;
    private boolean wifi;
    private int priceRange;
}
