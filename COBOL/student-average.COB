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
       01 STUDENT-GRADES.
           05 GRADE1        PIC 9(2)        VALUE 0.
           05 GRADE2        PIC 9(2)        VALUE 0.
           05 GRADE3        PIC 9(2)        VALUE 0.
       01 TOTAL             PIC 9(3)V99     VALUE 0.
       01 AVERAGE           PIC zz.99       VALUE 0.
       01 STUDENT-NAME      PIC A(30).

       PROCEDURE DIVISION.
           DISPLAY '----------------------------------'.
           DISPLAY '    STUDENT AVERAGE CALCULATOR    '.
           DISPLAY '----------------------------------'.
           DISPLAY 'ENTER STUDENT NAME: '.
           ACCEPT STUDENT-NAME.

           DISPLAY 'ENTER THE FIRST GRADE: '.
           ACCEPT GRADE1.
           DISPLAY 'ENTER THE SECOND GRADE: '.
           ACCEPT GRADE2.
           DISPLAY 'ENTER THE THIRD GRADE: '.
           ACCEPT GRADE3.

           COMPUTE TOTAL = GRADE1 + GRADE2 + GRADE3.
           COMPUTE AVERAGE = TOTAL / 3.

           DISPLAY '----------------------------------'.
           DISPLAY 'STUDENT: ' STUDENT-NAME.
           DISPLAY 'AVERAGE: ' AVERAGE.
           DISPLAY '----------------------------------'.
           STOP RUN.
       END PROGRAM STUDENT-AVERAGE.
