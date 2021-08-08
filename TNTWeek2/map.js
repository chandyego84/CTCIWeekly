let myarr = ["Microsoft", "TNTs"];
console.log("Printing an array w/ map function:");
let printIt = (val) => console.log(val);

myarr.map(printIt)

const grades = [42, 69, 99, 100];
const fixedStudentGrades = grades.map(score=> score + 1);
console.log(fixedStudentGrades);
