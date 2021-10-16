CREATE TABLE ROTATED as select x_, y_, z_ from
(select X*X_+Y*Y_+Z*Z_ as x_, X, Y, Z, new_coord from POINT cross join ROTATE where new_coord='x') as A
inner join
(select X*X_+Y*Y_+Z*Z_ as y_, X, Y, Z, new_coord from POINT cross join ROTATE where new_coord='y') as B
on A.X=B.X and A.Y=B.Y and A.Z=B.Z
inner join
(select X*X_+Y*Y_+Z*Z_ as z_, X, Y, Z, new_coord from POINT cross join ROTATE where new_coord='z') as C
on B.X=C.X and B.Y=C.Y and B.Z=C.Z;