const express = require("express");
const dotenv = require("dotenv").config();
const mongoose = require("mongoose");
const cors = require("cors");
const {connectDB} = require("./config/db");
const corsOptions = {
    origin: "*",
    credentials: true, //access-control-allow-credentials:true
    optionSuccessStatus: 200,
  };
const port = process.env.PORT || 8000;
connectDB();
const app = express();
app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
// General Routes
app.get("/",(req,res)=>{
    res.send("Hi from backened")
})
app.use("/api/orgs",require("./routes/generalRoutes"))


app.listen(port,() => {
  console.log("connected to port?");
});
