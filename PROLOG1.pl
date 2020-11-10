fac_sub(ODEMVC,f1).
fac_sub(FCS,f2).
fac_sub(DLD,f3).
fac_sub(DSGT,f4).
fac_sub(DTL,f5).
fac_sub(PPL,f6).
fac_sub(DSA-1,f7).

dep_sub(Comp_dep, DSA-1).
dep_sub(Comp_dep, PPL).
dep_sub(Comp_dep, DLD).
dep_sub(Comp_dep, DTL).
dep_sub(Comp_dep, DSGT).
dep_sub(Instru_dep, FCS).
dep_sub(Maths_dep, ODEMVC).

dep_stud(Comp_dep, S1).
dep_stud(Maths_dep, S2).
dep_stud(Instru_dep, S3).


dep_fac(X,Z) :- dep_sub(X,Y) , fac_sub(Y,Z).
