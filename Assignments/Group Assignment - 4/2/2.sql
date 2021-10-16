SELECT WordB2, DOC_ID FROM
     (SELECT WORD1, WORD2, DOC_ID 
     FROM ENTITY 
     WHERE WORD1 = "Pizza") 
        INNER JOIN 
     (SELECT AW1, WordB2, ADOC_ID FROM
          (SELECT WORD1 AS AW1, WORD2 AS AW2, DOC_ID AS ADOC_ID FROM ENTITY)
              INNER JOIN 
          (SELECT WORD1 AS BW1, WORD2 AS WordB2, DOC_ID AS BDOC_ID FROM ENTITY)
              ON AW2=BW1 WHERE ADOC_ID=BDOC_ID)
         ON WORD2=AW1 WHERE ADOC_ID=DOC_ID;