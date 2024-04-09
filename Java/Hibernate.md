# Hibernate

## Basics
1. It is an ORM tool
2. We create objects and use save method to save them into db.
3. To use save method, we create an object of session factory and session, then use save method.
4. We use `hibernate.cfg.xml` file to configure hibernate. This file goes into the `src/main/resources` folder. The db data from this file is sent to session factory. 
5. We need two dependencies: hibernate-core and mysql-connector-java.
6. We use `@Entity` to declare a class as a table.
7. We use `@Id` to define a primary key attribute.