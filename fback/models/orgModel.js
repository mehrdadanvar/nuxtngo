const mongoose = require("mongoose");
const orgSchema = mongoose.Schema({
  identity: String,
  name: String,
  category: String,
  link: String,
  description: Array,
  address: String,
  person: String,
  phone: String,
  social: Object,
},{collection:"organizations"});

module.exports = mongoose.model("Orgs", orgSchema,"organizations");
