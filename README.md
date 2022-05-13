# AirportHub_Management
UTD
CS 6360.003 Database Design
Database Project Description
Team Structure:
The project is a team project for students to learn how to become effective team players in a
software project. Each team may have 4-5 students (not 1, 2, or 3 and not 6), and one student
dedicates to the team leader. Each team member must contribute to all project deliverables.
Database Management System:
You are allowed to use any DBMS that is free and available to you such as MySQL, and a database 
connector such as JDBC to connect your Java (or any other language) front-end application to your 
MySQL database.
Project Narrative:
Airport officials have decided that all information related to the airport should be organized using a
DBMS and to build an Online Airport System, and you’ve been hired to design this system. Your task
is to organize the information about all the airplanes that are stationed and maintained at the airport. The
relevant information is as follows:
▪ Every airplane has a registration number, and each airplane is of a specific model.
▪ The airport accommodates a number of airplane models, and each model is identified by a model
number (e.g., DC-10) and has a capacity and a weight.
▪ A number of technicians work at the airport. You need to store the name, SSN, address, phone 
number, and salary of each technician.
▪ Each technician is a model(s), and his or her expertise may overlap with that of other technicians. This 
information about technicians must also be recorded.
▪ Traffic controllers must have an annual medical examination. For each traffic controller, you must 
store the date of the most recent exam.
▪ All airport employees (including technicians) belong to a union. You must store the union 
membership number of each employee. You can assume that each employee is uniquely identified
by the social security number.
▪ The airport has a number of tests that are used periodically to ensure that airplanes are still airworthy. 
Each test has a Federal Aviation Administration (FAA) test number, a name, and a maximum 
possible score.
▪ The FAA requires the airport to keep track of each time that a given airplane is tested by a given 
technician using a given test. For each testing event, the information needed is the date, the number 
of hours the technician spent doing the test, and the score that the airplane received on the test.

Functional Requirements:
An initial set of functional requirements for the Online Airport System are listed below, you should 
think of and write all other needed functional requirements for this project to be complete and 
practical. 
Login Functional Requirements:
This is an initial set of login functional requirements; you may add more as needed.
1: The system will allow the user to log in.
2. The system will verify the username and password.
3. The system will not allow the user to log in with an invalid username or password.
4. The system will be able to remember usernames and passwords.
5. The system will allow users to create accounts.
6. The system will enable users to log out of their accounts
Browsing Functional Requirements:
You should provide at least 10 browsing functional requirements for the Online Airport
System
1. ______________________________________________________________
2. ______________________________________________________________
3. ______________________________________________________________
4. ______________________________________________________________
5. ______________________________________________________________
6. ______________________________________________________________
7. ______________________________________________________________
8. ______________________________________________________________
9. ______________________________________________________________
10. ______________________________________________________________
Administrator Functional requirements 
You should provide at least 10 administration functional requirements for the Online 
Airport System
1. ______________________________________________________________
2. ______________________________________________________________
3. ______________________________________________________________
4. ______________________________________________________________
5. ______________________________________________________________
6. ______________________________________________________________
7. ______________________________________________________________
8. ______________________________________________________________
9. ______________________________________________________________
10. ______________________________________________________________

