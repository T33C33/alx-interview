0x04. Typescript

# JavaScriptTypeScript

**Weight:** 1  
**Project Duration:** Oct 9, 2024 6:00 AM to Oct 10, 2024 6:00 AM  
**Manual QA Review:** Oct 19, 2024 9:17 AM

## In a nutshell…

**Manual QA review:** 0.0/67 mandatory  
**Altogether:** 0.0%

- **Mandatory:** 0.0%
- **Optional:** no optional tasks

**Overall comment:**  
Project was failed automatically.

## Resources

**Read or watch:**

- TypeScript in 5 minutes
- TypeScript documentation

## Learning Objectives

By the end of this project, you should be able to explain the following without using Google:

- Basic types in TypeScript
- Interfaces, Classes, and functions
- How to work with the DOM and TypeScript
- Generic types
- How to use namespaces
- How to merge declarations
- How to use an ambient Namespace to import an external library
- Basic nominal typing with TypeScript

## Requirements

- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- All your files will be transpiled on Ubuntu 18.04
- Your TS scripts will be checked with jest (version 24.9.\*)
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `.ts` extension when possible
- The TypeScript compiler should not show any warning or error when compiling your code

## Configuration Files

Please use these files for the following tasks:

- `package.json`
- `.eslintrc.js`
- `tsconfig.json`
- `webpack.config.js`

## Tasks

### 0. Creating an interface for a student

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Copy the configuration files into the `task_0` directory. Write your code in `main.ts`:

- Create an interface named `Student` with `firstName`, `lastName`, `age`, and `location`.
- Create two students and an array `studentsList` containing them.
- Render a table using Vanilla JavaScript, appending a new row for each student with their first name and location.

**Requirements:**

- Webpack should return "No type errors found."
- Use TypeScript for every variable.

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_0/js/main.ts`, `task_0/package.json`, `task_0/.eslintrc.js`, `task_0/tsconfig.json`, `task_0/webpack.config.js`

### 1. Let's build a Teacher interface

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create a directory `task_1` and copy the configuration files into it. Define the `Teacher` interface:

- `firstName` and `lastName` (modifiable only during initialization)
- `fullTimeEmployee` (always defined)
- `yearsOfExperience` (optional)
- `location` (always defined)
- Allow additional attributes like `contract`.

**Example:**

```typescript
const teacher3: Teacher = {
  firstName: "John",
  fullTimeEmployee: false,
  lastName: "Doe",
  location: "London",
  contract: false,
};
console.log(teacher3);
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_1/js/main.ts`, `task_1/webpack.config.js`, `task_1/tsconfig.json`, `task_1/package.json`

### 2. Extending the Teacher class

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create an interface `Directors` extending `Teacher` with an additional attribute `numberOfReports`.

**Example:**

```typescript
const director1: Directors = {
  firstName: "John",
  lastName: "Doe",
  location: "London",
  fullTimeEmployee: true,
  numberOfReports: 17,
};
console.log(director1);
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_1/js/main.ts`

### 3. Printing teachers

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Write a function `printTeacher`:

- Accepts `firstName` and `lastName`
- Returns the first letter of `firstName` and the full `lastName`

**Example:**

```typescript
printTeacher("John", "Doe") -> J. Doe
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_1/js/main.ts`

### 4. Writing a class

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Write a class `StudentClass`:

- Constructor accepts `firstName` and `lastName`
- Method `workOnHomework` returns "Currently working"
- Method `displayName` returns `firstName`
- Describe the constructor and class through interfaces

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_1/js/main.ts`

### 5. Advanced types Part 1

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create interfaces `DirectorInterface` and `TeacherInterface` with specific methods. Implement classes `Director` and `Teacher` based on these interfaces. Create a function `createEmployee` that returns either a `Director` or `Teacher` based on the salary.

**Example:**

```typescript
console.log(createEmployee(200)); // Teacher
console.log(createEmployee(1000)); // Director
console.log(createEmployee("$500")); // Director
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_2/js/main.ts`, `task_2/webpack.config.js`, `task_2/tsconfig.json`, `task_2/package.json`

### 6. Creating functions specific to employees

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Write functions `isDirector` and `executeWork` to handle employee-specific tasks.

**Example:**

```typescript
executeWork(createEmployee(200)); // Getting to work
executeWork(createEmployee(1000)); // Getting to director tasks
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_2/js/main.ts`

### 7. String literal types

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Write a string literal type `Subjects` and a function `teachClass` to handle specific subjects.

**Example:**

```typescript
teachClass("Math"); // Teaching Math
teachClass("History"); // Teaching History
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_2/js/main.ts`

### 8. Ambient Namespaces

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create a directory `task_3` and copy the configuration files. Define types and interfaces in `interface.ts`. Write type declarations in `crud.d.ts` and use them in `main.ts`.

**Example:**

```typescript
const obj = { firstName: "Guillaume", lastName: "Salva" };
CRUD.insertRow(obj); // Insert row {firstName: "Guillaume", lastName: "Salva"}

const updatedRow: RowElement = {
  firstName: "Guillaume",
  lastName: "Salva",
  age: 23,
};
CRUD.updateRow(newRowID, updatedRow); // Update row 125 {firstName: "Guillaume", lastName: "Salva", age: 23}

CRUD.deleteRow(125); // Delete row id 125
```

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_3/js/main.ts`, `task_3/js/interface.ts`, `task_3/js/crud.d.ts`

### 9. Namespace & Declaration merging

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create a directory `task_4` and copy the configuration files. Define interfaces and classes in the `Subjects` namespace.

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_4/package.json`, `task_4/tsconfig.json`, `task_4/js/subjects/Cpp.ts`, `task_4/js/subjects/Java.ts`, `task_4/js/subjects/React.ts`, `task_4/js/subjects/Subject.ts`, `task_4/js/subjects/Teacher.ts`

### 10. Update task_4/js/main.ts

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create and export constants for `Cpp`, `Java`, and `React` subjects. Create a `Teacher` object `cTeacher` with `experienceTeachingC = 10`. Log the requirements and available teachers for each subject.

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- File: `task_4/js/main.ts`

### 11. Brand convention & Nominal typing

**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

Create a directory `task_5` and copy the configuration files. Define interfaces `MajorCredits` and `MinorCredits` with a brand property. Write functions `sumMajorCredits` and `sumMinorCredits` to sum the credits of two subjects.

**Repo:**

- GitHub repository: `alx-frontend-javascript`
- Directory: `0x04-TypeScript`
- Files: `task_5/js/main.ts`, `task_5/package.json`, `task_5/webpack.config.js`, `task_5/tsconfig.json`
