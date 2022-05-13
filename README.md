# AirportHub_Management
UTD <br/>
CS 6360.003 Database Design<br/>
Database Project Description<br/>
Team Structure:<br/>
The project is a team project for students to learn how to become effective team players in a<br/>
software project. Each team may have 4-5 students (not 1, 2, or 3 and not 6), and one student<br/>
dedicates to the team leader. Each team member must contribute to all project deliverables.<br/>
Database Management System:<br/>
You are allowed to use any DBMS that is free and available to you such as MySQL, and a database 
connector such as JDBC to connect your Java (or any other language) front-end application to your 
MySQL database.<br/>
Project Narrative:<br/>
Airport officials have decided that all information related to the airport should be organized using a
DBMS and to build an Online Airport System, and you’ve been hired to design this system. Your task
is to organize the information about all the airplanes that are stationed and maintained at the airport. The
relevant information is as follows:<br/>
▪ Every airplane has a registration number, and each airplane is of a specific model.<br/>
▪ The airport accommodates a number of airplane models, and each model is identified by a model
number (e.g., DC-10) and has a capacity and a weight.<br/>
▪ A number of technicians work at the airport. You need to store the name, SSN, address, phone 
number, and salary of each technician.<br/>
▪ Each technician is a model(s), and his or her expertise may overlap with that of other technicians. This 
information about technicians must also be recorded.<br/>
▪ Traffic controllers must have an annual medical examination. For each traffic controller, you must 
store the date of the most recent exam.<br/>
▪ All airport employees (including technicians) belong to a union. You must store the union 
membership number of each employee. You can assume that each employee is uniquely identified
by the social security number.<br/>
▪ The airport has a number of tests that are used periodically to ensure that airplanes are still airworthy. 
Each test has a Federal Aviation Administration (FAA) test number, a name, and a maximum 
possible score.<br/>
▪ The FAA requires the airport to keep track of each time that a given airplane is tested by a given 
technician using a given test. For each testing event, the information needed is the date, the number 
of hours the technician spent doing the test, and the score that the airplane received on the test.<br/>

Functional Requirements:<br/>
An initial set of functional requirements for the Online Airport System are listed below, you should 
think of and write all other needed functional requirements for this project to be complete and 
practical. <br/>
Login Functional Requirements:<br/>
This is an initial set of login functional requirements; you may add more as needed.<br/><br/>
1: The system will allow the user to log in.<br/>
2. The system will verify the username and password.<br/>
3. The system will not allow the user to log in with an invalid username or password.<br/>
4. The system will be able to remember usernames and passwords.<br/>
5. The system will allow users to create accounts.<br/>
6. The system will enable users to log out of their accounts<br/>
Browsing Functional Requirements:<br/>
You should provide at least 10 browsing functional requirements for the Online Airport
System<br/>
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
Administrator Functional requirements <br/>
You should provide at least 10 administration functional requirements for the Online <br/>
Airport System<br/>
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

Assumptions<br/>
In doing your project, you will need to make additional assumptions as well as identify the 
potential inconsistencies and resolve them. Any reasonable assumptions are fine, but they must be 
documented in your reports. <br/>
Project Phases and Deliverables Items<br/>
Phase 1 (Due on Sunday 02/13/2022): Requirements Analysis (15%)<br/>
A system requirement specifications are due that includes:<br/>
a) System description<br/>
b) Context diagram (system architecture)<br/>
c) Functional requirements (user's operational concepts)<br/>
d) Non-functional requirements (e.g., response time, maintainability)<br/>
Phase 2 (Due on Sunday 03/06/2022): Conceptual and Logical Database Design (15%)<br/>
The following document is due for this phase<br/>
a) ER Diagram (including the description of the entities, attributes, keys, <br/>
cardinality, andparticipation constraints)<br/>
b) Database Schema<br/>
c) List of business rules and integrity constraints of the database.<br/>
d) Interface requirements<br/>
Phase 3: (Due on Sunday 04/03/2022) Normalization and Database Implementation and
Testing (25%)<br/>
The following tasks and documents are due for this phase<br/>
a) Specify a set of functional dependencies for each relation presented then show the <br/>
normalizationprocess and normalized tables for each relation to 3NF (if applicable).<br/>
b) Show the implementation of tables in the target DBMS (snapshots of tables in DBMS)<br/>
c) SQL statements for database construction and data population<br/>
d) Identify the functional dependencies of the database schema<br/>
e) Implementation and demonstration of the database system (snapshots of GUI)<br/>
f) Suggestions on database tuning in terms of index structures, database design, or queries.
(optional)<br/>
g) Additional queries and views (snapshots of query and view implementations)<br/>
Phase 4. (Due on Sunday 04/24/2022) Front end application (25%)<br/>
Your application program should consist of a continuous loop in which:<br/>
a) A list of at least five alternative options is offered to the user. (An additional
alternativeshould be quit.)<br/>
b) The user selects an alternative.<br/>
The last part of this assignment is to write an application that users can use to 
communicate with yourdatabase. This application should be written in a programming 
language of your choice (such as Java)that uses a DB connecter (such as JDBC) to connect 
to your database to manipulate the proper data.<br/>

