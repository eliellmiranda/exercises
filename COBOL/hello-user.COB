      ******************************************************************
      * A simple COBOL program that showcases user interaction through
      * input and output operations. It asks for the user's name
      * and displays a customized greeting message.
      ******************************************************************

       IDENTIFICATION DIVISION.

       PROGRAM-ID. HELLO-USER.
       AUTHOR. ELIEL MIRANDA.
       DATE-WRITTEN. 2025-10-14.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME        PIC X(30).
       01 WS-GREETING    PIC X(30).

       PROCEDURE DIVISION.
           DISPLAY 'WHAT IS YOUR NAME?'
           ACCEPT WS-NAME
           STRING "HELLO, " WS-NAME DELIMITED BY SIZE
               INTO WS-GREETING
           DISPLAY WS-GREETING
           STOP RUN.
       END PROGRAM HELLO-USER.
