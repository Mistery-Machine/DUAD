const fs = require("fs");

fs.readFile("text.txt", "utf8", (error, data1) => {
  if (error) return console.log("We had a problem reading the file");

  fs.readFile("textOne.txt", "utf8", (error, data2) => {
    if (error) return console.log("We had a problem reading the file");

    const lista1 = data1.split(/\r?\n/).map((p) => p.trim());
    const lista2 = data2.split(/\r?\n/).map((p) => p.trim());

    const sameWords = lista1.filter((p) => lista2.includes(p) && p !== "");

    console.log("Hidden Message");
    console.log(sameWords.join(" "));
  });
});