Assumptions
In doing your project, you will need to make additional assumptions as well as identify the 
potential inconsistencies and resolve them. Any reasonable assumptions are fine, but they must be 
documented in your reports. 
Project Phases and Deliverables Items
Phase 1 (Due on Sunday 02/13/2022): Requirements Analysis (15%)
A system requirement specifications are due that includes:
a) System description
b) Context diagram (system architecture)
c) Functional requirements (user's operational concepts)
d) Non-functional requirements (e.g., response time, maintainability)
Phase 2 (Due on Sunday 03/06/2022): Conceptual and Logical Database Design (15%)
The following document is due for this phase
a) ER Diagram (including the description of the entities, attributes, keys, 
cardinality, andparticipation constraints)
b) Database Schema
c) List of business rules and integrity constraints of the database.
d) Interface requirements
Phase 3: (Due on Sunday 04/03/2022) Normalization and Database Implementation and
Testing (25%)
The following tasks and documents are due for this phase
a) Specify a set of functional dependencies for each relation presented then show the 
normalizationprocess and normalized tables for each relation to 3NF (if applicable).
b) Show the implementation of tables in the target DBMS (snapshots of tables in DBMS)
c) SQL statements for database construction and data population
d) Identify the functional dependencies of the database schema
e) Implementation and demonstration of the database system (snapshots of GUI)
f) Suggestions on database tuning in terms of index structures, database design, or queries.
(optional)
g) Additional queries and views (snapshots of query and view implementations)
Phase 4. (Due on Sunday 04/24/2022) Front end application (25%)
Your application program should consist of a continuous loop in which:
a) A list of at least five alternative options is offered to the user. (An additional
alternativeshould be quit.)
b) The user selects an alternative.
The last part of this assignment is to write an application that users can use to 
communicate with yourdatabase. This application should be written in a programming 
language of your choice (such as Java)that uses a DB connecter (such as JDBC) to connect 
to your database to manipulate the proper data.

c) The system prompts the user for appropriate input values.
d) The system accesses the database to perform the appropriate queries and/or modifications.
e) Data or an appropriate acknowledgment is returned to the user.
Both input and output in the application should be in a format more convenient and pleasing 
than rawinteractive SQL. Please include some interesting queries or modifications, i.e., 
operations that require some of the more complex SQL constructs such as subqueries, 
aggregates, set operators, etc. As a general example, if your database is a campus applicant
database, then your interface might include inits menu several useful queries on the database, 
with some queries performing statistical analysis requiring multiple levels of grouping, and 
other queries.
For this phase, just demonstrate this application to the TA during the final demo.
 Final Complete Project Report (Due: Monday 05/02/2022) (20%)
Submit a well written and complete report that includes the work that you have done in all the 
previous phases (one through four), The Contents of the Final Project Report should include,
but not be limited to the following sections:
1. Cover page
Provide the title of the course, the title of the project, the name of the instructor, names of
team members, and date.
2. Table of contents
Show the contents of the report and their corresponding page number.
3. Introduction
Provide a brief description of the project and the section organization of this report.
4. System Requirements
Give the context diagram (system architecture diagram) of the database system.
List the interface requirements of the system (or each subsystem).
List the functional and non-functional requirements of the database system.
5. Conceptual Design of the Database
The complete Entity-Relationship (ER) model of your database.
The data dictionary and business rules (i.e., constraints) of your ER model.
6. Logical Database Schema
Give the schema of the database which is restructured and translated from the ER diagram
presented in the section "Conceptual Design of the Database". Show the schema with
appropriate referential constraints. Give the SQL statements used to construct the schema. List
the expected database operations and estimated data volumes.
7. Functional Dependencies and Database Normalization
Identify and analyze the functional dependencies for each relation presented in the section
"Logical Database Schema".
Show the normalization process and normalized tables for each relation to 3NF (if
applicable). Give the SQL statements for constructing the normalized table (if applicable).

8. The Database System
Give a brief description of how to install and invoke your system.
Provide the “screen dumps” showing how to use your system step by step.
9. Suggestions on Database Tuning (optional)
Give suggestions on tuning your database in terms of index structures, database design,
and/or queries.
10. Additional Queries and Views
Define at least 3 complex queries and/or 2 views. In the queries and views, you must
demonstrate the uses of aggregate operators, group by clause, order by clause, and nest
queries.
Show the SQL statement for each of the defined queries and views, and its corresponding
execution results.
11. User application interface: describe how you build the system user interface and how users
use your system. Give a list of functions that are offered by your system to the users. Explain
how the functions are implemented in SQL.
12. Conclusions and Future Work
Give a conclusion or your feedback about this project.
Provide a brief description of possible future work.
13. References
List the references or books used for this project.
14. Appendix
An appendix gives the zip file containing the work products (including demo slides, final
report, SQL scripts, and source code of the project).
The zip file must have the following directories for all the teams:
/doc (contain all documents and presentation slides)
/project (contain all source code, test code, data, web pages, SQL scripts, library, and
executable files )
a README file (describing how to install and use your program)
