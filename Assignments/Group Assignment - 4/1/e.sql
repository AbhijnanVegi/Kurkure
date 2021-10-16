CREATE TABLE ROTATE(new_coord TEXT, X_ float, Y_ float, Z_ float);
INSERT INTO ROTATE VALUES('x',COS(alpha),-SIN(alpha),0),('y',SIN(alpha),COS(alpha),0),('z',0,0,1);
