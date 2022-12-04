const csv = require("csv-parser");
const fs = require("fs");
const results = [];
const resultsWithRank = [];
const token = "Tokens Earned", title = "Title Earned";
fs.createReadStream("data/data.csv")
	.pipe(csv())
	.on("data", (data) => results.push(data))
	.on("end", () => {
		let id = 0;
		let institute = results[0]["Institution"];
		results.forEach((result) => {
			result.id = id++;
		});
		results.sort(
			(a, b) =>
				Number(b[token]) - (Number(a[token])) ||
				a["Name"] - b["Name"]
		);
		let rank = 1;

		results[0]["Rank"] = rank;

		for (let pointer = 1; pointer < results.length; pointer++) {
			let tokenPreviousRank =
				Number(results[pointer - 1][token]);
			let tokenRank =
				Number(results[pointer][token]);

			if (tokenRank === 0) {
				rank++;
				results[pointer]["Rank"] = rank;
			}
			else if (
				tokenPreviousRank ===
				tokenRank
			) {
				results[pointer]["Rank"] = results[pointer - 1]["Rank"];
			} else {
				rank++;
				results[pointer]["Rank"] = rank;
			}
		}

		for (let pointer = 1; pointer < results.length; pointer++) {
			let token1 =
				Number(results[pointer][token]);

			if (token1 > 1250) {
				results[pointer]["title"] = "Tech Guru";
			}
			else if (token1 > 800) {
				results[pointer]["title"] = "Tech Genius";
			}
			else if (token1 > 450) {
				results[pointer]["title"] = "Tech Star";
			}
			else if (token1 > 100) {
				results[pointer]["title"] = "Rising Star";
			}
			else {
				results[pointer]["title"] = "Newbie";
			}
		}

		results.forEach((result) => {
			let obj = {
				Rank: result["Rank"],
				"Name": result["Name"],
				"Enrolment Status": result["Enrolment Status"],
				"Tokens Earned": result[token],
				"Title Earned": result[title],
				id: result["id"],
			};

			resultsWithRank.push(obj);
		});

		fs.writeFile(
			"data/data.json",
			JSON.stringify({
				resultsWithRank,
				buildDate: new Date(Date.now()).toDateString(),
				institute,
			}),
			(err) => {
				if (err) throw err;
				console.log("Data file has been saved!");
			}
		);
	});
