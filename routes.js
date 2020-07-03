/**
 * This module defines all API endpoints
 * and their handlers.
 */
const express = require("express");
const router = express.Router();

router.get("/music", (req, res) => {
  res.send({
    result: "OK"
  });
});

router.post("/like", (req, res) => {
  res.send({
    result: "OK"
  });
});

module.exports = router;
