const page1 = document.querySelector('#page1');
const page2 = document.querySelector('#page2');

const showBoth = () => {
  page1.classList.remove('hide');
  page2.classList.remove('hide');
};

const showHome = () => {
  showBoth();
  stop();
  page2.classList.add('hide');
};

state = {};

const showPlayer = async () => {
  try {
    //=====================================api call============================================//
    const res = await axios(
      `https://hackcation-music.herokuapp.com/music?mood=${currMood}`
    );
    state.playlist = res.data;

    // //============================placeholder playlist===================================//
    // state.playlist = [
    //   {
    //     title: `Intro And Tarantelle`,
    //     artist: `ABC`,
    //     mood: 'regret',
    //     url: 'http://www.openmusicarchive.org/audio/Intro_And_Tarantelle.mp3',
    //   },
    //   {
    //     title: `Dont Go Way Nobody`,
    //     artist: `EFG`,
    //     mood: 'alone',
    //     url: 'http://www.openmusicarchive.org/audio/Dont_Go_Way_Nobody.mp3',
    //   },
    //   {
    //     title: `April Kisses`,
    //     artist: `HIJ`,
    //     mood: 'sad',
    //     url: 'http://www.openmusicarchive.org/audio/April_Kisses.mp3',
    //   },
    //   {
    //     title: `Eddies Twister`,
    //     artist: `KLM`,
    //     mood: 'relaxed',
    //     url: 'http://www.openmusicarchive.org/audio/Eddies_Twister.mp3',
    //   },
    //   {
    //     title: `Little Bits`,
    //     artist: `NOP`,
    //     mood: 'happy',
    //     url: 'http://www.openmusicarchive.org/audio/Little_Bits.mp3',
    //   },
    // ];

    showBoth();
    page1.classList.add('hide');

    document.querySelector('.bg-class').style.backgroundColor =
      colors[currMood];
    document.querySelector('.shock').style.backgroundColor = colors[currMood];
    document.querySelector('.glow').style.backgroundColor = colors[currMood];
    state.currIndex = 0;
    song.src = state.playlist[state.currIndex].url;
    song.play();
    shock.classList.add('btn--shockwave', 'is-active');
    document.querySelector('#song-name').innerHTML =
      state.playlist[state.currIndex].title;
    console.log(document.querySelector('#song-name').innerHTML);
    document.querySelector('#artist-name').innerHTML =
      state.playlist[state.currIndex].artist;
  } catch (err) {
    // alert(`Server Error`);
    console.log(err);
  }
};

document.querySelector('.recom-btn').addEventListener('click', showPlayer);
document.querySelector('.back').addEventListener('click', showHome);

const songEndedHandler = () => {
  state.currIndex++;
  if (state.currIndex < state.playlist.length) {
    currMood = state.playlist[state.currIndex].mood;
    document.querySelector('.bg-class').style.backgroundColor =
      colors[currMood];
    document.querySelector('.shock').style.backgroundColor = colors[currMood];
    document.querySelector('.glow').style.backgroundColor = colors[currMood];
    song.src = state.playlist[state.currIndex].url;
    document.querySelector('#song-name').innerHTML =
      state.playlist[state.currIndex].title;
    console.log(document.querySelector('#song-name').innerHTML);
    document.querySelector('#artist-name').innerHTML =
      state.playlist[state.currIndex].artist;
    song.play();
    shock.classList.add('btn--shockwave', 'is-active');
  } else {
    alert('Playlist Has Ended. How do you feel now?');
  }
};

song.addEventListener('ended', songEndedHandler);
