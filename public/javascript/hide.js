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

    showBoth();
    page1.classList.add('hide');
    state.currIndex = 0;
    // color filler

    document.querySelector('.bg-class').style.backgroundColor =
      colors[currMood];
    document.querySelector('.shock').style.backgroundColor = colors[currMood];
    document.querySelector('.glow').style.backgroundColor = colors[currMood];

    // NULL URL FIX
    while (!state.playlist[state.currIndex].url) state.currIndex++;

    song.src = state.playlist[state.currIndex].url;
    song.play();
    shock.classList.add('btn--shockwave', 'is-active');
    document.querySelector('#song-name').innerHTML =
      state.playlist[state.currIndex].title;
    console.log(document.querySelector('#song-name').innerHTML);
    document.querySelector('#artist-name').innerHTML =
      state.playlist[state.currIndex].artist;
  } catch (err) {
    alert(`Server Error`);
    console.log(err);
  }
};

document.querySelector('.recom-btn').addEventListener('click', showPlayer);
document.querySelector('.back').addEventListener('click', showHome);

const songEndedHandler = () => {
  state.currIndex++;
  if (state.currIndex < state.playlist.length) {
    moods = ['#64BCDE', '#b8b8f4', '#F6914F', '#F9CA79', '#93A3ED', '#F9CCE4'];
    // color changer
    document.querySelector('.bg-class').style.backgroundColor =
      moods[state.currIndex % moods.length];
    document.querySelector('.shock').style.backgroundColor =
      moods[state.currIndex % moods.length];
    document.querySelector('.glow').style.backgroundColor =
      moods[state.currIndex % moods.length];

    // NULL URL FIX
    while (!state.playlist[state.currIndex].url) state.currIndex++;

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
