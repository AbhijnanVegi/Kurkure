SELECT COUNT(DOC_ID) AS LOTUS_COUNT FROM(
    SELECT BW2, DOC_ID FROM
     (SELECT WORD1, WORD2,DOC_ID FROM ENTITY WHERE WORD1="BJP") AS C 
         INNER JOIN 
     (SELECT AW1, BW2, ADOC_ID FROM
          (SELECT WORD1 AS AW1, WORD2 AS AW2, DOC_ID AS ADOC_ID FROM ENTITY) AS A 
              INNER JOIN 
          (SELECT WORD1 AS BW1, WORD2 AS BW2, DOC_ID AS BDOC_ID FROM ENTITY) AS B
              ON AW2=BW1 WHERE ADOC_ID=BDOC_ID) AS D
         ON WORD2=AW1 WHERE ADOC_ID=DOC_ID 
    ) AS E WHERE BW2="Lotus";