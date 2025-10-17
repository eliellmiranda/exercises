      ******************************************************************
      * THIS PROGRAM READS 3 STUDENT GRADES AND CALCULATES THE AVERAGE *
      *
      *
      *
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. STUDENT-AVERAGE.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 GRADE1        PIC 9.
       01 GRADE2        PIC 9.
       01 GRADE3        PIC 9.
       77 AVERAGE       PIC 9(2)V9(2).
       PROCEDURE DIVISION.
           DISPLAY 'ENTER THE FIRST GRADE: '.
           ACCEPT GRADE1.
           DISPLAY 'ENTER THE SECOND GRADE: '.
           ACCEPT GRADE2.
           DISPLAY 'ENTER THE THIRD GRADE: '.
           ACCEPT GRADE3.
           COMPUTE AVERAGE = (GRADE1 + GRADE2 + GRADE3) / 3.
           DISPLAY 'THE AVERAGE IS: ' AVERAGE
           STOP RUN.
       END PROGRAM STUDENT-AVERAGE.