c) The system prompts the user for appropriate input values.<br/>
d) The system accesses the database to perform the appropriate queries and/or modifications.<br/>
e) Data or an appropriate acknowledgment is returned to the user.<br/>
Both input and output in the application should be in a format more convenient and pleasing 
than rawinteractive SQL. Please include some interesting queries or modifications, i.e., 
operations that require some of the more complex SQL constructs such as subqueries, 
aggregates, set operators, etc. As a general example, if your database is a campus applicant
database, then your interface might include inits menu several useful queries on the database, 
with some queries performing statistical analysis requiring multiple levels of grouping, and 
other queries.<br/>
For this phase, just demonstrate this application to the TA during the final demo.<br/>
 Final Complete Project Report (Due: Monday 05/02/2022) (20%)<br/>
Submit a well written and complete report that includes the work that you have done in all the 
previous phases (one through four), The Contents of the Final Project Report should include,
but not be limited to the following sections:<br/>
1. Cover page<br/>
Provide the title of the course, the title of the project, the name of the instructor, names of
team members, and date.<br/>
2. Table of contents<br/>
Show the contents of the report and their corresponding page number.<br/>
3. Introduction<br/>
Provide a brief description of the project and the section organization of this report.<br/>
4. System Requirements<br/>
Give the context diagram (system architecture diagram) of the database system.<br/>
List the interface requirements of the system (or each subsystem).<br/>
List the functional and non-functional requirements of the database system.<br/>
5. Conceptual Design of the Database<br/>
The complete Entity-Relationship (ER) model of your database.<br/>
The data dictionary and business rules (i.e., constraints) of your ER model.<br/>
6. Logical Database Schema<br/>
Give the schema of the database which is restructured and translated from the ER diagram
presented in the section "Conceptual Design of the Database". Show the schema with
appropriate referential constraints. Give the SQL statements used to construct the schema. List
the expected database operations and estimated data volumes.<br/>
7. Functional Dependencies and Database Normalization<br/>
Identify and analyze the functional dependencies for each relation presented in the section
"Logical Database Schema".<br/>
Show the normalization process and normalized tables for each relation to 3NF (if
applicable). Give the SQL statements for constructing the normalized table (if applicable).<br/>

8. The Database System<br/>
Give a brief description of how to install and invoke your system.
Provide the “screen dumps” showing how to use your system step by step.<br/>
9. Suggestions on Database Tuning (optional)
Give suggestions on tuning your database in terms of index structures, database design,
and/or queries.<br/>
10. Additional Queries and Views<br/>
Define at least 3 complex queries and/or 2 views. In the queries and views, you must
demonstrate the uses of aggregate operators, group by clause, order by clause, and nest
queries.<br/>
Show the SQL statement for each of the defined queries and views, and its corresponding
execution results.<br/>
11. User application interface: describe how you build the system user interface and how users
use your system. Give a list of functions that are offered by your system to the users. Explain
how the functions are implemented in SQL.<br/>
12. Conclusions and Future Work<br/>
Give a conclusion or your feedback about this project.
Provide a brief description of possible future work.<br/>
13. References<br/>
List the references or books used for this project.<br/>
14. Appendix<br/>
An appendix gives the zip file containing the work products (including demo slides, final
report, SQL scripts, and source code of the project).<br/>
The zip file must have the following directories for all the teams:<br/>
/doc (contain all documents and presentation slides)
/project (contain all source code, test code, data, web pages, SQL scripts, library, and
executable files )<br/>
a README file (describing how to install and use your program)<br/>
