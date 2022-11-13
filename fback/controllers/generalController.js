const asyncHandler = require("express-async-handler");
const Orgs = require("../models/orgModel");
const main_post = asyncHandler(async (req, res) => {
  if (req.body.test !== "mehrdad") {
    res.status(200).json({ error: "corrent route,incorrect body!" });
  } else {
    let data = await require("./organizations.json");
    let strategy = data.items;
    await Orgs.insertMany(strategy)
      .then(() => {
        console.log("inserted");
      })
      .catch((error) => {
        console.log(error);
      });
    console.log(strategy.length);
    console.log(req.body.test);
    console.log("rout post is working");
  }
});

const main_get = asyncHandler(async (req, res) => {
  console.log("route org is working");
  const orgs = await Orgs.find();
  console.log(orgs);
  res.send(orgs);
});
module.exports = {
  main_get,
  main_post,
};
