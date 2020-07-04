/**
 * This module defines all API endpoints
 * and their handlers.
 */
const express = require('express');
const router = express.Router();

const songs = [
  {
    title: `Intro And Tarantelle`,
    artist: `ABC`,
    mood: 'regret',
    url: 'http://www.openmusicarchive.org/audio/Intro_And_Tarantelle.mp3',
  },
  {
    title: `Dont Go Way Nobody`,
    artist: `EFG`,
    mood: 'alone',
    url: 'http://www.openmusicarchive.org/audio/Dont_Go_Way_Nobody.mp3',
  },
  {
    title: `April Kisses`,
    artist: `HIJ`,
    mood: 'sad',
    url: 'http://www.openmusicarchive.org/audio/April_Kisses.mp3',
  },
  {
    title: `Eddies Twister`,
    artist: `KLM`,
    mood: 'relaxed',
    url: 'http://www.openmusicarchive.org/audio/Eddies_Twister.mp3',
  },
  {
    title: `Little Bits`,
    artist: `NOP`,
    mood: 'happy',
    url: 'http://www.openmusicarchive.org/audio/Little_Bits.mp3',
  },
];

router.get('/music', (req, res) => {
  // const candidates = [
  //   'http://www.openmusicarchive.org/audio/Intro_And_Tarantelle.mp3',
  //   'http://www.openmusicarchive.org/audio/Dont_Go_Way_Nobody.mp3',
  //   'http://www.openmusicarchive.org/audio/ancoats/Local%20Recall%20-%20Eileen%20Simpson%20and%20Ben%20White%20with%20live%20soundtrack%20by%20Graham%20Massey.mp3',
  //   'http://www.openmusicarchive.org/audio/April_Kisses.mp3',
  //   'http://www.openmusicarchive.org/audio/Eddies_Twister.mp3',
  //   'http://www.openmusicarchive.org/audio/Little_Bits.mp3',
  //   'http://www.openmusicarchive.org/audio/Struggling.mp3',
  //   'http://www.openmusicarchive.org/audio/Umbrellas_To_Mend.mp3',
  // ];
  res.status(200).json({
    status: 'success',
    results: songs.length,
    data: {
      songs,
    },
  });
});

router.post('/like', (req, res) => {
  res.send({
    result: 'OK',
  });
});

module.exports = router;
