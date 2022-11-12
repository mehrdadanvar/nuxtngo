const express = require("express");
const router = express.Router();
const {main_get,main_post} = require("../controllers/generalController")


router.post("/", main_post);
router.get("/", main_get);



module.exports = router;